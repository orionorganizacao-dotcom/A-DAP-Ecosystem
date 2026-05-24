# A-DAP Tamper Test

Initial state:

decision = APPROVE

Expected:

Computed hash == Stored hash
PASS

Tamper scenario:

decision = REJECT

Expected:

Computed hash != Stored hash
FAIL

Purpose:

Demonstrate integrity preservation and tamper detection.
