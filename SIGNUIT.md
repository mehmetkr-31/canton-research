# SignUIT — Automated Market Maker for Repo on Canton Network

> **"Sign. Use. It."** — Instant repo liquidity for everyone, not just Goldman Sachs.

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

**SignUIT** is an Automated Market Maker (AMM) protocol for repurchase agreements (repo) built on Canton Network. It allows any institution — hedge funds, asset managers, small banks — to instantly borrow USDC against tokenized collateral (US Treasuries, Gilts, Bunds), or earn yield by providing liquidity to repo pools.

Today, the repo market is a $6.9T/month market dominated by a handful of institutional platforms with $100M+ minimums. SignUIT opens this market to the buy-side — the firms that need it most but have been systematically excluded.

**Key Numbers:**
- $6.9T/month — Broadridge DLR repo volume (Canton Network)
- $25B/firm — unremunerated collateral sitting idle overnight
- 58% of market participants — struggling with collateral management
- 0 — open-access, permissionless repo platforms on Canton today

**Track:** HackCanton Season #1, Track 2 — Financial Applications

---

## The Problem

### 1. The Repo Market is Closed to 80% of Participants

The repurchase agreement (repo) market is one of the most critical funding mechanisms in global finance. Yet access is severely restricted:

| Platform | Minimum Size | Who Gets Access |
|---|---|---|
| Broadridge DLR | $100M+ per counterparty | Goldman, UBS, SocGen only |
| Tradeweb Repo | Invitation-only | DRW, Virtu, top-tier dealers |
| Fed Repo Facility | Overnight only | Primary dealers |
| **SignUIT** | **$1M+** | **Any institution on Canton** |

**Source:** Broadridge DLR whitepaper (2024), Tradeweb press release (July 2025), Canton Network blog

### 2. $25 Billion Per Firm Sits Unremunerated Every Night

According to the Canton Network blog post "The Weekend Revolution":

> *"At any given time, major financial institutions hold tens of billions in securities that are earning nothing because they can't be efficiently deployed into repo overnight or over weekends."*

- Estimated $25B per Tier 1 firm in unremunerated collateral overnight
- $346M/year in lost earnings per firm (at 4% repo rate)
- 17% of the week is weekend — collateral earns 0% for 17% of the time
- Friday 5pm → Monday 9am: 60 hours of zero yield on idle Treasuries

### 3. Buy-Side Firms Are Frozen Out

The firms that need liquidity most — hedge funds running momentum strategies, asset managers managing redemption risk, small regional banks managing intraday float — have no access to institutional repo rates.

- Hedge funds pay prime brokers 5-6% overnight for cash
- RepoAMM (SignUIT) offers 2.5-3% (institutional rates, democratized)
- Small banks fall back to the Fed discount window at penalty rates
- $268B in tokenized stablecoins remain immobile due to lack of repo infrastructure

### 4. The Operational Problem

Even for firms that have access, repo is operationally painful:

- Bilateral negotiations (call Goldman, agree on rate, confirm via SWIFT)
- T+0 settlement is rare; most repo still settles T+1 or T+2
- No 24/7 access — repos expire Friday, can't be rolled over weekend
- No transparent pricing — rates are negotiated in private

**SignUIT solves all four problems simultaneously.**

---

## The Solution

**SignUIT** is a two-sided liquidity marketplace for repo, implemented as an AMM on Canton Network.

### Core Concept

Like Uniswap for DeFi, but for institutional repo:

```
Traditional Repo:          SignUIT:

Bank A calls Bank B   →    Institution connects wallet
Negotiate rate         →    Rate is set by AMM formula (x*y=k)
Confirm via SWIFT      →    Transaction executes on Canton in seconds
Settle T+1             →    Settlement is instant (atomic swap)
Weekend: market closed →    24/7, 365 days a year
```

### Key Features

| Feature | Traditional Repo | SignUIT |
|---|---|---|
| Access | Relationship-gated | Open to any Canton participant |
| Minimum size | $100M | $1M |
| Rate discovery | Bilateral negotiation | AMM formula (transparent) |
| Settlement | T+1 or T+2 | Instant (atomic) |
| Availability | Mon-Fri 8am-5pm | 24/7/365 |
| Privacy | None (bilateral) | Canton privacy by default |
| Collateral types | Limited | Any tokenized security |

