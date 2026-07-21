# System Architecture — composition reference

**Slug:** `architecture` · **Tool:** Excalidraw (Mermaid `architecture-beta` v11+, or `flowchart`) · **Phase:** 4, 6 · **Source of truth:** tech stack + components

## Purpose
Show the high-level structure of a system — the main layers (frontend, backend/API, services, data, external integrations) and how they communicate (protocols/data flows). Supports decisions on responsibility split, technology choice, and integration points.

## When to use / when NOT
- **Use** to plan/document overall software architecture (new design or evaluating an existing one).
- **NOT** for dynamics (→ `sequence`/`state`), data modeling (→ `erd`), or process (→ `bpmn`). For a rigorous, layered abstraction hierarchy prefer **`c4`**.

## Element vocabulary
| Element | Meaning | Rules |
|---|---|---|
| Rectangle | **Component / Service** | An app module/service. Named by function (no logos). |
| Cylinder | **Database / Store** | Persistent storage; name + type (RDB/NoSQL). |
| Cloud / grey box | **External system** | Third-party/outside system. At the edge, labelled. |
| Stick figure | **User / Actor** | Person/role interacting with the system. Outside the layers. |
| One-way arrow | **Communication / Dependency** | A call/data transfer. Always directed and labelled (protocol/data). |
| Arrow label | **Connection label** | e.g. "HTTPS", "SQL", "JSON". Consistent wording. |
| Band / zone | **Layer** | Logical group (Frontend, API, Data). Top-to-bottom order. |

## Composition rules
- Connect only sensible pairs: component→component, component→DB, component→external, actor→component.
- Arrows are **one-way** and **labelled** (verb/protocol). Two-way = two opposed labelled arrows.
- Keep layers ordered (presentation → application → data). No frontend → DB skip past the backend.
- Arrange to minimize crossing lines (the "wire mess" anti-pattern); re-layout or use separate lanes.
- Don't mix static architecture with deployment/infrastructure detail — that's a separate deployment diagram.

## Canonical structure
Three stacked horizontal layers + side blocks for external systems:
- **Presentation:** Web UI, Mobile App.
- **Business/logic:** API server, microservices, auth service.
- **Data:** relational DB, cache, NoSQL.
- **External:** cloud APIs, payment gateways (at the sides).
```
Web UI ──HTTPS──▶ API Server ──JDBC──▶ Database
                     └──gRPC──▶ Auth Service
API Server ──HTTPS──▶ External Payment API
```

## Anti-patterns
- Crossing-line chaos ("wire mess").
- Unlabelled / generic arrow labels ("uses") — use "HTTPS/JSON", "JDBC".
- Decorative logos/icons instead of named boxes.
- Mixing abstraction levels (architecture + code/infra in one picture).
- Missing title/legend; inconsistent naming ("DB" vs "Database").

## Rendering
- **Mermaid:** `architecture-beta` (v11+): `group frontend(browser)[Front-end]`, `service web(browser)[Web UI] in frontend`, arrows `web -->|HTTPS/JSON| api`. Fallback: plain `flowchart LR; UI -->|HTTPS| API; API -->|SQL| DB`.
- **Excalidraw:** boxes + arrows with generous spacing. Colors: own components blue, external grey, data green; distinct color per layer, kept consistent in a legend. Layers vertical (frontend top → backend → data). Align within a layer; label protocols on arrows; add a legend if not obvious.

## Required inputs
- System name (title).
- Layer definitions (Frontend/UI, Backend/API, Services, Data, External).
- Components per layer (name + short description / tech).
- Connections: source → target + label (protocol/data), with direction.
- External systems and actors.

## Worked example
```mermaid
architecture-beta
group frontend(browser)[Front-end]
service web(browser)[Web App] in frontend
service mobile(browser)[Mobile App] in frontend
service api(server)[API Server]
service auth(lock)[Authentication Service]
service db(database)[Main Database]
web -->|HTTPS/JSON| api
mobile -->|HTTPS/JSON| api
api -->|gRPC| auth
api -->|JDBC| db
```
