import json
import hashlib

with open("examples/minimal-envelope.json","r") as f:
    data = json.load(f)

decision = data["decision"]

computed = hashlib.sha256(
    decision.encode()
).hexdigest()

print("Computed:", computed)
print("Stored:", data["decision_hash"])

if computed == data["decision_hash"]:
    print("PASS")
else:
    print("FAIL")
