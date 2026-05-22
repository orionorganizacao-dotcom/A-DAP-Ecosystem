# A-DAP Ecosystem

Infrastructure for verifiable decision systems and independent reconstruction.

---

## What is A-DAP?

A-DAP (Auditable Decision Accountability Protocol) is an architecture for preserving verifiable evidence in decision systems.

Traditional systems typically preserve:

- outputs
- logs
- explanations

A-DAP preserves something different:

existence, integrity, and temporality of a decision before its outcome becomes observable.

The objective is not merely to explain what happened.

The objective is to preserve independent evidence that something existed before the result.

---

## Core Principle

Decision ≠ Record ≠ Justification ≠ Proof

Explanation after execution does not necessarily imply verification before execution.

---

## Repository Map

| Repository | Purpose |
|-------------|----------|
| A-DAP-OS | Foundational principles and architecture |
| adap-v2-protocol | Protocol definition |
| adap-verifiability-core | Core implementation primitives |
| adap-minimal-verifiability | Minimal verifiability implementation |
| adap-verifiability-experiment | Experimental validation |
| observational-asymmetry-hypothesis | Research extension |

---

## Ecosystem Structure

A-DAP

├── Foundation  
│ └── A-DAP-OS  
│

├── Protocol  
│ └── adap-v2-protocol  
│

├── Core  
│ └── adap-verifiability-core  
│

├── Experiments  
│ ├── adap-minimal-verifiability  
│ └── adap-verifiability-experiment  
│

└── Research  
└── observational-asymmetry-hypothesis  

---

## Architectural Position

A-DAP does not attempt to prove:

- truth
- correctness
- institutional accountability

A-DAP attempts to preserve:

- evidence
- reconstruction
- independent verifiability

---

## Status

Current stage:

Research + Architecture + Experimental Validation

Future stages:

- external adversarial review
- cryptographic timestamp integration
- reproducible experiments
- formal publication
