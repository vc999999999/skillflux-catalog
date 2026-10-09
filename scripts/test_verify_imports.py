import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from verify_imports import verify_catalog, verify_record


class VerifyImportsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / "intake/example"
        self.directory.mkdir(parents=True)
        contents = {"SKILL.md": b"Read assets/model.bin", "assets/model.bin": b"\x00\xff\x80\x01"}
        self.record = {"target": "intake/example", "files": {}, "upstreamFiles": {}}
        for name, data in contents.items():
            path = self.directory / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            self.record["files"][name] = hashlib.sha256(data).hexdigest()
            blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            self.record["upstreamFiles"][name] = {"gitBlobSha": blob, "size": len(data)}

    def test_binary_resources_are_checked_without_decoding(self):
        self.assertEqual(verify_record(self.root, self.record)["files"], 2)

    def test_missing_resource_fails_even_when_entry_is_present(self):
        (self.directory / "assets/model.bin").unlink()
        with self.assertRaisesRegex(ValueError, "missing=.*assets/model.bin"):
            verify_record(self.root, self.record)

    def test_changed_bytes_fail(self):
        (self.directory / "assets/model.bin").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            verify_record(self.root, self.record)

    def test_updated_local_hash_does_not_hide_upstream_changes(self):
        data = b"changed"
        (self.directory / "assets/model.bin").write_bytes(data)
        self.record["files"]["assets/model.bin"] = hashlib.sha256(data).hexdigest()
        with self.assertRaisesRegex(ValueError, "upstream bytes mismatch"):
            verify_record(self.root, self.record)

    def test_extra_file_fails(self):
        (self.directory / "surprise.sh").write_bytes(b"echo unexpected")
        with self.assertRaisesRegex(ValueError, "unexpected=.*surprise.sh"):
            verify_record(self.root, self.record)

    def test_paths_cannot_escape_package_or_catalog(self):
        for target in ("../elsewhere", "/tmp/elsewhere", "intake/../elsewhere", "intake\\elsewhere"):
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "unsafe path"):
                verify_record(self.root, dict(self.record, target=target))
        self.record["files"]["../outside"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "unsafe path"):
            verify_record(self.root, self.record)

    def test_symlink_is_rejected(self):
        (self.directory / "linked").symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            verify_record(self.root, self.record)

    def test_catalog_metadata_is_separate_from_imported_bytes(self):
        target = self.root / "skills/test/example/1.0.0"
        target.parent.mkdir(parents=True)
        self.directory.rename(target)
        self.record["target"] = "skills/test/example/1.0.0"
        (target / "skillflux.json").write_text("{}")
        (target / "skillflux.review.json").write_text("{}")
        self.assertTrue(verify_record(self.root, self.record)["original"])

    def test_executable_mode_is_preserved(self):
        self.record["upstreamFiles"]["SKILL.md"]["mode"] = "100755"
        with self.assertRaisesRegex(ValueError, "mode mismatch"):
            verify_record(self.root, self.record)

    def test_unregistered_intake_skill_cannot_bypass_verification(self):
        imports = self.root / "imports"
        imports.mkdir()
        (imports / "example.json").write_text(json.dumps({
            "schema": "skillflux-import-audit/v1", "records": [self.record]}))
        self.assertEqual(len(verify_catalog(self.root)[0]), 1)
        orphan = self.root / "intake/unregistered/SKILL.md"
        orphan.parent.mkdir()
        orphan.write_text("Read missing scripts/render.py")
        with self.assertRaisesRegex(ValueError, "missing from import inventories"):
            verify_catalog(self.root)


if __name__ == "__main__":
    unittest.main()
