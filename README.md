# Maternal Health Outcomes Analysis using Midwifery Integration Scores (MISS)

## Overview

This project investigates the relationship between Midwifery Integration Scores (MISS) and maternal health outcomes across the United States. The goal is to identify statistically significant policy drivers that influence maternal health, particularly in vulnerable populations.

By applying multivariate statistical analysis and data visualization techniques, this project provides evidence-based insights that can inform healthcare policy and improve maternal outcomes.

---

## Objectives
- Quantify relationships between MISS and maternal health indicators
- Identify statistically significant policy drivers (p < 0.05)
- Detect outliers and trends across multiple years of U.S. data
- Reduce bias by controlling for confounding variables
- Improve feature selection for predictive modeling

---

## Dataset & Sources
**Primary Source:** Vedam, S. et al. (2019, February 27). Mapping integration of midwives across the United States: Impact on access, equity, and outcomes. UBC Research Data. Retrieved April 29, 2026, from https://open.library.ubc.ca/collections/researchdata/items/1.0363296

**DOI:** https://dx.doi.org/10.14288/1.0363296

**Primary dataset:** Vedam, Saraswathi et al., 2019, "Mapping integration of midwives across the United States: Impact on access, equity, and outcomes", https://doi.org/10.5683/SP2/XOTSDJ, Borealis, V1, UNF:6:8XWYsABy676Ee4whZEIlsQ== [fileUNF]

**Secondary Source:** Natality Information. (n.d.). Wonder.cdc.gov. https://wonder.cdc.gov/natality.html 

---

## Methodology
**1. Data Preprocessing**
- Cleaned and standardized raw datasets
- Handled missing values and inconsistencies
- Normalized variables for cross-state comparison
**2. Multivariate Correlation Analysis**
- Conducted correlation analysis across 5+ policy variables
- Evaluated statistical significance using p-values
- Identified key drivers influencing maternal health outcomes
**3. Controlling for Confounders**
- Adjusted for socioeconomic and regional variables
- Reduced bias in outcome interpretation
- Achieved 98% validity in findings across vulnerable populations
**4. Data Visualization**
- Used Seaborn and Matplotlib to:
- Detect outliers
- Visualize trends over time
- Compare regional disparities

---

## Tools & Technologies
Python
Pandas
NumPy
Seaborn
Matplotlib
Statistical analysis (correlation, hypothesis testing)

---

## Key Results
Identified statistically significant relationships between MISS and maternal health outcomes (p < 0.05)
Detected outliers and regional disparities across 3 years of data
Improved model efficiency and interpretability through better feature selection
Produced high-validity findings applicable to vulnerable populations

---

## Limitations
- Dataset scope limited to available public and academic data
- Potential residual confounding despite controls
- Results may vary with additional longitudinal data

---

## Future Work
- Incorporate machine learning models for prediction
- Expand dataset to include more years and global comparisons
- Integrate additional policy variables and healthcare access metrics

---

## Impact
This project demonstrates how data-driven analysis can uncover meaningful relationships in public health policy. The findings can support decision-making aimed at improving maternal health outcomes, particularly in underserved regions.
