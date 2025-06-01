
# Framework for LLM Behavioral Evaluation

This repository provides a unified framework to systematically evaluate the economic and strategic reasoning behavior of Large Language Models (LLMs). It combines principles from behavioral economics and game theory to assess how LLMs make decisions under uncertainty, engage in strategic interactions, and respond to socio-demographic contexts.

---

## 🔍 Project Scope

LLMs are increasingly used in high-stakes applications such as finance, healthcare, and public policy. This framework aims to audit their decision-making characteristics by:

- Measuring behavioral biases (e.g., risk aversion, loss aversion, probability distortion)
- Evaluating depth of strategic reasoning in game-theoretic settings
- Investigating the influence of demographic cues on model outputs

---

## 🧩 Components

### 1. Economic Behavior Module
- Evaluates individual LLM decision-making using structured multiple-choice tasks based on the Tanaka-Camerer-Nguyen model
- Computes behavioral parameters such as risk and loss aversion
- Includes persona-based prompting to probe socio-demographic sensitivity

➡️ See detailed implementation in: [`README.md`](./TCN_model/README.md)

---

### 2. Strategic Reasoning Module
- Estimates reasoning depth (τ) using Truncated Quantal Response Equilibrium (TQRE) on strategic games
- Applies log-likelihood optimization to fit LLM behavior to bounded rationality models
- Analyzes demographic effects through regression modeling

➡️ See detailed implementation in: [`README_StrategicReasoning.md`](./TQRE_model/README.md)

---

## 📦 Structure Overview

```
.
├── api_collect_data_*.py               # Scripts to query LLMs with persona prompts
├── profile_*.py                        # Demographic profile generators (US, UK, China, etc.)
├── Cal_Parameters.ipynb               # Notebook for parameter boundary estimation
├── estimation_submission.ipynb        # Strategic reasoning estimation pipeline
├── *.csv                              # Raw and processed data (responses, profiles, parameters)
├── README.md                          # Economic behavior component details
├── README_StrategicReasoning.md       # Strategic reasoning component details
└── readme.txt                         # Legacy notes
```

---

## 📊 Final Deliverables

- Behavioral benchmarks for multiple LLMs across decision-making scenarios
- Auditable outputs including:
  - Parameter CSVs
  - Demographic effect analyses
  - Chain-of-Thought (CoT) vs. baseline comparisons
- Open-source datasets and reproducible analysis pipelines

---

## 📋 License and Contributions

This framework is developed for research and transparency. Contributions and extensions (e.g., adding more LLMs or decision domains) are welcome via pull requests.

---

For any inquiries or collaborations, please contact [Zehua Yuan](https://github.com/NeoYY).
