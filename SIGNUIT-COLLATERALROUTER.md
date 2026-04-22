# SignUIT CollateralRouter — Private Collateral Routing for Canton-Native Institutions

> **"Your collateral, always where it needs to be."**
> Set your policies once and automate eligible collateral routing on Canton.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [The Problem](#the-problem)
3. [The Solution](#the-solution)
4. [How It Works](#how-it-works)
5. [User Personas](#user-personas)
6. [User Journeys](#user-journeys)
7. [Dashboard Design](#dashboard-design)
8. [Technical Architecture](#technical-architecture)
9. [Business Model](#business-model)
10. [Market Analysis & Competitive Landscape](#market-analysis)
11. [Go-to-Market Strategy](#go-to-market)
12. [MVP Roadmap (HackCanton)](#mvp-roadmap)
13. [Financial Projections](#financial-projections)
14. [Why Canton Network](#why-canton-network)
15. [Risk Analysis](#risk-analysis)

---

## Executive Summary

**SignUIT CollateralRouter** is a collateral operating system built on Canton Network. It allows institutions to define their collateral policies once — in a simple YAML file or UI — and have their tokenized assets continuously evaluated and routed according to policy, with every decision recorded on an immutable audit trail.

Canton is already hosting institutional activity across tokenized assets such as Treasuries, stablecoins, Gilts, and private credit instruments. Yet the question of *which* collateral goes *where* and *when* is still answered by humans with spreadsheets and manual coordination. SignUIT CollateralRouter fills that gap — a missing layer in the current stack — the engine that helps the assets already on Canton work as efficiently as possible.

**What the evidence supports:**
- In many institutions, collateral decisions still rely on spreadsheets, manual review, and operational coordination (ValueExchange/Canton, Jan 2026)
- Industry research suggests collateral delivery and operational cost remain major pain points — 70% of firms report delivery challenges, and operational costs can represent the majority of total trade cost (ValueExchange/Canton, Jan 2026)
- Large amounts of collateral remain idle outside business hours, representing unrealised yield
- We have not identified a Canton-native collateral routing engine today — a review of 233 Featured App submissions to Canton found no existing application focused on rule-based collateral routing
- SignUIT CollateralRouter occupies a gap in Canton's current application stack

**Tracks:** HackCanton Season #1 — Track 1 (RWA & Business Workflows) + Track 2 (Financial Applications)

---

## The Problem

### 1. Collateral Management is Still Manual

Institutions managing tokenized assets on Canton still rely on significant human coordination to determine which collateral to deploy, when to substitute it, and how to respond to margin or liquidity needs. According to a 2026 ValueExchange industry survey conducted in partnership with Canton Network:

> *"70% of firms report delivery challenges. Operational costs can represent the majority of total trade cost."*
> — ValueExchange / Canton Network, "Treasuries on-chain: An industry case for change", Jan 2026

In many institutions, intraday collateral decisions are still made by treasury operations teams using spreadsheets and manual coordination. A margin call arrives. Someone checks available holdings, selects collateral, contacts a counterparty, and waits for confirmation. The process can take many minutes, depending on complexity.

On Canton, settlement can be designed to be atomic and fast. But the *decision* of what to send remains a human one.

### 2. Multi-Asset Complexity Creates Costly Mistakes

A typical Canton participant today holds multiple collateral types simultaneously:

| Asset | Yield | Haircut | Liquidity |
|---|---|---|---|
| USDC | 0% | 0% | Instant |
| USYC | ~4.5% APY | 2% | Instant |
| US Treasury Token | ~4.2% APY | 5% | Fast |
| UK Gilt Token | ~4.0% APY | 8% | Fast |

The optimal decision — "cheapest-to-deliver" — requires knowing current yields, haircuts, counterparty requirements, and maturity profiles simultaneously. Without automation, firms tend to default to the most familiar choice, not the most efficient one.

The opportunity cost can compound meaningfully across many routing decisions.

### 3. The Cheapest-to-Deliver Problem Has No Canton-Native Solution

In traditional markets, cheapest-to-deliver (CTD) optimization is a known and well-understood concept — but it requires expensive, proprietary systems (Broadridge Collateral Management, Murex, Calypso). These systems cost hundreds of thousands to millions per year in licensing and are accessible primarily to the largest institutions.

On Canton, we have not identified a Canton-native equivalent today. The network provides the privacy and settlement features needed for this use case. The missing piece is the decision layer — the component that selects eligible collateral according to policy.

**Source:** Broadridge Collateral Management product page; ValueExchange/Canton Network, Jan 2026.

### 4. Idle Collateral Over Weekends and After Hours

Canton operates 24/7. Yet collateral decisions are still made primarily during business hours. On a typical Friday evening:

- Significant collateral holdings sit unremunerated overnight
- In many cases, positions are not continuously re-optimized
- Positions set in the morning run through the weekend without re-evaluation

> *"6:45 pm on a Friday, the financial world effectively goes into hibernation."*
> — Barnaby Nelson, Canton Network Blog, February 2026

Industry research (ValueExchange/Canton, Jan 2026) suggests even small yield improvements on idle collateral can create meaningful annual savings — and that the majority of survey respondents expect significant improvement in collateral mobility from on-chain infrastructure.

---

## The Solution

**SignUIT CollateralRouter** is a collateral operating system that runs natively on Canton. Institutions define their collateral policies once; the system evaluates them continuously, 24/7, across all tokenized assets.

**Day 1 approach:** CollateralRouter acts as a policy suggestion engine with human approval required before execution. Institutions see the recommended routing decision and can approve, modify, or reject it. This allows institutions to validate the system's recommendations before opting into fully automated execution — building trust before reducing human involvement.

### Core Concept

```
Traditional Collateral Management:    SignUIT CollateralRouter:

Margin call received              →   Smart contract trigger fires
Treasury team opens Excel         →   Rule engine evaluates policy
Manual asset selection            →   Cheapest-to-deliver computed
Phone call to counterparty        →   Suggestion presented with CTD rationale
SWIFT confirmation sent           →   Human approves or adjusts
T+1 or T+2 settlement             →   Settlement triggered after approval
Available: Mon–Fri 9am–5pm        →   Available: 24/7/365
       →   Phase 2: fully automated execution (opt-in)
```

### Three Rule Types (MVP)

**Rule 1 — Cheapest-to-Deliver (CTD)**
Automatically selects the collateral with the lowest opportunity cost that satisfies counterparty requirements.

```yaml
rule: cheapest_to_deliver
priority:
  - USYC    # lowest yield loss (already yield-bearing)
  - UST     # low haircut, high acceptance
  - GILT    # moderate haircut
  - USDC    # last resort (no yield)
min_ltv: 95
```

**Rule 2 — Expiry-First**
Prioritizes collateral nearing maturity to avoid operational risk from expired positions.

```yaml
rule: expiry_first
horizon_days: 7      # route collateral expiring within 7 days first
fallback: cheapest_to_deliver
```

**Rule 3 — Yield Maximizer**
Keeps highest-yielding assets deployed in yield-generating positions as long as possible; substitutes with lower-yield collateral when a call comes in.

```yaml
rule: yield_maximizer
protect:
  - USYC    # never send unless all others exhausted
  - UST     # protect Treasury positions
deploy_first:
  - USDC
  - CBTC
```

### Key Features

| Feature | Traditional Systems | SignUIT CollateralRouter |
|---|---|---|
| Setup | Months of integration | YAML file + Canton wallet |
| Cost | $500K–$5M/year licensing | Usage-based per routed transaction |
| Availability | Business hours | Designed for 24/7 execution |
| Decision speed | Manual, can take many minutes | Suggestion in seconds; execution on approval |
| Cheapest-to-deliver | Manual approximation | Algorithmic, policy-driven |
| Privacy | Counterparty sees all | Canton sub-transaction privacy |
| Multi-asset | Requires separate modules | Native: USDC, USYC, UST, Gilt |
| Weekend operation | No | Yes — triggers active 24/7 |

---

## How It Works

### Architecture: On-chain vs. Off-chain

SignUIT CollateralRouter separates concerns across on-chain and off-chain layers:

- **CTD calculation (off-chain):** Cheapest-to-deliver computation is fast and runs off-ledger, with results submitted to Canton for execution
- **Policy storage (on-chain):** Policy rules are stored on Canton for immutability, auditability, and multi-party visibility
- **Settlement execution (on-chain):** Actual asset routing uses Daml Finance atomic DvP for settlement finality and privacy

This separation allows the system to be fast without compromising on auditability.

### Rule Engine Architecture

```
┌──────────────────────────────────────────────────────┐
│               SignUIT CollateralRouter                │
│                                                      │
│  ┌────────────────┐    ┌───────────────────────────┐ │
│  │  Policy Store  │    │     Trigger Engine        │ │
│  │                │    │                           │ │
│  │  Rules (YAML)  │───▶│  On: margin call          │ │
│  │  Priority list │    │  On: position maturity    │ │
│  │  LTV floors    │    │  On: new opportunity      │ │
│  │  Haircut limits│    │  On: schedule (cron)      │ │
│  └────────────────┘    └──────────┬────────────────┘ │
│                                   │                  │
│                                   ▼                  │
│                   ┌───────────────────────────────┐  │
│                   │     Collateral Selector       │  │
│                   │                               │  │
│                   │  1. Query available holdings  │  │
│                   │  2. Apply CTD algorithm     │  │
│                   │  3. Verify LTV + haircut    │  │
│                   │  4. Select optimal asset    │  │
│                   └──────────────┬────────────────┘  │
│                                  │                   │
│                                  ▼                   │
│                   ┌───────────────────────────────┐  │
│                   │   Canton Settlement Engine    │  │
│                   │                               │  │
│                   │  Daml Finance atomic DvP      │  │
│                   │  Sub-transaction privacy      │  │
│                   │  Fast settlement (happy path) │  │
│                   │  Immutable audit trail        │  │
│                   └───────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```
┌──────────────────────────────────────────────────────┐
│               SignUIT CollateralRouter                │
│                                                      │
│  ┌────────────────┐    ┌───────────────────────────┐ │
│  │  Policy Store  │    │     Trigger Engine        │ │
│  │                │    │                           │ │
│  │  Rules (YAML)  │───▶│  On: margin call          │ │
│  │  Priority list │    │  On: position maturity    │ │
│  │  LTV floors    │    │  On: new opportunity      │ │
│  │  Haircut limits│    │  On: schedule (cron)      │ │
│  └────────────────┘    └──────────┬────────────────┘ │
│                                   │                  │
│                                   ▼                  │
│                   ┌───────────────────────────────┐  │
│                   │     Collateral Selector       │  │
│                   │                               │  │
│                   │  1. Query available holdings  │  │
│                   │  2. Apply CTD algorithm       │  │
│                   │  3. Verify LTV + haircut      │  │
│                   │  4. Select optimal asset      │  │
│                   └──────────────┬────────────────┘  │
│                                  │                   │
│                                  ▼                   │
│                   ┌───────────────────────────────┐  │
│                   │   Canton Settlement Engine    │  │
│                   │                               │  │
│                   │  Daml Finance atomic DvP      │  │
│                   │  Sub-transaction privacy      │  │
│                   │  Fast settlement (happy path) │  │
│                   │  Immutable audit trail        │  │
│                   └───────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

### Cheapest-to-Deliver Algorithm

CTD calculation runs off-chain for speed. Results are submitted to Canton for execution.

```
INPUT: Required amount R, counterparty requirements C

FOR each asset A in priority_list:
  opportunity_cost(A) = yield(A) × duration × R / LTV(A)
  IF haircut(A) satisfies C AND available(A) >= R / LTV(A):
    SELECT A
    BREAK

IF no asset found:
  ALERT: insufficient collateral
  RETURN error

OUTPUT: selected_asset, amount_to_send, estimated_savings_vs_USDC
```

**Example — $10M overnight margin call:**

| Option | Asset Sent | Opportunity Cost | vs. USDC |
|---|---|---|---|
| Naive (USDC first) | $10.5M USDC | $0/night | baseline |
| CTD (USYC first) | $10.7M USYC | $0/night* | $1,233 saved |
| CTD (UST first) | $10.5M UST | $1,151/night | $82 saved |

*USYC continues accruing yield even while pledged in some structures.

### Transaction Lifecycle

```
ROUTING FLOW:
┌──────────────────────────────────────────────────────┐
│ 1. Trigger fires (margin call / schedule / manual)   │
│ 2. Rule engine reads current policy                  │
│ 3. Holdings queried from Canton ledger               │
│ 4. CTD algorithm selects optimal collateral          │
│ 5. Allocation contract created on Canton             │
│    - Collateral locked in escrow                     │
│    - Routing record minted (#RouteID)                │
│    - Destination notified (atomic)                   │
│ 6. Settlement confirmed: fast in happy path          │
│ 7. AllocationRecord updated with outcome             │
│ 8. Savings report: estimated CTD benefit logged      │
└──────────────────────────────────────────────────────┘

SUBSTITUTION FLOW (when better collateral becomes available):
┌──────────────────────────────────────────────────────┐
│ 1. Yield Maximizer rule detects suboptimal position  │
│ 2. New collateral available (e.g. UST just received) │
│ 3. Substitution proposal created                     │
│ 4. Counterparty consent (Canton privacy contract)    │
│ 5. Atomic swap: old collateral out, new collateral in│
│ 6. Both positions updated simultaneously             │
└──────────────────────────────────────────────────────┘
```

---

## User Personas

### Persona 1: Rachel Kim — The Treasury Operations Manager

**Role:** Treasury Operations Manager, Vantage Capital Partners (quantitative hedge fund, $4B AUM)
**Age:** 34 | **Experience:** 9 years collateral management
**Collateral under management:** $800M across USDC, USYC, US Treasuries

**Goals:**
- Respond to margin calls in under 5 minutes instead of 45 minutes
- Never accidentally send USDC when USYC is available — it costs the fund
- Stop managing collateral priorities on a shared Excel spreadsheet
- Have auditability: know exactly what went where and why, for compliance

**Pain Points:**
- Receives 5–10 margin calls per day during volatile markets
- Collateral selection is ad-hoc — whoever picks up the phone decides
- No system enforces cheapest-to-deliver; senior traders often override with gut instinct
- Audit trail for collateral decisions is manual and incomplete
- Weekend calls from risk team: "did we leave anything deployed overnight?"

**How SignUIT CollateralRouter Solves It:**
- Policy configured once in YAML: `priority: [USYC, UST, USDC]`
- Every margin call handled automatically according to policy
- Full audit trail on Canton ledger: routing decisions are recorded immutably for auditability
- Weekend automation: collateral can keep working while the team is offline

**What This Means:**
- Less manual coordination on margin calls — the system evaluates policy and executes
- Consistent cheapest-to-deliver decisions — every time, not just when someone remembers
- Complete audit trail for compliance — every decision logged, timestamped, verifiable
- Reclaiming time spent on manual coordination — enabling the team to focus on higher-value work

**Quote:**
> *"Every margin call is a race against a clock I didn't set. By the time I've checked the spreadsheet and called the desk, the optimal window is gone. I need a system that already knows what to send before I even pick up the phone."*

---

### Persona 2: James Okafor — The Head of Financing

**Role:** Head of Financing, Meridian Asset Management ($22B AUM)
**Age:** 47 | **Experience:** 20 years fixed income and collateral
**Challenge:** Managing collateral across 12 counterparties with different haircut requirements

**Goals:**
- Implement a firm-wide cheapest-to-deliver policy that actually runs
- Stop overpledging: estimates the firm sends 15% more collateral than required
- Deploy idle Treasuries over weekends — currently $1.2B sits unremunerated Friday–Monday
- Replace Broadridge Collateral Management ($1.2M/year license) with something Canton-native

**Pain Points:**
- Each counterparty has different eligible collateral schedules; managing this is a full-time job for 3 people
- Treasuries tokenized on Canton but still routed manually — the on-chain infrastructure is there, the brain is not
- Overpledging buffer adds up: 15% excess across $5B in outstanding positions = $750M locked unnecessarily
- No real-time view of where all collateral is deployed and at what cost

**How SignUIT CollateralRouter Solves It:**
- Per-counterparty rules: different eligibility schedules encoded per destination
- Real-time dashboard: full view of all deployed collateral, cost, and CTD opportunity
- Weekend automation: idle Treasuries can be deployed according to policy, unwound Monday
- Usage-based pricing — potentially cost-effective compared to legacy licensing

**What This Means:**
- Policy automation can materially reduce manual decision-making overhead
- Idle collateral can work during non-business hours — not just sitting idle
- Counterparty-specific rules in code, not institutional memory

**Quote:**
> *"I have three analysts whose entire job is figuring out which collateral goes where every morning. That should be a rule in a config file, not a career."*

---

### Persona 3: Ana Ribeiro — The Regional Bank CFO

**Role:** CFO, Meridio Regional Bank ($9B total assets)
**Age:** 51 | **Location:** Lisbon, Portugal
**Challenge:** Competing with Tier 1 banks on funding costs while managing collateral across time zones

**Goals:**
- Automate collateral substitution when rates change overnight (US vs. EU time zones)
- Reduce daylight overdraft costs: currently paying ~€400K/year in overdraft fees
- Deploy excess Gilt holdings in cross-border repo during UK off-hours
- Get institutional-grade collateral management without institutional-grade pricing

**Pain Points:**
- Time zone problem: best collateral opportunities in US markets happen when Lisbon office is closed
- No automated substitution: positions opened in the morning are never re-optimized during the day
- Gilt tokenization is new — no tooling exists to deploy Gilt tokens effectively on Canton
- Tier 1 collateral management vendors require minimum $500M AUM and 12-month contracts

**How SignUIT CollateralRouter Solves It:**
- 24/7 trigger engine: policies can execute while the team is offline
- Cross-asset rules: Gilt-first when acceptable to counterparty, UST as backup
- Automatic substitution: system checks positions for optimization during the day
- Usage-based pricing — affordable for institutions without enterprise-scale budgets

**What This Means:**
- Time zone gaps become automatic — policies run 24/7, not just during local business hours
- Cross-border opportunities accessible without manual intervention
- Competitive with large-bank capabilities without large-bank pricing

**Quote:**
> *"Larger institutions often have more sophisticated collateral tooling than smaller firms. We have someone checking a spreadsheet at 9 AM. SignUIT is the first time that gap feels closeable."*

---

## User Journeys

### Journey 1: Margin Call Under 5 Minutes (Rachel)

**Scenario:** Tuesday, 3:47 PM. Volatile session. Risk desk sends a $15M margin call due by 4:00 PM.

```
STEP 1 — Trigger Fires (3:47:03 PM)
  Canton smart contract receives margin call event
  CollateralRouter trigger activates
  Rule engine reads Rachel's policy:
    priority: [USYC, UST, USDC]
    min_ltv: 95
    max_haircut: 8%

STEP 2 — CTD Calculation (3:47:04 PM — 1 second)
  Available holdings:
    USYC:  $8.2M  (yield: 4.5%, haircut: 2%)  → covers $8.04M net
    UST:   $12.0M (yield: 4.2%, haircut: 5%)  → covers $11.4M net
    USDC:  $25.0M (yield: 0%,   haircut: 0%)  → covers $25.0M net

  CTD result:
    USYC: $8.2M  → covers $8.04M  (not enough alone)
    UST:  $7.3M  → covers $6.96M  (fills remainder)
    Total: $15.0M covered ✓

  Opportunity cost saved vs. all-USDC: $1,849/night

STEP 3 — Suggestion Presented (3:47:04 PM)
  Rachel receives notification:
    "Margin call #MC-4821 — Suggested routing: $8.2M USYC + $7.3M UST
     Estimated savings: $1,849/night vs. USDC baseline
     [Approve] [Adjust] [Reject]"
  Rachel taps Approve (3:47:05 PM)

STEP 4 — Settlement (3:47:05–3:47:09 PM — seconds)
  Canton atomic swap executes:
    $8.2M USYC → locked in escrow → counterparty notified
    $7.3M UST  → locked in escrow → counterparty notified
    RouteRecord #88341 minted → audit trail created

STEP 4 — Confirmation (3:47:09 PM)
  Rachel's dashboard shows:
    ✓ Margin call #MC-4821 — SATISFIED
    Collateral sent:    $8.2M USYC + $7.3M UST
    Settlement time:    seconds (happy path)
    CTD savings:        estimated vs. USDC-first approach
    Next maturity:      Tomorrow 9:00 AM (auto-roll option available)

STEP 5 — Rachel's Experience
  3:47 PM — Margin call received
  3:47 PM — Notification: routing suggestion with CTD rationale
  3:47 PM — Rachel taps Approve on her phone
  3:47 PM — "Margin call satisfied."
  3:48 PM — Rachel is still on her other call.
  Total human time required: ~10 seconds.

COMPARISON:
  Old process (manual):    tens of minutes, inconsistent outcome
  CollateralRouter:        seconds to suggest, human approval required Day 1
  Time saved this call:    meaningful reduction
  Operational benefit:   consistency, auditability, CTD rationale visible
```

---

### Journey 2: Weekend Yield Automation (James)

**Scenario:** Friday, 6:30 PM. James's team has just left. $1.2B in US Treasury tokens are sitting idle on Canton.

```
STEP 1 — Friday Evening Trigger (6:45 PM)
  Yield Maximizer rule fires on schedule:
    trigger: friday_close
    time: 18:45
    action: deploy_idle_to_repo

  System scans all undeployed holdings:
    Idle UST: $1,200,000,000
    Current repo availability: $800M capacity (pool has room)

STEP 2 — Phased Deployment (6:45 PM)
  System scans all undeployed holdings:
    Idle UST: $1,200,000,000
    Current repo availability: $800M capacity (pool has room)

  Route 1: $400M UST → Pool A (4.1% APY, 72h term)
    Settlement: seconds
    Route #88400 minted
  Route 2: $300M UST → Pool B (3.9% APY, 48h term)
    Settlement: seconds
    Route #88401 minted
  Route 3: $200M UST → Pool C (4.0% APY, 72h term)
    Settlement: seconds
    Route #88402 minted
  Remaining $300M: no capacity → held idle, alert queued for Monday

STEP 3 — Weekend Monitoring (Continuous)
  Saturday 9:00 AM:  All positions healthy. Pool utilization: 71%.
  Saturday 2:00 PM:  Pool A utilization rises to 89%. Rate ticks up to 4.3%.
                     System notes: rate improvement, no action needed.
  Sunday 11:00 PM:   Pool B (48h term) approaching maturity.
                     Auto-roll rule activates:
                     $300M rolls into new 48h position at 4.0% APY ✓

STEP 4 — Monday Morning (8:00 AM)
  James opens dashboard:
    ┌─────────────────────────────────────────────┐
    │  WEEKEND SUMMARY                            │
    │  Deployed:     $900M UST (3 routes)         │
    │  Duration:     62 hours                     │
    │  Gross yield:  meaningful (see report)      │
    │  Router fee:   usage-based                  │
    │  Net earnings: yield earned on idle assets    │
    │                                             │
    │  Status:       All positions healthy         │
    └─────────────────────────────────────────────┘

STEP 5 — Unwind (8:02 AM)
  James clicks "Unwind for settlements"
  CollateralRouter executes:
    All 3 positions closed atomically
    $900M UST + yield → back to James's wallet
    Ready for Monday settlement obligations by 8:05 AM

OUTCOME: Yield earned on assets that previously earned nothing.
James's total effort: 0 minutes Friday, 2 minutes Monday.
```

---

### Journey 3: Cross-Border Substitution (Ana)

**Scenario:** Wednesday, 9:15 AM Lisbon time. Ana's bank has UK Gilt tokens and a Portuguese Treasury bond obligation due at noon.

```
PRE-CONDITIONS:
  Ana's policy:
    counterparty_EU: [GILT preferred, UST acceptable, USDC fallback]
    counterparty_US: [UST preferred, USYC acceptable]
    substitute_threshold: 0.5%  (if savings > 0.5%, auto-substitute)

STEP 1 — Morning Position Review (9:00 AM auto-trigger)
  System scans all active positions:
    Position #7721: €50M USDC pledged to EU counterparty (since Monday)
    Available: £80M GILT tokens (idle since tokenization Tuesday)
    CTD check: GILT has 4.0% yield vs. USDC at 0%
    Savings if substituted: €5,479/day (> 0.5% threshold)

STEP 2 — Substitution Proposal (9:00:05 AM)
  CollateralRouter creates substitution proposal:
    Offer: £52M GILT (equivalent to €50M at current FX)
    For: €50M USDC (return to Ana)
    Savings: €5,479/day

  EU counterparty's system receives proposal:
    Canton privacy contract: counterparty sees only their leg
    Auto-accept rule fires (GILT is on their eligible schedule)
    Acceptance: 9:00:08 AM

STEP 3 — Atomic Substitution (9:00:09 AM)
  Canton atomic swap:
    £52M GILT → counterparty escrow
    €50M USDC → returned to Ana's wallet
  Both legs execute simultaneously. No settlement risk.
  Route #88412 minted. Audit trail complete.

STEP 4 — Noon Obligation (12:00 PM)
  Portuguese Treasury obligation requires €50M cash
  Ana's €50M USDC (returned from substitution) is available ✓
  Obligation met without additional borrowing

STEP 5 — End of Day Summary
  Ana's CFO dashboard:
    Substitution #88412:  completed
    Gilt now deployed:    £52M earning yield
    USDC freed:           €50M available for PT obligation
    Next substitution:    System will check again at 9:00 AM Thursday

ANNUAL IMPACT:
  The savings compound meaningfully across daily CTD decisions,
  weekend deployments, and reduced operational overhead.
  This is measurable in practice, not just in model.
```

---

## Dashboard Design

### Rule Configuration Dashboard

```
┌────────────────────────────────────────────────────────────────┐
│  SignUIT CollateralRouter          [Ana.eth]    [Disconnect]   │
├────────────────────────────────────────────────────────────────┤
│  MY POLICIES                                    [+ New Policy] │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Policy Name        Rule Type         Status    Actions   │  │
│  │ EU Counterparties  Cheapest-to-Deliv ● Active  [Edit][▼] │  │
│  │ US Counterparties  Yield Maximizer   ● Active  [Edit][▼] │  │
│  │ Weekend Automation Expiry-First      ● Active  [Edit][▼] │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  EDIT POLICY: EU Counterparties                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Rule Type:  [Cheapest-to-Deliver       ▼]               │  │
│  │                                                          │  │
│  │  Priority Order (drag to reorder):                       │  │
│  │    1. ☰ UK Gilt Token (GILT)    yield: 4.0%  haircut: 8% │  │
│  │    2. ☰ US Treasury (UST)       yield: 4.2%  haircut: 5% │  │
│  │    3. ☰ USYC                    yield: 4.5%  haircut: 2% │  │
│  │    4. ☰ USDC                    yield: 0.0%  haircut: 0% │  │
│  │                                                          │  │
│  │  Constraints:                                            │  │
│  │    Min LTV:         [95    ]%                            │  │
│  │    Max Haircut:     [10    ]%                            │  │
│  │    Auto-substitute: [✓] if savings > [0.5]%/day          │  │
│  │                                                          │  │
│  │  [Save Policy]  [Test with $10M scenario]                │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

### Live Routing Dashboard

```
┌────────────────────────────────────────────────────────────────┐
│  SignUIT CollateralRouter                    Live  ● 14:23 UTC │
├────────────────────────────────────────────────────────────────┤
│  PORTFOLIO OVERVIEW                                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐           │
│  │ Total Mgd   │  │ Today Saved │  │  Routes Run │           │
│  │  $2.1B      │  │  +$48,230   │  │     127     │           │
│  └─────────────┘  └─────────────┘  └─────────────┘           │
│                                                                 │
│  DEPLOYED COLLATERAL                                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ #Route  Asset    Amount     Destination  Rate  Mat   Act  │  │
│  │ #88341  USYC     $8.2M      Pool Alpha   4.5%  T+1  [▼]  │  │
│  │ #88341  UST      $7.3M      Pool Alpha   4.2%  T+1  [▼]  │  │
│  │ #88400  UST      $400M      Pool Bravo   4.1%  T+3  [▼]  │  │
│  │ #88412  GILT     £52M       EU-CParty    4.0%  T+7  [▼]  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  COLLATERAL EFFICIENCY                                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  CTD Score: 94/100   ████████████████████░░  Excellent   │  │
│  │  Idle assets: $42M USDC (no matching rule yet)           │  │
│  │  Suggestion: Create rule for USDC → Pool Gamma (3.8%)    │  │
│  │                              [Apply Suggestion ▶]        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  RECENT ROUTING ACTIVITY                              [Export] │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  14:22:07  Route #88520  $15M margin → USYC+UST  ✓ 6s   │  │
│  │  13:45:31  Substitution  €50M USDC → GILT        ✓ 4s   │  │
│  │  09:00:05  Weekend unwind $900M UST ← 3 pools    ✓ 12s  │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

### Collateral Efficiency Report

```
┌────────────────────────────────────────────────────────────────┐
│  Efficiency Report — April 2026                [Download PDF]  │
├────────────────────────────────────────────────────────────────┤
│  CTD SAVINGS BREAKDOWN                                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  If all collateral sent as USDC:         $0/month        │  │
│  │  Actual cost with CollateralRouter:      -               │  │
│  │  ─────────────────────────────────────────────────────   │  │
│  │  USYC substitutions (142 events):        +$187,420       │  │
│  │  UST substitutions (89 events):          +$94,310        │  │
│  │  Gilt substitutions (31 events):         +$41,200        │  │
│  │  Weekend deployments (4 weekends):       +$262,857       │  │
│  │  ─────────────────────────────────────────────────────   │  │
│  │  Total April savings:                    $585,787        │  │
│  │  Router fees paid (2 bps):               -$4,200         │  │
│  │  NET BENEFIT:                            $581,587        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ROUTING PERFORMANCE                                           │
│  Avg settlement time:    4.2 seconds                          │
│  SLA met (< 30 sec):     100%                                 │
│  Failed routes:          0                                     │
│  Substitutions accepted: 98.7%                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Technical Architecture

### Stack Overview

```
┌──────────────────────────────────────────────────────────────┐
│              SignUIT CollateralRouter Frontend                │
│               React + TypeScript + Tailwind CSS              │
├──────────────────────────────────────────────────────────────┤
│                    Canton Ledger API                         │
│             (gRPC Ledger API + JSON API Gateway)             │
├──────────────────────────┬───────────────────────────────────┤
│   Daml Smart Contracts   │    External Integrations          │
│                          │                                   │
│  - CollateralPolicy.daml │  ┌──────────┐  ┌──────────────┐  │
│  - RoutingRule.daml      │  │Chainlink │  │Circle USDC   │  │
│  - AllocationRecord.daml │  │Oracle    │  │& USYC        │  │
│  - TriggerEngine.daml    │  │(FX + NAV)│  │(cash leg)    │  │
│  - Substitution.daml     │  └──────────┘  └──────────────┘  │
│                          │  ┌──────────┐  ┌──────────────┐  │
│                          │  │DTCC UST  │  │Daml Finance  │  │
│                          │  │Tokens    │  │Settlement    │  │
│                          │  └──────────┘  └──────────────┘  │
├──────────────────────────┴───────────────────────────────────┤
│                      Canton Network                          │
│          (Privacy-preserving distributed ledger)             │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Circle   │  │  DTCC    │  │Chainlink │  │  ACME /  │   │
│  │USDC/USYC │  │UST Tokens│  │ Oracle   │  │  Alpend  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└──────────────────────────────────────────────────────────────┘
```

### Daml Contract Design

**CollateralPolicy.daml** — Institution-level policy configuration
```daml
template CollateralPolicy
  with
    operator     : Party          -- SignUIT protocol
    institution  : Party          -- e.g. Vantage Capital
    policyId     : Text
    rules        : [RoutingRule]  -- ordered list of rules
    active       : Bool
    createdAt    : Time
  where
    signatory operator, institution
    key (operator, institution, policyId) : (Party, Party, Text)
```

**RoutingRule.daml** — Individual routing rule
```daml
data RuleType
  = CheapestToDeliver
  | ExpiryFirst { horizonDays : Int }
  | YieldMaximizer { protectedAssets : [InstrumentKey] }

template RoutingRule
  with
    policy       : ContractId CollateralPolicy
    ruleType     : RuleType
    priorityList : [InstrumentKey]   -- ordered asset priority
    minLtv       : Decimal           -- e.g. 0.95
    maxHaircut   : Decimal           -- e.g. 0.10
    autoSubstitute : Bool
    substituteThreshold : Decimal    -- e.g. 0.005 (0.5%/day)
```

**AllocationRecord.daml** — Immutable routing audit record
```daml
template AllocationRecord
  with
    routeId       : Text
    institution   : Party
    assetSent     : InstrumentKey
    amountSent    : Decimal
    destination   : Party
    ruleApplied   : RuleType
    settlementTime: Time
    ctdSavingsBps : Decimal    -- savings vs. USDC baseline
    status        : RouteStatus  -- Pending | Settled | Substituted | Failed
```

**TriggerEngine.daml** — Automated trigger management
```daml
template TriggerEngine
  with
    operator     : Party
    institution  : Party
    triggers     : [TriggerConfig]

data TriggerConfig = TriggerConfig
  with
    triggerType  : TriggerType
    policyId     : Text
    enabled      : Bool

data TriggerType
  = OnMarginCall  { sourceContract : ContractId }
  | OnSchedule    { cronExpression : Text }
  | OnMaturity    { daysBeforeExpiry : Int }
  | OnOpportunity { minSavingsBps : Decimal }
```

### Canton Privacy Model

Every routing decision in SignUIT CollateralRouter uses Canton's sub-transaction privacy:

- **Counterparty privacy:** Institution A cannot see what collateral Institution B is holding or routing
- **Rule privacy:** Competitors cannot reverse-engineer a firm's CTD policy from observed transactions
- **Position privacy:** Only the institution and the direct counterparty see the details of each allocation
- **Oracle privacy:** Price data consumed privately — no leakage of when a firm checks asset values

This is the core reason CollateralRouter must be built on Canton and not on any public chain. A public chain would leak every routing decision to every competitor in the ecosystem.

---

## Business Model

### Revenue Streams

| Stream | Rate | Who Pays | Notes |
|---|---|---|---|
| Routing Fee | Usage-based per routed transaction | Institution | Per successful routing event |
| Substitution Fee | Lower rate per substitution | Institution | Optimization events |
| Enterprise SaaS | Monthly fee | Large institutions | Custom rules, priority support, white-label |

### Unit Economics Example

**$500M portfolio, 10 routing events/day, 250 days/year:**

```
Routing fees:
  10 events/day × $500M avg × usage-based rate × 250 days
  (exact rate TBD — to be validated through pilot conversations)

Total per $500M institution scales with volume.
```

### Comparison vs. Legacy Solutions

| Solution | Annual Cost | Who Can Afford | Min AUM |
|---|---|---|---|
| Broadridge Collateral Mgmt | $800K–$1.5M | Tier 1 banks | $50B+ |
| Murex / Calypso | $1M–$5M | Bulge bracket | $100B+ |
| Excel + ops team (3 FTE) | $450K (salary) | Anyone | N/A |
| **SignUIT CollateralRouter** | **Usage-based** | **Any Canton participant** | **No minimum** |

---

## Market Analysis

### The Collateral Management Market

- **Global collateral market:** substantial in mobilizable assets
- **Annual spend on collateral management systems:** billions globally (Broadridge, Murex, Calypso, custom)
- **Canton is already hosting significant institutional financial activity**

### Competitive Landscape

| | Broadridge Coll. Mgmt | Murex/Calypso | ACME (Canton) | Alpend (Canton) | **SignUIT CollateralRouter** |
|---|---|---|---|---|---|
| **Platform** | Legacy DLT | On-premise | Canton | Canton | Canton |
| **Rule-based routing** | Yes | Yes | No | No | **Yes** |
| **Cheapest-to-deliver** | Yes | Yes | No | No | **Yes** |
| **24/7 automation** | Partial | No | No | No | **Yes** |
| **Canton-native** | Partial | No | Yes | Yes | **Yes** |
| **Min AUM** | $50B+ | $100B+ | No minimum | No minimum | **No minimum** |
| **Cost** | $800K–$1.5M/yr | $1M–$5M/yr | % of loan | % of loan | **Usage-based** |
| **Setup time** | 6–18 months | 12–24 months | Hours | Hours | **Minutes (YAML)** |

### Why No Existing Canton App Does This

- **ACME:** Overcollateralized lending — decides how much to lend, not which collateral to route
- **Alpend:** Private credit infrastructure — origination and servicing, not collateral optimization
- **Ditto CCvault:** Yield automation — focuses on stablecoin yield strategies, not multi-asset CTD routing
- **Cantex / Canton Exchange:** Spot DEX — trading, not collateral management

**We reviewed 233 Featured App submissions to Canton Network.** None offer rule-based collateral routing with cheapest-to-deliver optimization. SignUIT CollateralRouter fills that gap.

---

## Go-to-Market Strategy

### The First Customer Question

Before scaling, the most important question is: **who is the first buyer?**

Our initial target is not "any institution." It is:

**Treasury operations teams at institutions already on Canton** that:
- Have tokenized collateral (USDC, USYC, tokenized Treasuries)
- Currently manage that collateral with spreadsheets and manual coordination
- Would benefit from consistent, policy-driven routing without replacing their existing systems

**Why this wedge:**
- They already have the assets on Canton — no tokenization lift required
- They're already用手工管理 — pain is known and admitted
- The solution augments (doesn't replace) existing treasury workflows
- Usage-based pricing doesn't require enterprise-scale commitments

### Phase 1 — Anchor & Prove (Months 1–3)

**Target:** 3–5 early adopters already on Canton with tokenized assets

- **Primary targets:** Institutions using Broadridge DLR or other Canton-based lending facilities
- **Offer:** Pilot integration, then usage-based pricing
- **Entry point:** "You have the assets on Canton. Let them work more efficiently."
- **KPIs:** Pilot institutions signed, routing volume demonstrated, savings measurable

### Phase 2 — Expand & Automate (Months 4–12)

**Target:** 20–50 institutions

- **Add rule types:** Cross-currency routing, advanced policies
- **Add integrations:** Additional tokenized assets as they come on-chain
- **Enterprise tier:** Custom rule engine, dedicated support, SLA guarantees
- **KPIs:** Institutions, routing volume, measured savings

---

## MVP Roadmap (HackCanton)

### 4-Week Build Plan

**Week 1: Core Daml Contracts**
- [ ] `CollateralPolicy.daml` — policy and rule storage
- [ ] `RoutingRule.daml` — CTD + Expiry-First rule types
- [ ] `AllocationRecord.daml` — immutable routing audit log
- [ ] Deploy to Canton testnet
- [ ] Unit tests: CTD selection, rule priority, LTV validation

**Week 2: Trigger Engine + API**
- [ ] `TriggerEngine.daml` — OnMarginCall + OnSchedule triggers
- [ ] `Substitution.daml` — atomic collateral substitution workflow
- [ ] Canton Ledger API integration (Scala/TypeScript)
- [ ] Mock oracle: static prices for USDC, USYC, UST (Chainlink stub)
- [ ] CTD calculation service (off-chain, fast)

**Week 3: Frontend (MVP UI)**
- [ ] Rule configuration UI: drag-and-drop priority list
- [ ] Live routing dashboard: active positions, recent routes
- [ ] Efficiency report: CTD savings vs. USDC baseline
- [ ] Demo accounts: 3 pre-loaded institutions with different portfolios
- [ ] Canton wallet connect

**Week 4: Demo Polish + Pitch**
- [ ] Demo scenario A: Rachel — live margin call routed in 6 seconds
- [ ] Demo scenario B: James — $100M weekend deployment automation
- [ ] Analytics panel: savings summary, routing history
- [ ] Pitch deck aligned with working demo
- [ ] Testnet demo video (backup if live demo fails)

### MVP Scope (In)

- Two rule types: Cheapest-to-Deliver and Expiry-First
- Three assets: USDC, USYC, US Treasury token (mock)
- Manual trigger + schedule trigger (OnSchedule)
- Basic substitution workflow (one counterparty)
- Canton testnet deployment
- Three demo accounts (hedge fund, asset manager, regional bank)
- Routing audit log with CTD savings calculation

### MVP Scope (Out — Post-Hackathon)

- Yield Maximizer rule type
- Cross-currency routing (Gilt ↔ UST FX conversion)
- Live Chainlink oracle integration
- Enterprise SaaS tier and white-label
- DAO governance module
- Mobile app

### Demo Script (5 Minutes)

```
Min 0–1: PROBLEM
  "In many institutions, collateral is still managed manually.
  The assets are already on Canton. The problem is:
  no system decides which asset goes where — consistently."

Min 1–2: SOLUTION
  Show SignUIT CollateralRouter rule config screen
  "You define your policy once. Priority order. LTV floors.
  Set it once, then update as conditions change."

Min 2–4: LIVE DEMO
  --- Rachel scenario (90 seconds) ---
  $15M margin call fires → trigger activates
  CTD algorithm: USYC + UST selected per policy
  Canton settlement: seconds in happy path
  Dashboard: "Margin call satisfied."

  --- James scenario (90 seconds) ---
  Friday 6:45 PM — schedule trigger fires
  $100M UST deployed to yield pools per policy
  Monday dashboard: "Weekend yield earned on previously idle assets."

Min 4–5: MARKET + ASK
  "Institutions on Canton have tokenized assets.
  They need a private decision layer for collateral.
  SignUIT CollateralRouter: usage-based, Canton-native, policy-driven.
  HackCanton Track 1 + Track 2."
```

---

## Success Metrics

### North Star Metric

The most important metric for SignUIT CollateralRouter is:

> **$ value of collateral optimization savings realized per institution per month**

This measures the actual value delivered to customers — not projected revenue, not token incentives, but real savings from better collateral decisions.

### Secondary Metrics

| Metric | Description | Why It Matters |
|---|---|---|
| **Routing decision time** | Time from trigger to routing execution | Demonstrates automation value |
| **% of events automatically routed** | Share of events handled without human intervention | Shows operational efficiency |
| **Failed substitution rate** | Share of substitution attempts rejected | Indicates policy quality and counterparty acceptance |
| **Savings vs baseline** | CTD improvement vs. naive collateral selection | Proves algorithmic value |
| **Uptime of automated rule execution** | Reliability of 24/7 automation | Critical for weekend/after-hours value |

### Measurement Approach

These metrics will be measured on a per-institution basis during the pilot phase:

1. **Pilot (3 institutions, Month 1–3):** Measure baseline, then measure with SignUIT
2. **Validation:** Does the savings number go up? That's the north star.
3. **Scaling decision:** Evidence-backed validation precedes any revenue projection

---

## Why Canton Network

SignUIT CollateralRouter is built for Canton — not as marketing, but as a technical requirement.

### 1. Privacy is Non-Negotiable

Collateral routing decisions are among the most competitively sensitive operations in finance. If one participant can observe another's routing, they can infer that participant's position and strategy. On any public blockchain, every routing decision would be visible to every participant.

Canton's sub-transaction privacy ensures:
- Counterparties see only their own leg of a transaction
- Competitors cannot observe routing patterns, asset holdings, or CTD decisions
- Rule configurations remain confidential

### 2. Atomic Settlement Eliminates Routing Risk

Collateral substitution requires two legs to execute simultaneously: old collateral out, new collateral in. If either leg fails, the institution is exposed. On traditional systems, this settlement risk is managed through costly legal agreements and operational buffers.

Daml Finance's atomic delivery-vs-payment (DvP) settlement means:
- Both legs of a substitution execute atomically — no partial settlement risk
- Either both succeed or both roll back — no stuck positions
- Settlement can be fast in the happy path, not T+1

### 3. The Assets Are Already Here

SignUIT CollateralRouter does not need to build a new asset ecosystem. The collateral is already on Canton:

- **USDC / USYC:** Circle, native Canton integration, live today
- **US Treasury Tokens:** DTCC + Digital Asset, in progress
- **UK Gilt Tokens:** First trades executed on Canton (Feb 2026)
- **Eurobonds:** BNP Paribas Neobonds, live today

CollateralRouter is the orchestration layer for assets that already exist. The infrastructure is built. The router is the missing piece.

### 4. Daml Finance Settlement Library

Building production-grade atomic settlement from scratch on any other platform would require extensive security audits and custom development. Daml Finance provides:

- Pre-audited `Instrument`, `Holdings`, and `Lifecycle` templates
- `Settlement` workflow with atomic multi-leg execution
- Formal verification of contract correctness
- Digital Asset engineering support for integration

### 5. Institutional Participants Are Already on Canton

Several large institutions are active in Canton's ecosystem, making it a plausible distribution path. The business development conversation is not "come to our network" — it is "use your existing assets more intelligently."

---

## Risk Analysis

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Trigger latency under load | Medium | Medium | Off-chain CTD computation; only settlement on-chain. Target < 5s. |
| Oracle manipulation (price feed) | Low | High | Chainlink TWAP feeds; circuit breaker if price moves > 5% in 60 seconds |
| Canton network downtime | Very Low | High | Multi-node setup; graceful degradation to manual mode with alerts |
| Daml contract bug (wrong asset routed) | Low | High | Formal verification; sandbox testing; dry-run mode before live routing |
| Substitution rejected by counterparty | Medium | Low | Fallback rule always defined; rejected substitutions log to dashboard |

### Market Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Slow institutional adoption | Medium | High | Start with 3 anchor clients pre-launch; demonstrate $1M+ savings in Month 1 |
| Tokenized collateral supply thin | Medium | Medium | DTCC UST live H1 2026; USYC already liquid; start with USDC/USYC/UST only |
| Broadridge builds routing natively | Low | Medium | Broadridge is bilateral matching; architectural difference. Not same product. |
| Interest rates fall to zero | Low | Low | CTD optimization still valuable at any rate; operational savings unchanged |

### Regulatory Considerations

SignUIT CollateralRouter occupies the lowest-risk regulatory position of any financial application:

- **Not a broker-dealer:** The protocol does not take custody of assets, does not act as principal, and does not make discretionary investment decisions. It executes instructions defined by the institution itself.
- **Not a fund:** No pooling of assets. Each institution's collateral is always under the institution's own control.
- **Not an exchange:** No price discovery, no order matching, no public market. All routing is bilateral, rule-based, and institution-controlled.
- **Comparable to:** A Bloomberg EMSX routing rule, a Calypso collateral policy engine, or a Murex CTD optimizer — all of which operate without broker-dealer licensing.

**Recommended legal structure:** Protocol deployed as open-source software (MIT license); commercial entity structured as a Swiss GmbH or Cayman Foundation for token rewards. Legal opinion from Clifford Chance (existing Canton ecosystem partner) recommended pre-launch.

**Regulatory monitoring:** CFTC and SEC guidance on tokenized collateral management tools is evolving. Current guidance does not classify rule-based routing software as a regulated activity. Monitor quarterly.

---

## Summary

**SignUIT CollateralRouter** is a private collateral decision layer for Canton-native institutions. It helps them choose and route eligible collateral according to policy, with privacy and auditability built in.

**The core problem:** Canton has tokenized assets and private settlement rails, but no decision engine that optimizes which collateral to route.

**The solution:** A rule-based collateral orchestration engine where institutions define policies once, and SignUIT executes them continuously.

**Why now:** As more tokenized assets move onto Canton, the need for a private decision layer becomes more urgent. The infrastructure for settlement is emerging; the missing piece is the routing decision layer.

**The question we will validate:**
> What evidence do we have that a real institution would let SignUIT make the routing decision instead of doing it in-house or inside an existing treasury system?

This is the most important question — not the business model, not the revenue projection, but the validation that institutions will actually use automated routing.

**Set your policies. Execute continuously. Measure the savings.**

---

*Document version: 1.2 — Revised per second mentor feedback, HackCanton Season #1*
*Last updated: April 2026*
*Repository: canton-research/SIGNUIT-COLLATERALROUTER.md*

---

## Appendix A — Supporting Evidence

### Source Citations

| Claim | Source | Link | Note |
|---|---|---|---|
| 70% of firms report delivery challenges | ValueExchange / Canton Network, Jan 2026 | ¹ | Industry survey |
| Operational costs can be majority of trade cost | ValueExchange / Canton Network, Jan 2026 | ¹ | Industry survey |
| Weekend hibernation quote | Barnaby Nelson, Canton Network Blog, Feb 2026 | ¹ | Public statement |
| Intraday repo scaling case study | Broadridge / SocGen | ² | Whitepaper |
| Canton tokenomics and app rewards | Canton Network, Mar 2026 | ³ | Network documentation |
| Canton privacy and settlement docs | Canton's technical docs | ⁵ | Network reference |

### Detailed Market Figures

The market sizing and cost figures cited in this document are supported by industry research but should be treated as directional, not precise. The ValueExchange report ("Treasuries on-chain: An industry case for change," Jan 2026) provides the most comprehensive publicly available evidence on collateral management pain points and tokenization opportunity.

### Partner Integration Status

Partnerships with Circle, DTCC, Euroclear, Chainlink, and others represent target outreach — not confirmed partnerships. Status is listed as "target" or as publicly announced by the partner.

---

## References

¹ Canton Network Blog, "The Weekend Revolution: Collateral is Finally Working Overtime" (February 2026)
  https://www.canton.network/blog/the-weekend-revolution-collateral-is-finally-working-overtime
  • "58% of market participants are currently struggling with collateral management and margining issues"
  • "Tokenizing collateral is expected to increase interest earnings by $346M a year for Tier 1 firms"
  • "Enabling 24/7 collateral mobility... adding 120 hours of financing activity to the week"

² Broadridge, "Return on Innovation: Intraday Repo Has Arrived on Scale" (Whitepaper)
  https://www.broadridge.com/white-paper/capital-markets/return-on-innovation-intraday-repo-has-arrived-on-scale
  • "At many firms, intraday funding is still managed on Excel spreadsheets — a manual and inefficient process"
  • "Some firms spend a million or more dollars per year on daylight overdraft alone"
  • Case Study: Societe Generale reduced daylight overdraft to zero "four out of five days" with DLT

³ Canton Network, "Earn with every transaction: Continuous transaction-based revenue for apps and assets on Canton" (March 2026)
  https://www.canton.network/blog/earn-with-every-transaction-continuous-transaction-based-revenue-for-apps-and-assets-on-canton

⁴ ValueExchange / Canton Network, "Treasuries on-chain: An industry case for change" (January 2026)
  https://thevx.io/campaign/treasuries-on-chain-an-industry-case-for-change/
  • Industry survey — 70% of firms report delivery challenges
  • Operational costs represent majority of total trade cost
  • "Liquidity crises are now measured in minutes, not days"

⁵ Canton's privacy and settlement documentation
  https://docs.global.canton.network.sync.global/

---

## Appendix B — Revenue Model (Directional)

### Revenue Model Rationale

SignUIT charges usage-based fees per routed transaction. The exact pricing will be validated during the pilot phase through customer conversations, not assumed in advance.

**Sample pricing scenarios (for discussion, not commitment):**

| Scenario | Assumptions | Estimated Annual Revenue |
|---|---|---|
| Conservative | 10 institutions, $500M avg, 2 bps | $2.5M |
| Medium | 50 institutions, $1B avg, 2 bps | $25M |
| Aggressive | 150 institutions, $2B avg, 2 bps | $150M |

These projections are directional — they demonstrate a plausible business model, not a committed forecast. Revenue validation is Phase 1 work, not a pre-launch assumption.

### Canton Coin Rewards (Reference Only)

Canton Network's Activity Marker provides token rewards to Featured Apps. This mechanism exists and could provide supplemental protocol revenue. However:

- **It should not be in the core pitch** — makes the pitch feel token-incentivized rather than customer-driven
- **It is directional** — reward levels depend on network activity and token price, both variable
- **It is post-pilot** — requires Featured App status, which requires an operational app first

*Reference only: This is not a material business driver for the pitch.*
