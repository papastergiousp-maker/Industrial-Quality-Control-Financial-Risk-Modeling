# Industrial Tomato Quality Control Pipeline

A data analytics project that simulates the decision-making logic of a Quality Control Analyst on an industrial tomato paste production line, inspired by personal experience at D. Nomikos S.A.

> **Disclaimer:** This project uses 100% synthetic data and personal cost estimations for methodology demonstration purposes only. It does not contain real or confidential corporate data.

---

## What Does This Project Do?

Imagine a tomato paste factory running 24 hours a day. Every hour, a lab analyst takes a sample and measures 8 quality parameters (acidity, colour, viscosity, salt, etc.). The analyst then decides: is this batch good to ship, does it need correction, or must it be discarded?

This project **automates that decision** using Python and turns it into a full financial report:

1. **Reads** 720 hourly measurements across 8 quality parameters
2. **Compares** each measurement against the official MFD-024 spec sheet limits
3. **Classifies** every batch into one of three outcomes:
   - **Accept** — all parameters within spec → €0 cost
   - **Correction** — 1–2 parameters marginally out of spec → €450 (citric acid dosing + labor + QC)
   - **Critical Waste** — critical parameter severely out of spec, or 3+ failures → €6,000 (lost batch + sanitization + investigation + disposal)
4. **Calculates** the total financial impact of production failures
5. **Simulates** what happens if HACCP / ISO 22000 quality protocols are implemented (how much cost is saved)
6. **Generates** 14 professional charts, an Excel report, and an interactive web dashboard

---

## Business Problem

Without automated QC monitoring, production failures are caught late — after the batch has already been processed and packaged. A single discarded batch costs €6,000. On a 30-day season month with a 3% failure rate, that is €276,000 in waste alone.

This project demonstrates that implementing HACCP/ISO 22000 protocols reduces failures by 25% and operational costs by 15%, saving approximately **€355,000 per season** — validated against the published financials of Kyknos S.A. (Athens Stock Exchange).

---

## Project Evolution

**Phase 1 — Prototype** (`INDUSTRIAL ANOMALY DETECTION.ipynb`): Single-parameter pH proof-of-concept analyzing 480 batches with a simple if-elif-else classification engine. Built to validate the business logic.

**Phase 2 — Full Pipeline** (`generate_pipeline.py`): Production-grade pipeline processing 720 hourly batches across 8 quality parameters with HACCP simulation, 14 charts, and a multi-sheet Excel report.

**Phase 3 — Interactive Dashboard** (`dashboard.html`): Client-side web dashboard. Open it in any browser, load the CSV, and explore the data with live filters, HACCP sliders, and CSV export.

---

## Spec Sheet — MFD-024 (D15 Aseptic Tomato Paste)

| Parameter | Min | Max | Target | Unit | What it measures |
|-----------|-----|-----|--------|------|-----------------|
| BRIX | 28.0 | 30.0 | 28.5 | % | Total soluble solids — paste concentration |
| COLOR a/b | 1.85 | 2.40 | 2.00 | ratio | Red-to-yellow colour ratio (Hunter Lab) |
| BOSTWICK | 2.0 | 6.0 | 4.0 | cm/30s | Viscosity / flow consistency |
| pH | 4.10 | 4.45 | 4.20 | — | Acidity level — food safety critical |
| ACIDITY | 0.0 | 8.0 | 6.5 | % | Titratable acidity |
| BLOTTER TEST | 0.0 | 5.0 | 3.0 | mm | Serum separation indicator |
| SYNERESIS | 0.0 | 6.0 | 4.0 | % | Water separation from paste |
| SALT | 1.5 | 2.5 | 2.0 | % | Sodium chloride content |

---

## HACCP / ISO 22000 Impact Simulation

| Metric | Baseline | With HACCP | Change |
|--------|----------|------------|--------|
| Monthly QC cost | €314,250 | €234,480 | −€79,770 |
| Annual savings (×3 season months) | — | €239,310 | +€239,310 |
| Annual revenue recovered | — | €115,500 | +€115,500 |
| **Total annual impact** | — | **~€355,000** | |
| Production yield | 93.6% | 95.1% | +1.5pp |

Benchmark: ~1% of Kyknos S.A. annual turnover (€36.3M), ~15% of Kyknos EBITDA (€2.4M) — consistent with realistic QC improvement at this production scale.

