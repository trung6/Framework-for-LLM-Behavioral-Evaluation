
# LLM Strategic Reasoning Evaluation

This project evaluates the strategic reasoning capabilities of Large Language Models (LLMs) through behavioral game theory frameworks. It consists of two main components:

---

## 🧠 1. Parameter Estimation (Python)

This component estimates reasoning parameters based on LLM behavior in one-shot strategic games. It uses bounded rationality assumptions and log-likelihood optimization to infer reasoning depth (τ).

### 📁 Files
- `estimation_submission.ipynb`: Jupyter notebook for full parameter estimation workflow.
- Input data:
  - `base.csv`, `baseCoT.csv`
  - `highstake.csv`, `highstakeCoT.csv`
  - `lowstake.csv`
- Output:
  - Estimation results are saved as CSVs with reasoning parameters like τ (tau).

### ⚙️ Key Estimation Steps
1. Load payoff matrix and LLM decision data.
2. Estimate expected utility under different opponent beliefs.
3. Compute level-k choice probabilities.
4. Optimize log-likelihood function to estimate reasoning depth.

---

## 👥 2. Demographic Feature Evaluation (Stata)

This analysis investigates whether LLM decisions are influenced by demographic embeddings (e.g., age, gender, education, race, politics).

### 📊 Analysis Steps
- Prepare and clean dataset (`Profile.csv`, `aggregated_demographic_100.csv`, `aggregated_demographic_CoT_100.csv`)
- Generate dummy variables for each demographic feature
- Run OLS regressions to assess impact on τ (reasoning depth)
- Separate regressions for CoT vs. non-CoT responses
- Export regression tables and coefficient plots

### 📁 Files
- `demographic_analysis.do` (not included here)
- Input:
  - `aggregated_demographic_100.csv`
  - `aggregated_demographic_CoT_100.csv`
- Output:
  - `regression_results.csv`, `regression_results_cot.csv`
  - Visualizations of demographic effects on LLM reasoning

---

## 📦 Dependencies

- Python 3.9+
  - `numpy`, `pandas`, `scipy`
  - `matplotlib`, `seaborn` (optional for plotting)
- Jupyter Notebook
- Stata (with ability to run `.do` files and import CSVs)

---

## ✅ Final Output

The final artifact includes:
- Reasoning depth estimations across game types and LLMs
- Comparative analysis of baseline vs. Chain-of-Thought prompting
- Demographic influence quantification on decision rationality
- CSV summaries and plots for reproducibility and audit

---

Feel free to contribute by extending analysis to more models or integrating new behavioral benchmarks.
