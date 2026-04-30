# Name: Sarah Hoang
# Date: April 16, 2026
# Program: analysis.py

## import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

from data_preprocessing import full_df

# DESCRIPTIVE STATISTICS

## Integration Scores
print(full_df['Integration_scores'].describe())

print('State with highest integration score:', full_df.loc[
    full_df["Integration_scores"] == full_df["Integration_scores"].max(), "State"
].iloc[0])

print('State with lowest integration score:', full_df.loc[
    full_df["Integration_scores"] == full_df["Integration_scores"].min(), "State"
].iloc[0])

## Cesarean rate
print(full_df['CS'].describe())

print('State with highest c-section rate:', full_df.loc[
    full_df["CS"] == full_df["CS"].max(), "State"
].iloc[0])

print('State with lowest c-section rate:', full_df.loc[
    full_df["CS"] == full_df["CS"].min(), "State"
].iloc[0])

### FIGURE 1.2
m, b = np.polyfit(full_df["CS"], full_df["Integration_scores"], 1)

x_line = np.linspace(min(full_df["CS"]), max(full_df["CS"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='CS', y='Integration_scores')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Cesarean Rate (%)")
scatter.set_ylabel("Integration Scores")
scatter.set_title("Relationship between Integration Scores and Cesarean Rate across the USA")

plt.show()

### Pearson's Correlation
print(full_df["CS"].corr(full_df["Integration_scores"], method="pearson"))

## Induction rate
print(full_df['Induction'].describe())

print('State with highest induction rate:', full_df.loc[
    full_df["Induction"] == full_df["Induction"].max(), "State"
].iloc[0])

print('State with lowest induction rate:', full_df.loc[
    full_df["Induction"] == full_df["Induction"].min(), "State"
].iloc[0])

### FIGURE 1.4
m, b = np.polyfit(full_df["Induction"], full_df["Integration_scores"], 1)

x_line = np.linspace(min(full_df["Induction"]), max(full_df["Induction"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Induction', y='Integration_scores')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Induction Rate (%)")
scatter.set_ylabel("Integration Scores")
scatter.set_title("Relationship between Integration Scores and Induction Rate across the USA")

plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Induction"], full_df["Integration_scores"])
print("corr:", corr, "\np-value:", p_value)

## Preterm rate
print(full_df['Preterm'].describe())

print('State with highest Preterm rate:', full_df.loc[
    full_df["Preterm"] == full_df["Preterm"].max(), "State"
].iloc[0])

print('State with lowest Preterm rate:', full_df.loc[
    full_df["Preterm"] == full_df["Preterm"].min(), "State"
].iloc[0])

### FIGURE 1.6
m, b = np.polyfit(full_df["Preterm"], full_df["Integration_scores"], 1)

x_line = np.linspace(min(full_df["Preterm"]), max(full_df["Preterm"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Preterm', y='Integration_scores')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Preterm Rate (%)")
scatter.set_ylabel("Integration Scores")
scatter.set_title("Relationship between Integration Scores and Preterm Rate across the USA")

plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Preterm"], full_df["Integration_scores"])
print("corr:", corr, "\np-value:", p_value)

# CONFOUNDING VARIABLES

## Average Maternal Age
print(full_df["Average_maternal_age"].describe())

print('State with highest average maternal age:', full_df.loc[
    full_df["Average_maternal_age"] == full_df["Average_maternal_age"].max(), "State"
].iloc[0])

print('State with lowest average maternal age:', full_df.loc[
    full_df["Average_maternal_age"] == full_df["Average_maternal_age"].min(), "State"
].iloc[0])

print(full_df[full_df['State'].isin(['MS', 'NJ'])][['State', 'Average_maternal_age', 'Average_maternal_age_rank']])

### FIGURE 2.1
plt.hist(full_df["Average_maternal_age"], bins=20, edgecolor='black')
plt.title("Distribution of Average Maternal Age")
plt.show()

### FIGURE 2.2
m, b = np.polyfit(full_df["Integration_scores"], full_df["Average_maternal_age"], 1)

x_line = np.linspace(min(full_df["Integration_scores"]), max(full_df["Integration_scores"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Integration_scores', y='Average_maternal_age')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Integration Scores")
scatter.set_ylabel("Average Maternal Age")
scatter.set_title("Relationship between Average Maternal Age and Integration Scores across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Average_maternal_age"], full_df["Integration_scores"])
print("corr:", corr, "\np-value:", p_value)

### FIGURE 2.3
m, b = np.polyfit(full_df["Preterm"], full_df["Average_maternal_age"], 1)

x_line = np.linspace(min(full_df["Preterm"]), max(full_df["Preterm"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Preterm', y='Average_maternal_age')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Preterm Rate (%)")
scatter.set_ylabel("Average Maternal Age")
scatter.set_title("Relationship between Average Maternal Age and Preterm Rate across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Average_maternal_age"], full_df["Preterm"])
print("corr:", corr, "\np-value:", p_value)

### FIGURE 2.4
m, b = np.polyfit(full_df["CS"], full_df["Average_maternal_age"], 1)

x_line = np.linspace(min(full_df["CS"]), max(full_df["CS"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='CS', y='Average_maternal_age')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Cesarean Rate")
scatter.set_ylabel("Average Maternal Age")
scatter.set_title("Relationship between Average Maternal Age and Cesarean Rate across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Average_maternal_age"], full_df["CS"])
print("corr:", corr, "\np-value:", p_value)

### FIGURE 2.5
m, b = np.polyfit(full_df["Induction"], full_df["Average_maternal_age"], 1)

x_line = np.linspace(min(full_df["Induction"]), max(full_df["Induction"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Induction', y='Average_maternal_age')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Induction Rate")
scatter.set_ylabel("Average Maternal Age")
scatter.set_title("Relationship between Average Maternal Age and Induction Rate across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Average_maternal_age"], full_df["Induction"])
print("corr:", corr, "\np-value:", p_value)

## Mother's Educational Level
print(full_df["Maternal_educational_level"].describe())

print('State with highest average maternal age:', full_df.loc[
    full_df["Maternal_educational_level"] == full_df["Maternal_educational_level"].max(), "State"
].iloc[0])

print('State with lowest average maternal age:', full_df.loc[
    full_df["Maternal_educational_level"] == full_df["Maternal_educational_level"].min(), "State"
].iloc[0])

print(full_df[full_df['State'].isin(['MS', 'NJ'])][['State', 'Maternal_educational_level', 'Maternal_educational_level_rank']])

### FIGURE 2.6
plt.hist(full_df["Maternal_educational_level"], bins=20, edgecolor='black')
plt.title("Distribution of Maternal Educational Level")
plt.show()

### FIGURE 2.7
m, b = np.polyfit(full_df["Integration_scores"], full_df["Maternal_educational_level"], 1)

x_line = np.linspace(min(full_df["Integration_scores"]), max(full_df["Integration_scores"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Integration_scores', y='Maternal_educational_level')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Integration Scores")
scatter.set_ylabel("Maternal Educational Level")
scatter.set_title("Relationship between Maternal Educational Level and Integration Scores across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Maternal_educational_level"], full_df["Integration_scores"])
print("corr:", corr, "\np-value:", p_value)

### FIGURE 2.8
m, b = np.polyfit(full_df["Preterm"], full_df["Maternal_educational_level"], 1)

x_line = np.linspace(min(full_df["Preterm"]), max(full_df["Preterm"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Preterm', y='Maternal_educational_level')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Preterm Rate (%)")
scatter.set_ylabel("Maternal Educational Level")
scatter.set_title("Relationship between Maternal Educational Level and Preterm Rate across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Maternal_educational_level"], full_df["Preterm"])
print("corr:", corr, "\np-value:", p_value)

### FIGURE 2.9
m, b = np.polyfit(full_df["CS"], full_df["Maternal_educational_level"], 1)

x_line = np.linspace(min(full_df["CS"]), max(full_df["CS"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='CS', y='Maternal_educational_level')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Cesarean Rate")
scatter.set_ylabel("Maternal Educational Level")
scatter.set_title("Relationship between Maternal Educational Level and Cesarean Rate across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Maternal_educational_level"], full_df["CS"])
print("corr:", corr, "\np-value:", p_value)

### FIGURE 2.10
m, b = np.polyfit(full_df["Induction"], full_df["Maternal_educational_level"], 1)

x_line = np.linspace(min(full_df["Induction"]), max(full_df["Induction"]), 100)
y_line = m * x_line + b

scatter = sns.scatterplot(data=full_df, x='Induction', y='Maternal_educational_level')
scatter.plot(x_line, y_line, color='red', linewidth=2, zorder=1)

scatter.set_xlabel("Induction Rate")
scatter.set_ylabel("Maternal Educational Level")
scatter.set_title("Relationship between Maternal Educational Level and Induction Rate across the USA")
plt.show()

#### Pearson's Correlation & P-Value
corr, p_value = pearsonr(full_df["Maternal_educational_level"], full_df["Induction"])
print("corr:", corr, "\np-value:", p_value)

########################################
