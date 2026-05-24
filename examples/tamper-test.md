# A-DAP Tamper Test v0.1

## Objective

Demonstrate that A-DAP evidence changes when the decision artifact is modified.

This test does not prove correctness.

This test demonstrates detectable integrity failure.

---

## Procedure

Step 1

Run:

```bash
python verify_adap.py
```

Expected:

```text
PASS
```

---

Step 2

Open:

minimal-envelope.json

Modify one character only.

Example:

Original:

decision = APPROVE

Modified:

decision = REJECT

---

Step 3

Run again:

```bash
python verify_adap.py
```

Expected:

```text
FAIL
Hash mismatch detected
```

---

## Interpretation

If a one-byte modification invalidates verification:

Integrity preservation exists.

If modifications remain undetected:

The mechanism fails.