### Supported Collateral (MVP)

- **US Treasury Tokens** (primary pool)
- **UK Gilt Tokens** (secondary pool)
- **USYC** (US Yield Coin — tokenized T-bills by Hashnote, Circle partner)

### Supported Cash Leg

- **USDC** (Circle, native Canton integration)

---

## How It Works

### AMM Formula

SignUIT uses a constant product formula (same as Uniswap v2):

```
x * y = k

Where:
  x = USDC in pool
  y = Collateral tokens in pool
  k = Constant (invariant)
```

The repo rate is derived from the pool ratio:

```
Repo Rate = f(utilization)

utilization = borrowed / totalDeposited
rate = baseRate + (utilization * rateSlope)

Example:
  Base rate: 2.0%
  Pool 70% utilized → rate = 2.0% + (0.70 * 1.5%) = 3.05%
  Pool 90% utilized → rate = 2.0% + (0.90 * 1.5%) = 3.35%
```

Higher demand = higher rate. Rate discovery is fully transparent and algorithmic.

### Transaction Lifecycle

```
BORROW FLOW:
┌──────────────────────────────────────────────────────┐
│ 1. Borrower selects amount + collateral type         │
│ 2. Smart contract quotes rate (based on utilization) │
│ 3. Borrower approves collateral transfer             │
│ 4. Canton atomic swap:                               │
│    - Collateral locked in escrow contract            │
│    - USDC transferred to borrower                    │
│    - Position NFT minted (#PositionID)               │
│ 5. At maturity: Borrower repays USDC + interest      │
│ 6. Canton atomic swap:                               │
│    - USDC (+ interest) transferred to pool           │
│    - Collateral returned to borrower                 │
│    - Position NFT burned                             │
└──────────────────────────────────────────────────────┘

LP FLOW:
┌──────────────────────────────────────────────────────┐
│ 1. LP deposits USDC into pool                        │
│ 2. LP receives LP tokens (proportional share)        │
│ 3. LP tokens accrue interest continuously            │
│ 4. LP can withdraw at any time (liquidity permitting)│
│ 5. On withdrawal: LP tokens burned, USDC + yield out │
└──────────────────────────────────────────────────────┘
```

### Collateral Management

- **LTV (Loan-to-Value):** 95% for US Treasuries, 90% for Gilts
- **Liquidation threshold:** 97% LTV (buffer = 2%)
- **Liquidation trigger:** If collateral value drops below threshold
- **Liquidation mechanic:** Position auto-closes, collateral sold at discount to pool
- **Oracle:** Chainlink price feeds for collateral valuation

---

## User Personas

### Persona 1: Sarah Chen — The LP (Liquidity Provider)

**Role:** Treasury Operations Manager, Goldman Sachs  
**Age:** 38 | **Experience:** 12 years collateral management  
**Portfolio under management:** $50B in US Treasuries

**Goals:**
- Earn yield on Treasuries that sit idle Friday 5pm → Monday 9am
- Reduce the $25B problem — deploy collateral without bilateral negotiations
- Generate income from small tranches ($5-30M) that are too small for DLR

**Pain Points:**
- Broadridge DLR requires $100M+ per counterparty onboarding
- Weekend collateral earns 0% — 17% of the year is wasted
- Small tranche deployment is not worth the operational cost bilaterally
- Can't see real-time utilization or pool health across counterparties

**How SignUIT Solves It:**
- Deploy any amount in 2 clicks — no phone calls, no negotiations
- 24/7 market means weekend yield is finally captured
- Real-time APY and pool utilization visible on dashboard
- LP tokens are liquid — withdraw at any time if cash is needed

**Quote:**
> *"I have $8B sitting doing nothing every Friday afternoon. I've been saying this for years — someone needs to build a repo pool we can just click into."*

---

### Persona 2: Mike Rodriguez — The Borrower

**Role:** CFO, Verition Fund (quantitative hedge fund, $8B AUM)  
**Age:** 42 | **Experience:** 15 years quantitative trading  
**Challenge:** Margin calls, leverage management, intraday liquidity gaps

**Goals:**
- Access instant overnight cash when margin calls hit at 3:45pm
- Avoid revealing trading positions to prime broker (privacy critical)
- Pay institutional rates (2-3%) instead of prime brokerage rates (5-6%)
- Borrow $1M-$50M tickets — too small for DLR, too big for credit card

