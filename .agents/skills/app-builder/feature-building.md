# Feature Building

> How to analyze and implement new features.

## Feature Analysis

```
Request: "add payment system"

Analysis:
├── Required Changes:
│   ├── Database: orders, payments tables
│   ├── Backend: /api/checkout, /api/webhooks/stripe
│   ├── Frontend: CheckoutForm, PaymentSuccess
│   └── Config: Stripe API keys
│
├── Dependencies:
│   ├── stripe package
│   └── Existing user authentication
│
└── Scope: DB + 2 API routes + 2 components + config
```

## Iterative Enhancement Process

```
1. analyze project and architecture
2. create scoped change plan
3. align DESIGN.md when UI changes
4. obtain any required approval
5. apply scoped changes
6. test and validate
7. verify behavior
8. preview only when appropriate

*Note: Integrate `verify-changes` semantics. Do not equate 'tests passed' with 'authorized to merge/deploy'.*
```

## 🛡️ JINC Governance: Human Gate

Technical planning, successful scaffolding, passing tests, successful preview, or verification evidence do not authorize consequential actions. Actions such as merge, deployment, publication, release, protected-branch push, or infrastructure mutation remain subject to explicit Human Gate requirements.

## Error Handling

| Error Type         | Solution Strategy                    |
| ------------------ | ------------------------------------ |
| TypeScript Error   | Fix type, add missing import         |
| Missing Dependency | Run npm install                      |
| Port Conflict      | Suggest alternative port             |
| Database Error     | Check migration, validate connection |

## Recovery Strategy

```
1. Detect error
2. Try automatic fix
3. If failed, report to user
4. Suggest alternative
5. Rollback if necessary
```
