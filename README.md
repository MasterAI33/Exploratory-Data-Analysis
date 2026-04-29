# Penguin Body Dimensions in Relation to Inhabiting Island

## Overview

This repository contains an exploratory data analysis (EDA) project investigating **how the body dimensions of juvenile, female Adelie penguins vary depending on the island they inhabit**. The analysis was part of a Big Data Bootcamp project.

## Project Motivation

**Research Question:**
How do the island and health metrics of a juvenile, female, Adelie species penguin affect its body dimensions (bill length, bill depth, flipper length, body mass)?

**Why it Matters:**  
Understanding environmental effects on penguin size can help researchers target interventions to improve survival. This is especially important, as 9 out of 18 penguin species are currently endangered or vulnerable.

## Dataset
- **Name:** Palmer Penguins Dataset (Extended)
- **Source:** [Link in project materials]
- **Description:** Each row represents the metrics for a juvenile, female Adelie penguin.  
- **Preprocessing:**
  - Filtered to only *Adelie* species, *female* sex, *juvenile* age.
  - Excluded unused variables (e.g., year, food) to focus on core analyses.
    - Food is considered an affecting variable and will be used to make further inferences after a general idea is established

## Data Cleaning
- Reduced the initial dataset to include only relevant rows: juvenile, female, Adelie penguins (final N = 360).
- Removed unused columns for clarity and reliability.

## Visualizations & Analyses
- **Bill Length vs Island:** Minor differences observed. The Dream island showed an anomaly, likely due to dataset inaccuracy.
- **Bill Depth vs Island:** Little or no difference between islands.
- **Flipper Length vs Island:** Flipper lengths are similar across islands.
- **Body Mass vs Island:** Minimal difference in body weights between islands.

## Hypothesis Testing
- **Approach:**  
  Used A/B testing with shuffling to compare mean differences of body dimensions between islands (primarily Biscoe vs Torgensen).
- **Example Test:**  
  - Variable: Bill length (mm)
  - Population: Juvenile, female Adelie penguins from Biscoe and Torgensen
  - Result:  
    - P-value = 0.7128 (not statistically significant)
    - Conclusion: **Fail to reject the null hypothesis**; the inhabitant island shows minimal effect on bill length.

## Conclusion
- The island of residence has **little to no correlation** with the body dimensions of juvenile, female Adelie penguins in this dataset.
- The hypothesis that islands significantly impact penguin size was **not supported**.
- Some data limitations led to anomalies, and further hypothesis testing on all metrics/islands would strengthen the analysis.
- Suggests more specific environmental or biological factors may play a bigger role.

## Further Work
- In the future, hypothesis tests that span across all three variables will be conducted (e.g ANOVA Testing)
- The dataset will be compared to real-world experimental data to analyze its accuracy better

## Acknowledgements
- Authors of the Palmer Penguin Dataset Extended (attached in materials)
