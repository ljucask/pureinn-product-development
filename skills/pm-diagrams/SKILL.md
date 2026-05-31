---
name: pm-diagrams
description: Generate visual diagrams using Excalidraw. Supports: Domain Model overview, User Flow, Business Process Model, System Architecture, JTBD Four Forces. Renders inline and exports to excalidraw.com for sharing and editing. Can be called at any phase.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: diagrams, visual diagram, domain model diagram, user flow, business process, system architecture, JTBD forces, Excalidraw
  role: specialist
  scope: visualization
  output-format: diagram
  related-skills: pm-domain-model, jtbd-building, pm-fsd
---

# PM - Diagrams

## What this skill does

Generates hand-drawn visual diagrams using Excalidraw. Renders inline in the conversation and optionally exports a shareable link to excalidraw.com.

Supported diagram types:

| Type | Best used in | Primary input |
|---|---|---|
| Domain Model Overview | Phase 4 | Domain Model artifact (pm-domain-model output) |
| User Flow | Phase 2, Phase 6 | Feature description, user journey steps |
| Business Process Model | Phase 2, FI | Process steps, actors, decision points |
| System Architecture | Phase 4, Phase 6 | Tech stack, components, integrations |
| JTBD Four Forces | Phase 2 | JTBD Analysis output (jtbd-building) |

This skill is standalone - it can be called at any point without running a specific phase first. It complements `pm-domain-model` (which also generates its own Excalidraw diagram at Stage 1 and Stage 2).

---

## Dependencies

**No hard dependencies.** Works from raw input or from existing artifacts.

**Best used with:**
- `pm-domain-model` output → Domain Model Overview diagram
- `jtbd-building` output → JTBD Four Forces diagram
- `pm-fsd` or feature description → User Flow diagram

---

## Step 0: Current state check

Check if a previous diagram checkpoint exists for this project in the session context.

If checkpoint exists: offer to continue from it (add elements, update, or start fresh).
If no checkpoint: proceed to Step 1.

Apply the standard skill interaction pattern (CLAUDE.md).

**Options:**

```
What diagram do you want to create?
  A) Domain Model Overview - domains, entities, relationships
  B) User Flow - step-by-step flow for a feature or process
  C) Business Process Model - BPMN-style with swim lanes and actors
  D) System Architecture, JTBD Four Forces, or something else - describe what you need
```

---

## Step 1: Gather inputs

### A) Domain Model Overview

```
For the Domain Model Overview, I need:

1. DOMAINS (from your domain model)
   List each domain and its key entities:
   e.g., "Identity: User, Profile, Session"
       "Booking: Booking, BookingRequest"
   [paste or list]

2. DOMAIN RELATIONSHIPS
   Which domains reference which others?
   e.g., "Booking references Identity (user), Booking references Property"
   [describe or paste from domain model]

3. EXTERNAL SYSTEMS (optional)
   Any external integrations to show? (Stripe, Twilio, Google Maps...)

4. FOCUS AREA (optional)
   Show all domains, or zoom into a specific area?
```

### B) User Flow

```
For the User Flow diagram, I need:

1. FEATURE OR PROCESS NAME
   What is being mapped?

2. ACTOR(S)
   Who performs the actions? (e.g., Guest, Host, Admin, System)

3. FLOW STEPS
   List the steps in order. Mark decision points with "?" and system actions with "[system]":
   e.g.,
   1. User opens checkout
   2. User enters payment details
   3. [system] Validates payment
   4. ? Payment valid
      YES → Booking confirmed
      NO → Show error, allow retry
   5. [system] Sends confirmation email
   [list your steps]

4. HAPPY PATH vs. FULL FLOW
   Happy path only, or include error states and edge cases?
```

### C) Business Process Model

```
For the Business Process Model, I need:

1. PROCESS NAME
   What business process is being modeled?

2. ACTORS / SWIM LANES
   Who are the participants? Each gets their own lane.
   e.g., Guest, Host, Platform, Payment Provider

3. PROCESS STEPS PER ACTOR
   For each actor, what do they do?
   Mark handoffs (when control passes from one actor to another).
   Mark decision points and their outcomes.

4. START AND END EVENTS
   What triggers the process? What does "done" look like?

5. SCOPE
   All happy path only, or include exceptions and error handling?
```