**Pain Points:**
- Prime broker charges 5.5-6% overnight — 2x what Goldman pays
- Prime broker can see his position when he calls for repo — alpha leakage
- No 24/7 market — margin calls happen after-hours, no solution
- $100M minimum at DLR means he can never access institutional rates

**How SignUIT Solves It:**
- Borrow $1-50M in under 60 seconds, no phone calls
- Canton privacy — Goldman cannot see his positions or borrowing patterns
- Rates at 2.8-3.2% — saving $437 per $5M overnight ticket vs prime broker
- Available at 11pm on a Sunday if needed

**Quote:**
> *"Every time I call my prime broker for $5M overnight, I know they're reading my book. SignUIT is the first repo solution that respects operational privacy."*

---

### Persona 3: David Kim — The Small Bank

**Role:** Head of Treasury, Metro Regional Bank ($5B total assets)  
**Age:** 45 | **Location:** Dallas, Texas  
**Challenge:** Excluded from every institutional repo platform

**Goals:**
- Access repo market as both lender AND borrower based on daily cash needs
- Compete with large bank funding costs
- Diversify away from Federal Home Loan Bank (2-day settlement)
- Generate income from excess Treasury holdings between regulatory reporting dates

**Pain Points:**
- Too small for Broadridge DLR (need $100M+ counterparty)
- Tradeweb Repo invitation-only (invite never came)
- FHLB has T+2 settlement — useless for intraday needs
- Federal discount window carries stigma — stock price impact

**How SignUIT Solves It:**
- Full access: same rates as Goldman, no minimums
- Both borrow and lend based on daily operational needs
- Real-time T+0 settlement on Canton
- No disclosure requirements — Canton privacy preserved

**Annual Value:**
- Earns $400/day lending $10M Treasuries at 4% APY
- Pays $1,600 for occasional $20M 1-day borrow (month-end reporting)
- Net benefit: $140K/year vs current alternatives

---

## User Journeys

### Journey 1: LP Deposits for Weekend Yield (Sarah)

**Scenario:** Friday 4:30 PM. Sarah has $30M in idle US Treasuries.

```
STEP 1 — Connect
  Sarah opens SignUIT dashboard (signuit.app)
  Clicks "Connect Wallet" → Canton wallet authentication
  Dashboard loads with her existing $20M position

STEP 2 — Decide to Deposit
  She sees:
    Current pool APY:        4.5%
    Pool utilization:        72%
    Projected 72h earnings:  $13,700 on $30M
  She clicks "Add Liquidity"

STEP 3 — Select Pool & Amount
  Modal: "Add Liquidity"
  Pool: [US Treasury / USDC ▼]
  Amount: $30,000,000 USDC
  Preview:
    You'll receive:    45,231 LP tokens
    Your pool share:   12.5% (up from 5%)
    Current APY:       4.5%
    Projected 72h:     $13,699

STEP 4 — Approve & Deposit
  Clicks "Approve USDC" → Canton wallet signature
  Clicks "Deposit" → Canton wallet signature
  Transaction confirms in ~5 seconds

STEP 5 — Monitor
  Dashboard now shows:
    Total Deposited:    $50,000,000
    Pool Share:         12.5%
    Current APY:        4.5%
    Accrued Earnings:   $0.00 (just deposited)
    Projected weekend:  $13,699

  --- WEEKEND PASSES ---

STEP 6 — Monday Morning Check (8:00 AM)
  Sarah opens dashboard:
    Weekend Earnings:   $9,123.45
    Pool still healthy: 68% utilized
    Total Value:        $50,009,123

STEP 7 — Partial Withdraw for Settlement
  She needs $30M for Monday settlements
  Clicks "Withdraw" on US-TRSY/USDC row
  Enters: $30,000,000
  Preview:
    You receive:        $30,000,000 USDC
    + earnings:         $5,473.89 (her share of $9,123)
    LP tokens burned:   27,138
  Confirms → Receives $30,005,473 USDC
  Keeps remaining $20M deposited
```

**Outcome:** Sarah earned $5,473 in 60 hours on collateral that previously earned $0.

---

### Journey 2: Emergency Overnight Borrow (Mike)

**Scenario:** 3:45 PM Tuesday. Mike's fund receives a $5M margin call due at 4:00 PM.

