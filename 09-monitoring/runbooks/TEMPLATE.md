# Runbook — <alert name>

> Copy this file as `runbooks/<alert-name>.md`. The alert's description must link here.

| Field         | Value                                       |
| ------------- | ------------------------------------------- |
| Alert         | e.g. `TasksApiHighErrorRate`                |
| Severity      | SEV1 / SEV2 / SEV3                          |
| Service       | Tasks API                                   |
| Last reviewed | YYYY-MM-DD                                  |

## What this alert means

One or two sentences: what is broken, from the user's point of view.

## Impact

Who is affected and how (e.g. "users cannot create tasks").

## First checks (5 minutes)

1. Open the dashboard: <link>
2. Was there a deployment recently? `git log` / pipeline history / `kubectl rollout history`
3. Check health endpoints: `curl -s https://<host>/health` and `/ready`
4. Check recent errors in Loki: `{app="tasks-api"} | json | level="ERROR"`

## Mitigation

Fastest way to stop the impact, even before the root cause is known:

- Roll back: `<command>`
- Restart: `<command>`
- Scale up: `<command>`

## Diagnosis

Deeper steps once the impact is under control.

## Escalation

Who or what to contact if the steps above do not work.

## Related

- Postmortems: <links>
- Dashboards: <links>