### D) System Architecture

```
For the System Architecture diagram, I need:

1. LAYERS
   What are the main architectural layers?
   e.g., Frontend / Backend API / Services / Database / External APIs

2. COMPONENTS PER LAYER
   List the components in each layer:
   e.g., "Frontend: Next.js app, Admin dashboard"
        "Backend: REST API, Auth service, Notification service"
        "Database: PostgreSQL, Redis cache"
        "External: Stripe, SendGrid, AWS S3"

3. KEY CONNECTIONS
   Which components talk to which? Any important data flows to highlight?

4. SCOPE
   Full system overview, or zoom into a specific area (e.g., just the auth flow)?
```

### E) JTBD Four Forces

```
For the JTBD Four Forces diagram, I need:

1. CURRENT SOLUTION (what users do today)
   What tool, process, or workaround are they switching from?

2. NEW SOLUTION (your product)
   What are they switching to?

3. PUSH FORCES (what drives them away from current solution)
   What frustrations, pain points, or limitations make them want to switch?
   (3-5 specific pain points)

4. PULL FORCES (what attracts them to your solution)
   What specific benefits or capabilities attract them to switch?
   (3-5 specific gains)

5. ANXIETY FORCES (what holds them back from switching)
   What fears, uncertainties, or concerns stop them from switching?
   (2-4 specific anxieties)

6. HABIT FORCES (what keeps them attached to the current solution)
   What comfortable routines, sunk costs, or switching costs anchor them?
   (2-4 specific habits)
```

---

## Step 2: Generate diagram

Generate the Excalidraw diagram using `mcp__claude_ai_Excalidraw__create_view`.

### Visual conventions per diagram type

---

#### Domain Model Overview

Layout: domains as large zone rectangles (background, opacity 35), entities as small rounded rectangles inside their domain, external systems in a separate zone (light orange background).

Color scheme:
- Identity/Auth domain: Light Blue (`#dbe4ff`) zone
- Core business domain (primary): Light Purple (`#e5dbff`) zone
- Supporting domains: Light Green (`#d3f9d8`) zone
- Payments/Finance domain: Light Teal (`#c3fae8`) zone
- External systems: Light Orange (`#ffd8a8`) zone
- Relationship arrows: `#1e1e1e`, `endArrowhead: "arrow"`

Layout guidance:
- Camera XL (1200x900) for products with 4+ domains
- Camera L (800x600) for 2-3 domains
- Domains arranged left-to-right or in a hub pattern depending on relationships
- Entity rectangles: 140x50, `fontSize: 16`, inside their domain zone
- Domain labels: top-left of zone, `fontSize: 18`, bold, domain color
- Relationship arrows connect domain zones, not individual entities
- Label arrows with the key reference (e.g., "booking ref", "user ref")

---

#### User Flow

Layout: top-to-bottom flow. Start ellipse at top, end ellipse at bottom. Decision diamonds expand horizontally.

Color scheme:
- Start/End ellipses: Light Green (`#b2f2bb`), stroke `#22c55e`
- User action steps: Light Blue (`#a5d8ff`), stroke `#4a9eed`
- System actions: Light Purple (`#d0bfff`), stroke `#8b5cf6`
- Decision diamonds: Light Yellow (`#fff3bf`), stroke `#f59e0b`
- Error/failure paths: Light Red (`#ffc9c9`), stroke `#ef4444`
- Arrows: `#1e1e1e`, label with action name if not obvious

Layout guidance:
- Camera M (600x450) for simple flows (5-8 steps)
- Camera XL (1200x900) for complex flows with branches
- Step rectangles: 200x60, rounded corners, `fontSize: 16`
- Decision diamonds: 160x80
- Happy path flows vertically; alternative paths branch horizontally
- System actions shown with dashed border or distinct purple fill
- Use camera panning to reveal flow progressively (top → bottom)