```
STEP 1 — Emergency Access
  Mike opens SignUIT mobile app (Face ID login)
  Dashboard immediately shows:
    Available to Borrow:   $45M (pool has capacity)
    Current Rate:          2.8% APY
    Your Collateral:       $12M US-TRSY (available)

STEP 2 — Quick Borrow
  Taps "Borrow Now"
  Enters: $5,000,000 USDC
  Selects collateral: [US Treasury Tokens ▼]

  System quotes:
    Borrow amount:         $5,000,000 USDC
    Collateral required:   $5,263,158 US-TRSY (95% LTV)
    Your available:        $12,000,000 ✓
    Interest rate:         2.8% APY
    Duration:              [Overnight ▼] (rolls until repaid)
    Interest due tonight:  $383.56
    Liquidation price:     collateral < $4,750,000 (never expected)

STEP 3 — Review & Confirm
  Terms displayed:
    Borrow:       $5M USDC
    Collateral:   $5.26M US-TRSY (locked in escrow)
    Rate:         2.8% APY
    Maturity:     Next day, 9:00 AM (auto-roll available)
  
  Taps "Approve Collateral" → Canton wallet signature (5 sec)
  Taps "Borrow Now" → Canton wallet signature (5 sec)

  Canton atomic swap executes:
    $5.26M US-TRSY → locked in SignUIT escrow contract
    $5.00M USDC → transferred to Mike's wallet
    Position NFT #12345 → minted to Mike's address

STEP 4 — Use Funds
  3:52 PM — Mike transfers $5M USDC to exchange
  3:58 PM — Margin call met ✓
  Crisis averted. Total time: 13 minutes.

STEP 5 — Repay Next Morning
  9:30 AM — Trading position closed, cash available
  Opens app, sees:
    Position #12345 active
    Borrowed:       $5,000,000
    Interest due:   $383.56
    Total to repay: $5,000,383.56

  Taps "Repay" → Confirms
  Canton atomic swap executes:
    $5,000,383.56 USDC → returned to pool (interest distributed to LPs)
    $5,263,158 US-TRSY → returned to Mike's wallet
    Position NFT #12345 → burned

COST COMPARISON:
  SignUIT:              $383.56   (2.8% overnight)
  Prime broker:         $823.97   (6.0% overnight)
  Savings this trade:   $440.41
  Annual (50 trades):   $22,020 saved
  Privacy:              Protected ✓ (Canton privacy)
```

---

### Journey 3: Dual-Role Bank (David, Month-End)

**Scenario:** David's bank is a net lender 28 days/month, net borrower 2 days/month (regulatory reporting).

```
Days 1-28: LEND MODE
  David deposits $10M US Treasuries to SignUIT pool
  Earns 4.0% APY continuously
  Daily earnings: $1,095.89
  28-day earnings: $30,684.93

Day 29-30: BORROW MODE (month-end regulatory reporting)
  Bank needs $20M for balance sheet window dressing
  Borrows $20M USDC overnight × 2 nights
  Rate: 3.0% APY = $1,643.84 total interest

  NET MONTH:
    Earned (lending):   $30,684.93
    Paid (borrowing):   $1,643.84
    Net profit:         $29,041.09

  vs. OLD WORLD (FHLB + Fed Window):
    Earned: $0 (no repo access)
    Paid:   ~$4,000 (discount window + FHLB fees)
    SignUIT advantage: $33,041/month = $396,492/year
```

---

## Dashboard Design

