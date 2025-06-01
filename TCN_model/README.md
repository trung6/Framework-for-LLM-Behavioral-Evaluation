
# LLM Behavioral Evaluation Framework

This project provides a comprehensive framework to evaluate the behavioral characteristics of Large Language Models (LLMs) using tools from behavioral economics and game theory. Our goal is to examine how LLMs respond to uncertainty, strategic interaction, and socio-demographic cues, and to quantify their decision-making parameters such as risk aversion, probability distortion, and loss aversion.

---

## 🔍 Overview

Our framework consists of three main components:

### 1. Demographic Feature Simulation & API Interaction
- **Profile Generation**: Scripts under `profile_*.py` generate synthetic user profiles using real-world demographic distributions (China, USA, UK, etc.) or randomized/augmented distributions (e.g., minority groups).
- **API Scripts**: 
  - `api_collect_data_gpt.py`, `api_collect_data_claude.py`, and `api_collect_data_gemini.py` interact with GPT-4, Claude, and Gemini models, respectively.
  - These scripts embed demographic personas into prompts and log model decisions across a set of structured economic tasks.

### 2. Behavioral Parameter Estimation
- **Notebook**: `Cal_Parameters.ipynb`
  - Symbolically and numerically solves for valid ranges of behavioral parameters:
    - `Sigma` (risk aversion)
    - `Alpha` (probability weighting)
    - `Lambda` (loss aversion; calculated externally in Excel)
  - Output saved to `sigma_results.csv` and `alpha_results.csv`.

### 3. Statistical Analysis
- A Stata script (not included here) processes LLM responses to:
  - Encode categorical variables
  - Perform descriptive analysis
  - Run regressions to quantify how demographic cues influence behavioral parameters

---

## 📂 Directory Structure

```
.
├── api_collect_data_gpt.py
├── api_collect_data_claude.py
├── api_collect_data_gemini.py
├── profile_USA.py
├── profile_UK.py
├── profile_China.py
├── profile_random.py
├── profile_random_minority.py
├── Cal_Parameters.ipynb
├── readme.txt (legacy)
└── data/
    ├── data.xlsx (external file for Lambda calculations)
    ├── sigma_results.csv
    ├── alpha_results.csv
```

---

## 🚀 How to Run

### Generate Demographic Samples
```bash
python profile_USA.py  # or UK/China/random
```

### Call LLM APIs
Set up your keys (OpenAI, Anthropic, Google) as environment variables or in the scripts, then run:
```bash
python api_collect_data_gpt.py
```

### Compute Parameter Ranges
Run `Cal_Parameters.ipynb` in a Jupyter environment. Outputs are saved to CSVs.

### Run Statistical Analysis (in Stata)
Ensure `data.xlsx` is prepared and cleaned, then run the Stata `.do` script provided in the supplementary material.

---

## 📦 Dependencies

- Python 3.9+
  - `openai`, `anthropic`, `google-generativeai`
  - `pandas`, `numpy`, `sympy`
- Jupyter Notebook (for parameter estimation)
- Stata (for regression analysis)

---

## 🎯 Final Output

The final artifact includes:
- A synthetic dataset of LLM responses across economic tasks
- Behavioral parameter estimates for each LLM
- A comparative analysis of how LLM behavior varies by model, task, and demographic prompt
- A reproducible framework for auditing LLM rationality and fairness

---

Let us know if you'd like to contribute or extend the evaluation framework!