---

#### Business Process Model

Layout: horizontal swim lanes, one per actor. Process flows left-to-right within lanes. Handoffs shown as arrows crossing lane boundaries.

Color scheme:
- Lane headers: match actor role color (User → Blue, System → Purple, External → Orange)
- Lane backgrounds: alternating light/white for readability
- Activity rectangles: Light Blue (`#a5d8ff`)
- Decision gateways: Light Yellow (`#fff3bf`), diamond shape
- Start event: Green ellipse (small, 40x40)
- End event: Red ellipse with thick border (small, 40x40)
- Handoff arrows: cross lane boundary, label with what is passed

Layout guidance:
- Camera XL (1200x900) for 3+ actors
- Lane height: 120px per actor, separator line between lanes
- Activities: 150x50 rectangles
- Flow left to right, top of diagram = start of process
- Decision points expand the lane temporarily for branching

---

#### System Architecture

Layout: horizontal layers stacked top-to-bottom (Frontend → Backend → Database → External). Components arranged within their layer.

Color scheme:
- Frontend layer: Blue zone (`#dbe4ff`)
- Backend/API layer: Purple zone (`#e5dbff`)
- Data/Storage layer: Teal zone (`#c3fae8`)
- External/Integration layer: Orange zone (`#ffd8a8`)
- Component boxes: white/light fill matching layer, rounded corners
- Connection arrows: `#1e1e1e`, label with protocol or data type

Layout guidance:
- Camera XL (1200x900) for full system
- Layer backgrounds: full-width zones, 150px height each
- Component boxes: 160x50, minimum 30px gap between components
- Vertical arrows between layers show data flow
- Label connections with method (REST, WebSocket, SQL query, etc.)

---

#### JTBD Four Forces

Layout: two-column layout. Left column = forces that push AWAY from current and pull TOWARD new. Right column = forces that pull TOWARD current (anxiety, habit). Center = the switch decision point.

Structure:
- Top-left quadrant: PUSH forces (why leave current)
- Bottom-left quadrant: PULL forces (why adopt new)
- Top-right quadrant: ANXIETY forces (fear of switching)
- Bottom-right quadrant: HABIT forces (attachment to current)
- Center: large arrow or circle representing the switch moment

Color scheme:
- PUSH (pain): Light Red (`#ffc9c9`), stroke `#ef4444`, arrows pointing right (toward switch)
- PULL (attraction): Light Green (`#b2f2bb`), stroke `#22c55e`, arrows pointing right (toward new)
- ANXIETY (fear): Light Orange (`#ffd8a8`), stroke `#f59e0b`, arrows pointing left (away from switch)
- HABIT (inertia): Light Purple (`#d0bfff`), stroke `#8b5cf6`, arrows pointing left (away from switch)
- Switch center: large arrow or diamond, neutral dark `#1e1e1e`
- Section headers: bold text, matching color

Layout guidance:
- Camera L (800x600)
- Each force as a labeled rectangle with arrow pointing toward or away from center
- 2-4 force items per quadrant
- Current solution label on left, New solution label on right
- Switch arrow in center, pointing right

---

## Step 3: Export (optional)

After rendering the diagram inline, offer export:

```
Diagram complete.

Options:
  A) Export to excalidraw.com → shareable link for editing
  B) Save checkpoint → continue editing in a future session
  C) Done
```

If user selects A: call `mcp__claude_ai_Excalidraw__export_to_excalidraw` with the diagram JSON and return the shareable URL.

If user selects B: note the checkpoint ID returned by `create_view` and inform the user it can be restored with `/pm-diagrams` in a future session.

---

## Internal completeness checklist

<!-- Claude reference only -->

**Before generating:**
- [ ] Diagram type selected and input gathered
- [ ] Correct camera size for diagram complexity
- [ ] Color scheme matches the type conventions above
- [ ] Elements ordered correctly for streaming (background → shape → label → arrow)

**After generating:**
- [ ] All elements labeled and readable at display scale (font ≥ 16)
- [ ] Camera covers all content with padding
- [ ] Export option offered to user
