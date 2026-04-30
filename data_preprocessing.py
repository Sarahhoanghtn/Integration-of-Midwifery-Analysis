# Name: Sarah Hoang
# Date: April 16, 2026
# Program: data_preprocessing.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = None
with open('US_Mapping_DATA_FINAL_Dec_5_2017.csv', 'r') as file:
    df = pd.read_csv(file, encoding="cp1252")
    df.columns = df.columns.str.replace('ï»¿', '')

# Load confounding data
confounding_df = pd.read_excel('Natality, 2007-2024.csv.xlsx', engine='openpyxl')
confounding_df = confounding_df.drop(columns='Notes')
confounding_df = confounding_df.dropna(how='all')

# Synchronize state names
def match_state(state_value):
    us_state_codes = {
        "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA", "Colorado": "CO",
        "Connecticut": "CT", "Delaware": "DE", "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA",
        "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
        "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA",
        "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
        "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
        "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
        "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD",
        "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
        "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
    }

    state_names = list(us_state_codes.keys())

    if not isinstance(state_value, str):
        return None

    state_value = state_value.strip().lower()

    for full_state in state_names:
        if full_state.lower().startswith(state_value):
            return us_state_codes[full_state]

    return None

# Replace state names with state codes
df["State"] = df["State"].fillna("").apply(match_state)
confounding_df["State"] = confounding_df["State"].fillna("").apply(match_state)

# Merge databases
full_df = df[['State', 'Integration_scores','CS', 
       'Preterm', 'Induction', 'Percent_black_births', 
       'CPM_Licensure', 'CM_Licensure', 'All_midwives_home_birthing_center_ACCESS',
       'All_midwives_hospital_births_ACCESS',
       'All_midwives_all_locations_ACCESS', 'CNM_CM_per_1000_births_DENSITY',
       'CPM_per_1000_births_DENSITY', 'All_types_midwives_DENSITY']].copy()

# Add columns for confounding variables
full_df['Average_maternal_age'] = None
full_df['Pct_total_births'] = None
full_df['Maternal_educational_level'] = None

#
confounding_df['Mother\'s Education Code'] = pd.to_numeric(confounding_df['Mother\'s Education Code'], errors='coerce')
confounding_df = confounding_df.dropna(subset=['Mother\'s Education Code'])

states = full_df['State'].unique()
for state in states:
    curr_values = confounding_df[confounding_df['State'] == state]
    avg_mat_age = round(curr_values['Average Age of Mother'].mean(), 2)
    pct_births = round(100.0 * sum(curr_values['% of Total Births']), 2)

    
    educational_levels = confounding_df['Mother\'s Education Code'].unique()
    weighted_sum = 0.0
    for level in educational_levels:
        weighted_sum += level * 100.0 * sum(curr_values[curr_values['Mother\'s Education Code'] == level]['% of Total Births'])
    weighted_sum /= pct_births

    full_df.loc[full_df["State"] == state, "Average_maternal_age"] = avg_mat_age
    full_df.loc[full_df["State"] == state, "Pct_total_births"] = pct_births
    full_df.loc[full_df["State"] == state, "Maternal_educational_level"] = weighted_sum

## Add rankings
full_df['Integration_Rank'] = full_df['Integration_scores'].rank(ascending=False)
full_df['Cesarean_Rank'] = full_df['CS'].rank(ascending=False)
full_df['Induction_Rank'] = full_df['Induction'].rank(ascending=False)
full_df['Preterm_Rank'] = full_df['Preterm'].rank(ascending=False)

full_df['Average_maternal_age_rank']= full_df['Average_maternal_age'].rank(ascending=False)
full_df['Maternal_educational_level_rank']= full_df['Maternal_educational_level'].rank(ascending=False)

full_df["Average_maternal_age"] = pd.to_numeric(full_df["Average_maternal_age"], errors='coerce')
full_df["Maternal_educational_level"] = pd.to_numeric(full_df["Maternal_educational_level"], errors='coerce')

# NOTE: pct_births doesn't add up to 100%

