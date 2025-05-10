# Diabetes Markov Model for Patient Outcome Simulation

## Overview
This project simulates the progression of diabetes in patients using a Markov model, built as part of a class conference presentation on **"Markov Models in Healthcare: Simulating Patient Outcomes"**. The model predicts patient transitions between health states (Controlled, Uncontrolled, Severe, Death) over 5 years, leveraging the [Kaggle NIDDK Diabetes Dataset](https://www.kaggle.com/datasets/mathchi/diabetes-data-set?resource=download). The results align with real-world benchmarks from the CDC (20–30% complication rate) and UKPDS (~10–20% mortality over 5 years), achieving a realistic distribution: ~46% Controlled, ~13% Uncontrolled, ~30% Severe, and ~11% Death.

## Dataset
The project uses the [Kaggle NIDDK Diabetes Dataset](https://www.kaggle.com/datasets/mathchi/diabetes-data-set?resource=download), which includes:
- **Patients**: 768 female patients of Pima Indian heritage.
- **Features**: Glucose, Insulin, BMI, Blood Pressure, Age, etc.
- **States Defined**:
  - **Controlled**: Blood Glucose < 140 mg/dL
  - **Uncontrolled**: Blood Glucose 140–199 mg/dL
  - **Severe**: Blood Glucose ≥ 200 mg/dL
- **Initial Distribution**: ~65% Controlled, ~25% Uncontrolled, ~10% Severe (derived from Glucose levels).

The dataset is cross-sectional, so transition probabilities were tuned using literature (CDC, UKPDS).

## Markov Model
The Markov model simulates 1000 patients over 60 months (5 years) with the following states:
- **Controlled**: Well-managed diabetes.
- **Uncontrolled**: Poorly managed diabetes.
- **Severe**: Advanced complications (e.g., retinopathy, nephropathy).
- **Death**: Absorbing state.

### Transition Matrix
The transition probabilities (`data/probabilities.csv`) were tuned to match:
- **CDC**: 20–30% complication rate over 5–10 years.
- **UKPDS**: 1–10% annual mortality, 2–15% annual complication progression.

Example (monthly probabilities):
```
Controlled,Uncontrolled,Severe,Death
0.9655,0.03,0.004,0.0005
0.10,0.80,0.095,0.005
0.00,0.05,0.945,0.005
0.00,0.00,0.00,1.00
```

### Results
Final state distribution after 5 years:
- **Controlled**: ~46% (460 patients)
- **Uncontrolled**: ~13% (131 patients)
- **Severe**: ~30% (298 patients)
- **Death**: ~11% (111 patients)

The model is stochastic, reflecting real-world variability, and results align with CDC and UKPDS benchmarks.

## Visualizations
The project includes five visualizations (generated in `notebooks/Diabetes_Markov_Model.ipynb`):
1. **State Distribution**: Bar chart of final patient states (~46% Controlled, ~30% Severe).
2. **Patient Trajectory**: Sample patient’s transitions (e.g., Controlled → Severe) with labeled complications.
3. **Transition Heatmap**: Probability matrix (e.g., 94.5% Severe retention).
4. **Cohort Progression**: Proportions of patients in each state over 60 months.
5. **Cumulative Deaths**: Cumulative mortality reaching ~11%.

Plots are saved as PNGs (e.g., `state_distribution.png`) in the project directory.




## References
- **Kaggle NIDDK Diabetes Dataset**: https://www.kaggle.com/datasets/mathchi/diabetes-data-set
- **CDC National Diabetes Statistics Report**: https://www.cdc.gov/diabetes/data/statistics-report/
- **UKPDS**: Stratton et al., 2000 (PubMed ID: 10905422)

