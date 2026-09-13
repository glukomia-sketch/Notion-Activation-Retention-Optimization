# Notion Activation & Retention Optimization

## Product Management Case Study

A product analytics and strategy case study focused on identifying onboarding friction, improving user activation, and increasing recurring engagement through data-driven product decisions.

> **Note:** This project uses a synthetic dataset for portfolio and product-management analysis purposes. NotionStart and SmartTemplate are proposed product concepts, not existing Notion features.

---

##  Product Objective

**Identify onboarding and engagement gaps to improve user activation and retention.**

---

##  Problem Statement

New users may sign up but fail to reach meaningful product value because of friction during onboarding and early product usage.

This project analyzes the user journey from **signup → onboarding → workspace creation → content creation → collaboration** to identify the largest activation drop-offs and prioritize product opportunities.

---

##  Product Analytics

The analysis evaluates:

* User activation funnel
* Onboarding drop-offs
* Acquisition-channel performance
* Cohort retention
* Experiment performance
* Product engagement metrics

### Activation Journey

**Signup → Onboarding Started → Workspace Created → Content Created → Collaboration → Paid**

The project defines **Collaboration** as the activation milestone because it represents meaningful product usage beyond initial setup.

---

##  Product Solutions

### 1. NotionStart

A personalized onboarding experience that recommends a relevant starting workflow based on the user's goals and use case.

**Expected impact:**

* Reduce onboarding friction
* Improve time-to-value
* Increase workspace creation
* Increase activation rate

### 2. SmartTemplate

A personalized template recommendation system that helps users quickly create relevant workflows after setting up their workspace.

**Expected impact:**

* Increase content creation
* Improve feature adoption
* Increase recurring engagement
* Improve retention

---

##  RICE Prioritization

Product opportunities are prioritized using:

**RICE = Reach × Impact × Confidence ÷ Effort**

| Initiative               | Reach | Impact | Confidence | Effort | RICE Score |
| ------------------------ | ----: | -----: | ---------: | -----: | ---------: |
| NotionStart              |     9 |    3.0 |        0.9 |      3 |    **8.1** |
| SmartTemplate            |     8 |    2.5 |       0.85 |      4 |   **4.25** |
| Guided Collaboration     |     6 |    2.5 |        0.8 |      5 |    **2.4** |
| Advanced Personalization |     5 |    2.0 |        0.7 |      6 |   **1.17** |

**Prioritization decision:** NotionStart is prioritized first because it combines high reach, strong expected activation impact, high confidence, and moderate effort.

> RICE scores are relative portfolio estimates and are not observed product results.

---

##  Experimentation Roadmap

### Experiment 1 — NotionStart

**Hypothesis:** Personalized onboarding will increase the percentage of new users reaching activation.

**Control:** Existing onboarding
**Treatment:** NotionStart personalized onboarding

**Primary KPI:** Activation Rate

**Secondary KPIs:**

* Workspace creation rate
* Content creation rate
* Time-to-value
* D7 retention

### Experiment 2 — SmartTemplate

**Hypothesis:** Personalized templates will increase meaningful product usage after workspace creation.

**Control:** Generic template recommendations
**Treatment:** SmartTemplate recommendations

**Primary KPI:** Content Creation Rate

**Secondary KPIs:**

* Template adoption
* Feature adoption
* DAU/MAU
* D7/D30 retention

---

##  Success Metrics

| Metric           | Product Goal                                           |
| ---------------- | ------------------------------------------------------ |
| Activation Rate  | Increase users reaching meaningful collaboration       |
| Time-to-Value    | Reduce time required to reach first meaningful outcome |
| Feature Adoption | Increase adoption of recommended workflows             |
| D7/D30 Retention | Improve recurring product usage                        |
| DAU/MAU          | Increase engagement frequency                          |

---

## Tech Stack

* **Python** — Product analytics and data processing
* **SQL** — Funnel, retention and experiment analysis
* **Streamlit** — Interactive product analytics dashboard
* **Plotly** — Product analytics visualizations
* **Pandas** — Data manipulation
* **Git/GitHub** — Version control

---

##  Project Structure

```text
├── data/
│   └── sample/
├── docs/
│   ├── business_problem.rst
│   ├── executive_summary.rst
│   ├── metric_dictionary.rst
│   └── product_strategy.md
├── python/
│   └── src/
│       ├── analysis.py
│       ├── generate_data.py
│       ├── metrics.py
│       └── run_sql_models.py
├── sql/
│   ├── marts/
│   │   ├── mart_cohort_retention.sql
│   │   ├── mart_experiment_results.sql
│   │   ├── mart_funnel.sql
│   │   └── mart_product_growth_daily.sql
│   └── staging/
└── streamlit_app/
    └── pages/
        ├── 01_executive_summary.py
        ├── 02_funnel.py
        ├── 03_cohorts.py
        └── 04_experimentation.py
```

---

##  Product Decision Framework

**User Journey Analysis**
↓
**Identify Activation Drop-off**
↓
**Define User Problem**
↓
**Generate Product Solutions**
↓
**Prioritize Using RICE**
↓
**Design Experiments**
↓
**Measure KPI Impact**
↓
**Iterate**

---

## Key PM Skills Demonstrated

* User Journey Analysis
* Funnel Analysis
* Product Analytics
* Problem Prioritization
* RICE Framework
* Product Strategy
* Experiment Design
* KPI Definition
* Activation & Retention Analysis
* User-Centric Product Thinking
* Data-Driven Decision Making
