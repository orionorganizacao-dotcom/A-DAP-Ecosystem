# A-DAP Evidence Map v0.1

Status: Prototype Evidence Layer

Objective: Hostile Independent Validation

---

## Core Claim

A-DAP does not prove that a decision is correct.

A-DAP preserves independent evidence that a decision existed before its outcome was observed.

---

## Evidence Structure

| Claim | Artifact | Observable | Verification | Status |
|---|---:|---:|---:|---:|
| Decision existed before outcome | minimal-envelope.json | SHA256 | verify_adap.py | Pending |
| Decision integrity preserved | ledger.sha256 | Hash mismatch | Tamper test | Pending |
| Verification reproducible | verify_adap.py | PASS/FAIL | Run locally | Pending |
| Auditability is architectural | protocol flow | reconstruction path | documentation review | Draft |

---

## Validation Goal

The objective is not persuasion.

The objective is reproducibility.

---

## Current Status

Internal validation complete.

External hostile validation pending.
