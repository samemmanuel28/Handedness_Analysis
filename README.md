# Handedness_Analysis
## Refuting the myth that Left-Handed people die sooner, using Python and R
This repository contains the Python and R code, along with the data, used for a data analysis project aimed at re-examining the claim that left-handed individuals have a shorter average lifespan than right-handed individuals. The analysis applies Bayesian statistical methods to demonstrate that any observed differences in age at death can be attributed to historical and sociocultural changes in the prevalence of left-handedness over time, rather than an intrinsic biological factor.

## Project Goal
The primary objective of this project was to:
Investigate the widely discussed claim regarding a shorter lifespan for left-handed individuals.
Determine if observed differences in age at death could be explained by factors like historical bias and changing societal norms related to handedness.

## Methodology
The core of this project's methodology involves Bayesian inference to calculate the probability of being a certain age at death given an individual's handedness. This approach accounts for the dynamic prevalence of left-handedness across different birth years.

## Key functions implemented in the code include:
* P_lh_given_A: Estimates the probability of an individual being left-handed at a given age, considering historical trends in handedness prevalence.
* P_lh: Calculates the overall probability of left-handedness within the study population for a specific year.
* P_A_given_lh: Applies Bayes' Theorem to determine the probability distribution of age at death for left-handed individuals.
* P_A_given_rh: Applies Bayes' Theorem to determine the probability distribution of age at death for right-handed individuals.
These functions integrate concepts of age distribution, historical handedness rates, and conditional probabilities to derive insights.

## Code and Data Structure
The repository is organized as follows:
* Analysis.py: The main Python script containing the Bayesian analytical functions, data loading, and initial processing.
* Viz.R: The R script used for generating various data visualizations and performing some data preparation specific to plotting.
* LH_Data.csv: Dataset containing left-handedness rates by age and gender. This data is used to model historical changes in handedness prevalence.
* DD_Data.csv: Dataset containing death distribution data (number of deaths by age for both sexes). This data provides the general population's age-at-death distribution.
* bayes_probabilities_1990.csv: Intermediate output from Python, containing calculated Bayesian probabilities for the 1990 study year, used by the R script.
* bayes_probabilities_2018.csv: Intermediate output from Python, containing calculated Bayesian probabilities for the 2018 study year, used by the R script.
* cleaned_lh_data.csv: Intermediate output from Python, a cleaned version of LH_Data.csv used by the R script.
* cleaned_death_distribution.csv: Intermediate output from Python, a cleaned version of DD_Data.csv used by the R script.
* README.md: This file, providing an overview of the project.
* Visualizations/: A directory to store generated plots.

## How to Run the Code
To run this analysis and reproduce the results and visualizations:
1. Clone the Repository
2. Install Python Dependencies
3. Install R and RStudio
4. Install R Packages
5. Execute the Python Script
6. Execute the R Script

## Results
The analysis demonstrated that the observed difference in average age at death between left- and right-handed individuals significantly diminishes when historical shifts in handedness prevalence are accounted for. This suggests that the apparent discrepancy in earlier studies was likely a statistical artifact rather than a biological reality.

* In a 1990 context, an apparent average age difference of approximately 5.6 years was observed, with right-handers appearing to live longer.
* In a 2018 context, this difference was virtually eliminated (approximately 0.3 years), showing a strong convergence of average lifespans, supporting the hypothesis that sociocultural factors explain the historical observation.