### LP Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│  SignUIT                                [Sarah.eth] [Disconnect] │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  YOUR PORTFOLIO                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ Total Value  │  │ Today's Earn │  │  Current APY  │           │
│  │  $50,009,123 │  │   +$9,123    │  │    4.5%       │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│                                                                   │
│  YOUR POSITIONS                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Pool          Deposited    APY   Earned(7d)  Util   Act  │   │
│  │ US-TRSY/USDC  $30,000,000  4.5%  $8,904     72%  [▼]    │   │
│  │ UK-GILT/USDC  $20,000,000  3.8%  $5,205     65%  [▼]    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  [+ Add Liquidity]                                               │
│                                                                   │
│  POOL ANALYTICS                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  APY History (30d)       Pool Utilization                │   │
│  │  5% ┤    ╭──╮           ████████░░  72%                  │   │
│  │  4% ┤───╯    ╰──        Borrowers active: 47             │   │
│  │  3% ┤                   Available to LP: $140M           │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Borrower Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│  SignUIT                                [Mike.eth]  [Disconnect] │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  QUICK BORROW                                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  I want to borrow: [$5,000,000      ] USDC               │   │
│  │  Using collateral: [US Treasury   ▼]                     │   │
│  │                                                          │   │
│  │  Current rate:     2.8% APY                              │   │
│  │  Collateral needed: $5,263,158   (95% LTV)               │   │
│  │  Your collateral:  $12,000,000  ✓ Sufficient             │   │
│  │  Interest (1 day): $383.56                               │   │
│  │                                                          │   │
│  │  Duration: [Overnight ▼]   [Borrow Now →]                │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ACTIVE POSITIONS                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ #ID     Borrowed    Collateral       Rate  Maturity  Act  │   │
│  │ #12345  $5M USDC   $5.26M US-TRSY  2.8%  04-22    [Repay]│   │
│  │ #12340  $2M USDC   $2.1M UK-GILT   3.1%  04-25    [Repay]│   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  HEALTH METRICS                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ Collat Ratio │  │ Liquidation  │  │ Total Interest│           │
│  │   105% ✓     │  │  Safe Zone   │  │  $767/day    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

### Analytics Dashboard (Public/Admin)

```
┌─────────────────────────────────────────────────────────────────┐
│  SignUIT Analytics                                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  PROTOCOL OVERVIEW                                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │  TVL     │  │ 24h Vol  │  │ Tot Fees │  │ Act Users│        │
│  │  $500M   │  │  $45M    │  │  $1.2M   │  │   234    │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
│                                                                   │
│  POOL PERFORMANCE                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Pool          TVL      Util   Volume(24h)  APY  Borrowers│   │
│  │ US-TRSY/USDC  $300M    72%    $32M         4.1%  156     │   │
│  │ UK-GILT/USDC  $120M    65%    $8M          3.7%   61     │   │
│  │ BUND/USDC     $80M     58%    $5M          3.2%   17     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  RATE CURVE (US-TRSY/USDC Pool)                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  5% ┤                                           ╭────    │   │
│  │  4% ┤                                    ╭─────╯         │   │
│  │  3% ┤                         ╭─────────╯                │   │
│  │  2% ┤─────────────────────────                           │   │
│  │     └──────────────────────────────────────────────────  │   │
│  │     0%  20%  40%  60%  80%  100% utilization             │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technical Architecture

### Stack Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     SignUIT Frontend                         │
│                  React + TypeScript + Tailwind               │
├─────────────────────────────────────────────────────────────┤
│                     Canton HTTP API                          │
│              (Ledger API + JSON API Gateway)                 │
├───────────────────────┬─────────────────────────────────────┤
│   Daml Smart          │     External Integrations            │
│   Contracts           │                                      │
│                       │  ┌─────────────┐  ┌──────────────┐  │
│  - RepoPool.daml      │  │  Chainlink  │  │    Circle    │  │
│  - Position.daml      │  │   Oracle    │  │  USDC/USYC   │  │
│  - LPToken.daml       │  │  (prices)   │  │  (cash leg)  │  │
│  - AMM.daml           │  └─────────────┘  └──────────────┘  │
│  - Liquidation.daml   │                                      │
├───────────────────────┴─────────────────────────────────────┤
│                   Canton Network                             │
│         (Privacy-preserving distributed ledger)              │
│                                                              │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐               │
│   │ Goldman  │   │  Circle  │   │ Chainlink│               │
│   │ (LP)     │   │ (USDC)   │   │ (Oracle) │               │
│   └──────────┘   └──────────┘   └──────────┘               │
└─────────────────────────────────────────────────────────────┘
```

### Daml Contract Design

**RepoPool.daml** — Core AMM pool contract
```
template RepoPool
  with
    operator     : Party         -- SignUIT protocol
    collateral   : InstrumentKey -- e.g. US-TRSY
    cash         : InstrumentKey -- USDC
    totalCash    : Decimal        -- Total USDC in pool
    totalCollat  : Decimal        -- Total collateral locked
    lpTokenSupply: Decimal        -- Total LP tokens minted
    baseRate     : Decimal        -- Minimum repo rate (e.g. 2.0%)
    rateSlope    : Decimal        -- Rate increase per utilization unit
```

