# Postmortem — <short title>

> Copy this file as `postmortems/YYYY-MM-DD-<short-title>.md`.
> **Blameless:** describe what the system and the process allowed to happen, not who made a mistake.

| Field            | Value                                    |
| ---------------- | ---------------------------------------- |
| Date             | YYYY-MM-DD                               |
| Type             | Real incident / Game day                 |
| Severity         | SEV1 / SEV2 / SEV3                       |
| Duration         | Start → end (total minutes)              |
| Time to detect   | minutes                                  |
| Time to mitigate | minutes                                  |
| Author           |                                          |
| Status           | Draft / Reviewed / Action items done     |

## Summary

Two or three sentences: what happened, the impact, how it was fixed.

## Impact

- Users affected:
- Requests failed / slowed:
- SLO and error budget consumed:

## Timeline (UTC)

| Time  | Event                                              |
| ----- | -------------------------------------------------- |
| 10:02 | Deployment of image `sha-abc123`                   |
| 10:05 | Alert `TasksApiHighErrorRate` fires                |
| 10:07 | Investigation starts, runbook opened               |
| 10:12 | Rollback triggered                                 |
| 10:15 | Error rate back to normal — incident mitigated     |

## Root cause

What actually caused the problem. Use the **5 whys**:

1. Why did the API return errors? →
2. Why…? →
3. Why…? →
4. Why…? →
5. Why…? →

## Detection

How was it detected? Would users have noticed first? Was the alert fast and clear enough?

## What went well

-

## What went wrong

-

## Where we got lucky

-

## Action items

| Action                                   | Type        | Owner | Status | Link |
| ---------------------------------------- | ----------- | ----- | ------ | ---- |
| Add an alert on …                        | Detect      | me    | ⬜     |      |
| Add a test that would have caught …      | Prevent     | me    | ⬜     |      |
| Update runbook …                         | Mitigate    | me    | ⬜     |      |

## Lessons learned

What would I do differently next time?