---

## Charts Generated (14 total)

| # | Chart | What it shows |
|---|-------|--------------|
| 00 | Pipeline Flow | End-to-end architecture diagram |
| 01 | Status Distribution | Donut chart — Accept / Correction / Waste percentages |
| 02 | Cost Breakdown | Monthly correction vs. waste vs. total cost |
| 03 | Daily Trend | Stacked bar (outcomes per day) + cost line chart |
| 04 | Parameter Distributions | 8 histograms vs. MFD-024 spec limits |
| 05 | HACCP Impact | Side-by-side Baseline vs. HACCP batch outcomes and costs |
| 06 | Pareto Analysis | 80/20 rule — which parameters cause most failures |
| 07 | Correlation Heatmap | Which parameters drift together (Pearson r) |
| 08 | SPC Control Chart | Statistical Process Control ±3σ for pH and BRIX |
| 09 | Process Capability | Cp / Cpk Six Sigma benchmark for all 8 parameters |
| 10 | Failure Heatmap | Hour-of-day × day-of-month failure cost map |
| 11 | Boxplots by Status | Parameter value distributions per batch outcome |
| 12 | ROI Break-Even | HACCP investment (€35K) payback timeline |
| 13 | Risk Priority Matrix | FMEA-style Frequency × Severity bubble chart |

---

## Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| pandas | Data manipulation and aggregation |
| NumPy | Statistical data generation (Normal Distribution) |
| matplotlib | Chart generation (14 PNG charts) |
| seaborn | Enhanced statistical visualizations |
| openpyxl | Excel report with embedded charts |
| Chart.js | Interactive charts in the dashboard |
| PapaParse | CSV parsing in the browser (dashboard) |

---

## How to Run

**One click:** Double-click `run_pipeline.bat` — installs all dependencies and generates all output files.

**Manual:**
```
py -3 generate_pipeline.py --regen
```

To view the dashboard: open `dashboard.html` in any browser, then load `tomato_qc_data.csv` when prompted.

---

## Files

| File | Description |
|------|-------------|
| `generate_pipeline.py` | Main pipeline — data generation, classification, costing, 14 charts, Excel export |
| `dashboard.html` | Interactive web dashboard — open locally in any browser |
| `run_pipeline.bat` | One-click runner (installs dependencies + runs pipeline) |
| `tomato_qc_data.csv` | 720 hourly batch records with Status, Cost, Deviations columns |
| `tomato_qc_report.xlsx` | 5-sheet Excel report with embedded charts |
| `HACCP_Impact_Simulation.csv` | Standalone HACCP/ISO 22000 financial impact analysis |
| `charts/` | 14 PNG charts |
| `INDUSTRIAL ANOMALY DETECTION.ipynb` | Phase 1 prototype — pH-only proof of concept |

---

## CV-Ready Summary

> "Designed and implemented a Python-based Quality Control pipeline for an industrial tomato paste production line, classifying 720 hourly batches across 8 physicochemical parameters against MFD-024 spec sheet limits. Performed HACCP / ISO 22000 impact simulation projecting ~€355K annual savings — benchmarked against Kyknos S.A. FY 2022–23 financials (Athens Stock Exchange). Delivered 14 analytical charts, a multi-sheet Excel report, and an interactive web dashboard."

---

## Sources

| Source | How it was used |
|--------|----------------|
| **Kyknos S.A. FY 2022–23 Annual Report** (Athens Stock Exchange — ATHEX) | Benchmark validation: turnover €36.3M, EBITDA €2.4M — used to confirm that the projected €355K annual impact is realistic for a single aseptic line at this scale |
| **EU Tomato Paste Market Reports 2024–25** | Wholesale paste price reference: €1,150/tonne for 28–30 Brix aseptic paste — used to calculate batch value (3t × €1,150 = €3,450 ≈ €3,500) |
| **MFD-024 Spec Sheet — D15 Aseptic Paste Line (D. Nomikos S.A.)** | Official spec limits for all 8 quality parameters (BRIX, COLOR, BOSTWICK, pH, ACIDITY, BLOTTER, SYNERESIS, SALT) |
| **Personal QC experience at D. Nomikos S.A.** | Cost estimates (correction €450, critical waste €6,000), HACCP reduction factors (−25% waste, −15% operational cost), and Greek tomato season duration (3 months, Aug–Oct) |