**Position.daml** — Individual borrow position
```
template Position
  with
    positionId   : Text
    borrower     : Party
    borrowed     : Decimal    -- USDC amount
    collateral   : Decimal    -- Collateral locked
    rate         : Decimal    -- Fixed rate at origination
    startTime    : Time
    maturity     : Time       -- Overnight = startTime + 1 day
    status       : PositionStatus  -- Active | Repaid | Liquidated
```

**LPToken.daml** — LP share token
```
template LPToken
  with
    holder       : Party
    pool         : ContractId RepoPool
    amount       : Decimal    -- Number of LP tokens
    depositTime  : Time
```

### Canton Privacy Model

Every transaction in SignUIT uses Canton's sub-transaction privacy:

- **Borrower privacy:** Goldman Sachs (as LP) cannot see who is borrowing or for what purpose
- **Rate privacy:** Competing firms cannot see each other's positions
- **Collateral privacy:** Only the protocol and the borrower see collateral details
- **Disclosure:** Only what is needed for settlement is revealed, per Canton privacy contracts

This is the key differentiator vs. traditional bilateral repo — SignUIT provides Goldman Sachs-level rates with Verition-level privacy.

---

## Business Model

### Revenue Streams

| Stream | Rate | Who Pays |
|---|---|---|
| Protocol Fee | 0.10% of borrowed amount | Borrower |
| LP Spread | 0.15% (LP earns 0.15% less than full rate) | Distributed to protocol |
| Liquidation Penalty | 2% of liquidated collateral | Defaulting borrower |
| Pool Deployment Fee | 0.05% one-time | New pool launchers (later) |

### Unit Economics Example

**$100M pool at 70% utilization, 4.0% gross rate:**

```
Gross interest generated:     $100M × 70% × 4.0% / 365 = $7,671/day
LP receives (3.85% rate):     $100M × 70% × 3.85% / 365 = $7,381/day
Protocol fee (0.15%):         $100M × 70% × 0.15% / 365 = $  288/day
+ Protocol fee (0.10%):       $100M × 70% × 0.10% / 365 = $  192/day
                                                          ─────────────
Total protocol revenue:                                   $  480/day
Annual (1 pool, $100M):                                   $175,200/year
```

### Volume-Based Revenue Projection

| Year | TVL | Monthly Volume | Annual Revenue |
|---|---|---|---|
| Year 1 (post-launch) | $200M | $1B | $1.5M |
| Year 2 | $1B | $5B | $7.5M |
| Year 3 | $3B | $15B | $22.5M |

---

## Market Analysis

### Competitive Landscape

| | Broadridge DLR | Tradeweb Repo | SignUIT |
|---|---|---|---|
| **Access** | Goldman, UBS, SocGen | DRW, Virtu only | Any institution |
| **Minimum** | $100M+ | Invitation | $1M |
| **Settlement** | T+0 | T+0 | Instant |
| **Availability** | Business hours | Business hours | 24/7 |
| **Privacy** | Bilateral (exposed) | Platform sees all | Canton privacy |
| **Rate transparency** | Opaque | Opaque | Algorithmic/public |
| **Weekend** | No | No | Yes |
| **Canton native** | Yes | No | Yes |

### Why SignUIT Wins

1. **Broadridge DLR** is a bilateral matching platform, not an AMM. It requires counterparty relationships. SignUIT is permissionless — any Canton participant can use it.

2. **Tradeweb Repo** is not on Canton and is invitation-only for top-tier dealers. Not addressable by buy-side.

3. **No AMM exists on Canton.** Cantex, Canton Exchange, Pool Party — all DEXes for spot trading. None do repo. SignUIT is the first.

### Total Addressable Market

```
Canton repo volume (Broadridge DLR):   $6.9T/month
Buy-side excluded (58% of participants): $4.0T addressable
SignUIT Year 1 target (0.025%):          $1B/month
SignUIT Year 3 target (0.2%):            $15B/month
```

---

## Go-to-Market Strategy

### Phase 1: Launch (Months 1-3)

**Target:** 5 buy-side institutions, 2 LP institutions

