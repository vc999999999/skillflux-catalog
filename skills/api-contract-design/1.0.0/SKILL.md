---
name: api-contract-design
description: Define HTTP API contracts that clients can implement and verify.
---

# API contract design

Start from the client actions and existing routes. For each operation specify method, path, request schema, response schema, expected status codes and authorization boundary. Separate resource identifiers from user-supplied paths and URLs.

Specify cursor or offset semantics, stable ordering, pagination bounds and empty results. For writes define idempotency behavior, transaction boundaries and what happens when a retry arrives after a partial failure. Validate resource ownership before applying changes.

Use a consistent error envelope with machine-readable codes and useful messages. Include one valid and one invalid request for each nontrivial operation. Keep examples internally consistent with real models. Add compatibility rules before changing existing response fields.

Verify the contract through request-level tests, including malformed bodies, permission failures, missing resources and duplicate writes. Do not invent successful backend behavior in client mocks when reporting implementation status.
