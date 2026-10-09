#!/usr/bin/env python3
"""Check collected package bytes against import inventories without executing them."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys

METADATA = {"skillflux.json", "skillflux.review.json", "index.json"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_path(root, relative):
    require(isinstance(relative, str) and relative, "empty/non-string path")
    parts = relative.split("/")
    require(not PurePosixPath(relative).is_absolute()
            and all(p not in ("", ".", "..") for p in parts)
            and "\\" not in relative and "\x00" not in relative,
            f"unsafe path: {relative!r}")
    path = root
    for part in parts:
        path = path / part
        require(not path.is_symlink(), f"symlink is not supported: {path}")
    return path


def inventory(directory, excluded=()):
    require(not directory.is_symlink(), f"symlink is not supported: {directory}")
    require(directory.is_dir(), f"missing package directory: {directory}")
    result = {}
    for path in sorted(directory.rglob("*")):
        mode = path.lstat().st_mode
        require(not stat.S_ISLNK(mode), f"symlink is not supported: {path}")
        if stat.S_ISDIR(mode):
            continue
        require(stat.S_ISREG(mode), f"non-regular file: {path}")
        relative = path.relative_to(directory).as_posix()
        if relative not in excluded:
            safe_path(directory, relative)
            result[relative] = path.read_bytes()
    return result


def verify_record(root, record):
    target = record.get("target")
    if target is None:
        require(record.get("disposition") == "source-only",
                "only source-only records may omit target")
        return None
    directory = safe_path(root, target)
    require(target.split("/")[0] in ("skills", "intake"),
            f"target must be under skills/ or intake/: {target}")
    files = record.get("files")
    require(isinstance(files, dict) and files, "missing file inventory")
    for name, digest in files.items():
        safe_path(directory, name)
        require(isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest),
                f"invalid SHA-256 for {name}")
    actual = inventory(directory, METADATA if target.startswith("skills/") else ())
    missing = sorted(files.keys() - actual.keys())
    extra = sorted(actual.keys() - files.keys())
    require(not missing and not extra, f"inventory mismatch; missing={missing}, unexpected={extra}")
    for name, content in actual.items():
        require(hashlib.sha256(content).hexdigest() == files[name], f"SHA-256 mismatch: {name}")
    upstream = record.get("upstreamFiles")
    if upstream is not None:
        require(isinstance(upstream, dict) and upstream, "empty upstream inventory")
        for name, source in upstream.items():
            safe_path(directory, name)
            require(name in actual, f"missing original upstream file: {name}")
            require(isinstance(source, dict), f"invalid upstream entry: {name}")
            content = actual[name]
            blob = hashlib.sha1(b"blob " + str(len(content)).encode("ascii") + b"\0" + content).hexdigest()
            require(source.get("gitBlobSha") == blob and source.get("size") == len(content),
                    f"upstream bytes mismatch: {name}")
            if "mode" in source:
                mode = "100755" if (directory / name).stat().st_mode & 0o111 else "100644"
                require(source["mode"] == mode, f"upstream executable mode mismatch: {name}")
    return {"target": target, "files": len(files), "original": upstream is not None,
            "paths": [f"{target}/{name}" for name in files]}


def verify_catalog(root):
    root = root.resolve()
    manifests = sorted((root / "imports").glob("*.json"))
    require(manifests, "no import manifests found")
    results, errors, source_only = [], [], 0
    for manifest in manifests:
        try:
            require(not manifest.is_symlink(), "manifest may not be a symlink")
            data = json.loads(manifest.read_text(encoding="utf-8"))
            require(data.get("schema") == "skillflux-import-audit/v1", "unsupported import schema")
            require(isinstance(data.get("records"), list) and data["records"], "missing records")
            for record in data["records"]:
                try:
                    require(isinstance(record, dict), "record must be an object")
                    result = verify_record(root, record)
                    if result is None:
                        source_only += 1
                    else:
                        results.append(result)
                except (ValueError, OSError) as exc:
                    errors.append(f"{manifest.name} [{record.get('id', '?') if isinstance(record, dict) else '?'}]: {exc}")
        except (ValueError, OSError, AttributeError) as exc:
            errors.append(f"{manifest.name}: {exc}")
    # Reverse coverage prevents unregistered, Markdown-only copies bypassing CI.
    if (root / "intake").exists():
        try:
            covered = {path for result in results for path in result["paths"]}
            unlisted = sorted(f"intake/{name}" for name in inventory(root / "intake")
                              if f"intake/{name}" not in covered)
            require(not unlisted, f"intake files missing from import inventories: {unlisted}")
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
    require(not errors, "\n".join(errors))
    return results, source_only


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        results, sources = verify_catalog(args.catalog)
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    unique = {r["target"] for r in results}
    original = {r["target"] for r in results if r["original"]}
    print(f"Verified {len(unique)} package/resource directories against SHA-256 inventories; "
          f"{len(original)} also match original Git blob inventories; {sources} source-only records skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