- Partner with **Circle** for USDC rails (existing Canton integration)
- List on **Canton ecosystem page** as Featured App
- **Direct outreach:** 20 mid-size hedge funds excluded from DLR
- **Initial pools:** US-TRSY/USDC only (single pool, proven collateral)
- **KPIs:** $50M TVL, 20 borrowers, $200M monthly volume

### Phase 2: Growth (Months 4-12)

**Target:** 50+ institutions across LP and borrower roles

- Add **UK Gilt / USDC** pool (tap European buy-side)
- Integrate **Chainlink CCIP** for cross-chain collateral portability
- Partner with **DTCC** or regional custodians for collateral bridging
- Mobile app launch (critical for Mike's 3:45 PM use case)
- **KPIs:** $500M TVL, 200+ borrowers, $2B monthly volume

### Phase 3: Scale (Year 2+)

**Target:** Become the default repo layer for Canton Network

- Multi-collateral expansion (Bunds, JGBs, corporate bonds)
- White-label offering for large institutions to run their own pools
- Integration with Broadridge DLR for overflow liquidity routing
- Explore tokenized money market fund collateral (Franklin Templeton, BlackRock)
- **KPIs:** $3B TVL, $15B monthly volume, $22.5M annual revenue

### Partnership Targets

| Partner | Why | Status |
|---|---|---|
| Circle | USDC rails, native Canton integration | Existing Canton partner |
| Chainlink | Price oracles, CCIP bridge | Existing Canton partner |
| Broadridge | Overflow routing from DLR | Target outreach |
| DTCC | Collateral tokenization | Target outreach |
| Hashnote | USYC (tokenized T-bills) | Target outreach |

---

## MVP Roadmap (HackCanton)

### 4-Week Build Plan

**Week 1: Core Contracts**
- [ ] `RepoPool.daml` — AMM pool with deposit/withdraw
- [ ] `Position.daml` — Borrow/repay lifecycle
- [ ] `LPToken.daml` — LP share tokens
- [ ] Deploy to Canton testnet
- [ ] Unit tests for all contracts

**Week 2: Backend + API**
- [ ] Canton HTTP Ledger API integration
- [ ] Rate calculation service (utilization → rate)
- [ ] Position monitoring service (maturity alerts)
- [ ] Mock collateral oracle (Chainlink stub for MVP)

**Week 3: Frontend (MVP UI)**
- [ ] Borrower dashboard: Quick Borrow widget
- [ ] LP dashboard: Deposit / Withdraw / Earnings
- [ ] Position table: Active borrows with repay button
- [ ] Pool stats: TVL, utilization, current rate
- [ ] Canton wallet connect

**Week 4: Polish + Demo**
- [ ] Demo scenario scripted (Sarah + Mike personas)
- [ ] Analytics page (protocol TVL, volume, fees)
- [ ] Pitch deck aligned with working demo
- [ ] Testnet demo video (backup if live fails)

### MVP Scope (In)

- Single pool: US Treasury tokens / USDC
- Overnight repo duration only
- Manual liquidation (oracle price checked on repay)
- Basic LP deposit/withdraw
- Canton testnet deployment
- 2 demo accounts (LP + Borrower)

### MVP Scope (Out — Post-Hackathon)

- Multi-collateral pools
- Automated liquidation bots
- Mobile app
- Cross-chain collateral
- Real Chainlink oracle integration
- KYC/AML module

### Demo Script (5 Minutes)

```
Min 0-1: PROBLEM
  Show slide: "$25B unremunerated collateral"
  Show slide: "Only Goldman/UBS on Broadridge DLR"
  "58% of Canton participants have no repo access"

Min 1-2: SOLUTION OVERVIEW
  Show SignUIT logo + tagline
  "AMM for repo. Uniswap, but for repurchase agreements."
  Canton Network native, privacy-preserving

Min 2-4: LIVE DEMO
  --- LP flow (Sarah, 90 seconds) ---
  Open LP dashboard
  Click "Add Liquidity" → $30M USDC
  Show: APY 4.5%, projected weekend earnings $13,700
  Confirm transaction → LP tokens minted

  --- Borrower flow (Mike, 90 seconds) ---
  Switch to borrower account
  Enter $5M borrow → collateral auto-calculated
  Confirm → $5M USDC received in 30 seconds
  Show position: #12345, 2.8% rate, $383 interest

Min 4-5: MARKET + ASK
  $6.9T/month market, 0 open-access platforms
  Year 1: $1B volume, $1.5M revenue
  Ask: HackCanton recognition + Canton ecosystem onboarding
```

---

## Financial Projections

### 3-Year Model

| Metric | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| TVL | $200M | $1B | $3B |
| Monthly Volume | $1B | $5B | $15B |
| Active Users | 50 | 250 | 1,000 |
| Protocol Fee Revenue | $1.5M | $7.5M | $22.5M |
| Operating Costs | $800K | $2M | $5M |
| **Net Revenue** | **$700K** | **$5.5M** | **$17.5M** |

### Break-Even Analysis

```
Monthly fixed costs (Year 1):  ~$65K
  Engineering (2):              $40K
  Infrastructure (Canton node): $10K
  Legal/compliance:             $10K
  Other:                        $5K

Break-even monthly volume:     $325M
Expected Month 6 volume:       $500M+
Break-even timeline:           Month 4-5
```

---

## Why Canton Network

SignUIT could not exist without Canton. Here is why Canton is not just the platform — it is the competitive moat:

### 1. Privacy by Design

Traditional repo requires revealing your portfolio to your counterparty. This is why Goldman can read Verition's book when Verition calls for repo. Canton's sub-transaction privacy means:

- LPs cannot see individual borrower positions
- Borrowers cannot see LP identities
- Competing firms cannot reverse-engineer each other's positions from pool activity
- Privacy is enforced at the protocol layer, not through legal agreements

### 2. Daml Finance Library

Building repo contracts from scratch on EVM would take 6+ months of security audits. Daml Finance provides:

- Pre-audited `Instrument` and `Holdings` templates
- `Settlement` workflows (atomic swap, delivery vs payment)
- `Lifecycle` management (coupon payments, maturity events)
- Canton team support for integration

### 3. Institutional Trust

Canton's participants are Goldman Sachs, Deutsche Bank, BNP Paribas, SIX Swiss Exchange. This is the only distributed ledger where buy-side firms can plausibly interact with sell-side institutions in a regulated, compliant context.

### 4. Interoperability with Broadridge DLR

Broadridge DLR already processes $6.9T/month on Canton. SignUIT can route excess demand to DLR (large tickets) and capture DLR overflow (small tickets). No other blockchain has this integration point.

### 5. Real-World Adoption

Canton is not a whitepaper blockchain. It has:
- 25+ major financial institutions in production
- $1T+ in assets represented on-chain
- Regulatory engagement with SEC, ESMA, FCA

---

## Risk Analysis

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Smart contract bug (funds lost) | Low | Critical | Daml Finance pre-audited templates; formal verification |
| Oracle manipulation | Low | High | Chainlink TWAP + circuit breakers |
| Canton network downtime | Very Low | High | Multiple node operators; SLA monitoring |
| Liquidation cascade (collateral devalued rapidly) | Low | Medium | Conservative LTV (95% vs 98% typical); early liquidation threshold |

### Market Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Institutional adoption slow | Medium | High | Start with 3 anchor LPs (seed $100M TVL before launch) |
| Broadridge DLR expands access | Low | Medium | SignUIT's AMM model is structurally different; not direct competition |
| Interest rate compression (rates near 0%) | Low | Medium | Revenue scales with volume, not just rate; 0% rates = high LP demand |

### Regulatory Considerations

- Repo is a regulated financial instrument in most jurisdictions
- SignUIT is a protocol, not a broker-dealer (similar to Uniswap legal structure)
- Canton's institutional participants already have their own regulatory frameworks
- Recommend: Legal wrapper as a foundation or association (Swiss/Cayman structure)
- CFTC guidance on digital asset repo is evolving — monitor closely

---

## Summary

**SignUIT** is the missing piece of the Canton ecosystem:

- The repo market is $6.9T/month and growing
- 58% of participants are excluded from current platforms
- $25B per firm sits unremunerated every night
- No open-access, AMM-based repo solution exists on Canton

SignUIT opens the repo market to anyone with tokenized collateral and a Canton wallet. Not just Goldman. Everyone.

**Sign. Use. It.**

---

*Document version: 1.0 — HackCanton Season #1 Submission Draft*  
*Last updated: April 2026*  
*Repository: canton-research/SIGNUIT.md*
