# Cascade Log Example: Agri / Commodities Market Entry

This example continues [agri_commodity_market_entry.md](agri_commodity_market_entry.md) after the initial strategy choice.

## Project

- **Name:** DniproSun India market entry
- **Owner:** Export Director
- **Domain:** edible oils / agri commodities
- **Created at:** 2026-03-10T09:00:00Z
- **Description:** phased India entry for sunflower oil under freight, FX, and channel uncertainty

## Parties

| ID | Party | Role | Incentives | Expected reaction |
| --- | --- | --- | --- | --- |
| party-1 | DniproSun Foods | exporter / decision owner | grow export mix while holding margin floor | stay disciplined on credit and channel focus |
| party-2 | GulfEast Distributors | India food-service distributor | secure reliable imported sunflower supply with workable payment terms | push for longer credit and volume rebates |
| party-3 | Regional private-label retailer | alternative channel partner | lock margin-positive private label supply | demand exclusivity if trials work |
| party-4 | incumbent edible-oil suppliers | competitor set | defend procurement accounts and price share | respond with tactical discounting |

## Decision Version v1

- **Version:** v1
- **Date:** 2026-03-10T09:00:00Z
- **Decision statement:** enter India in the next 6 months without breaking the 8% gross margin floor
- **Chosen strategy:** food-service distributor wedge with strict receivables guardrails
- **Rejected or deferred options:** premium urban retail launch, private label first, full wait-and-watch
- **Accepted trade-offs:** lower early brand visibility in exchange for faster operational learning
- **Confidence:** Medium
- **Confidence rationale:** best initial fit with current resources, but channel economics depend on discipline in collections and commodity pricing
- **Revisit triggers:** collection cycle >95 days; landed margin <8%; distributor reorder missing after first trial shipments
- **What changed since last version:** initial decision

## Active Assumptions

| ID | Assumption | Confidence | Status | Evidence |
| --- | --- | --- | --- | --- |
| a-1 | institutional buyers value supply reliability enough to pay a sunflower premium | Medium | active | distributor interviews and prior regional buyer feedback |
| a-2 | first distributor can convert trial volume into repeat demand within 8 weeks | Medium | active | distributor pipeline claims; no shipment proof yet |
| a-3 | landed margin can stay above 8% if FX remains within planning band | Low | active | freight and FX scenario model |

## Signals

| ID | Signal | Metric | Direction | Threshold | Source | Related revisit triggers |
| --- | --- | --- | --- | --- | --- | --- |
| s-1 | gross margin after logistics | blended shipped margin | stable | >=8% | internal finance model | landed margin floor |
| s-2 | receivables cycle | days sales outstanding | stable | <=95 days | distributor aging report | collection risk |
| s-3 | reorder velocity | days from first shipment to repeat PO | stable | <=56 days | distributor sales report | channel proof |

## Actions

| ID | Description | Owner | Status | Due date | Depends on |
| --- | --- | --- | --- | --- | --- |
| act-1 | finalize first distributor contract with collection guardrails | Export Director | done | 2026-03-24 |  |
| act-2 | ship first trial container of 15L food-service packs | Supply Lead | done | 2026-04-02 | act-1 |
| act-3 | open private-label fallback conversation with one regional retailer | Commercial Manager | in_progress | 2026-04-20 | act-1 |

## Outcomes

| ID | Summary | Impact | Recorded at | Related decision version |
| --- | --- | --- | --- | --- |
| out-1 | first trial shipment cleared on time with no customs exception | positive | 2026-04-04T16:00:00Z | v1 |
| out-2 | initial sell-through in institutional kitchens outperformed distributor forecast by 18% | positive | 2026-04-29T18:00:00Z | v1 |

## Update Entry u1

- **Update ID:** u1
- **Timestamp:** 2026-05-02T10:30:00Z
- **Change summary:** demand signal is stronger than expected, but payment-term pressure and private-label interest increased
- **What happened since last version:** first distributor reordered earlier than expected, but requested 105-day terms for the second purchase cycle
- **Facts added or changed:**
  - repeat purchase order arrived 41 days after first shipment
  - landed margin remained at 9.1% on the first cycle
  - distributor asked for longer payment terms tied to volume growth
  - one regional retailer opened a private-label conversation after seeing category movement
- **Assumptions confirmed:**
  - `a-1` reliability matters in food-service procurement
  - `a-2` repeat demand can appear inside the target window
- **Assumptions invalidated:**
  - none fully invalidated
- **Signals that moved:**
  - `s-3` improved from stable to favorable
  - `s-2` moved toward risk because the distributor is pushing longer terms
- **Did other parties react as expected?:**
  - competitors responded through tactical discounts, not through service guarantees
- **Current decision status:** adapt
- **Updated working hypothesis:** continue the food-service wedge, but do not expand volume unless payment terms stay within risk policy; keep the private-label path active as a hedge, not the primary strategy
- **Revised revisit triggers:**
  - if DSO exceeds 95 days, freeze volume expansion
  - if private-label economics exceed food-service margin by >1.5 points with acceptable exclusivity terms, reopen channel prioritization
- **Next review at:** 2026-05-24T09:00:00Z
