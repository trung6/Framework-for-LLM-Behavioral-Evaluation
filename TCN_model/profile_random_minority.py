import pandas as pd
import numpy as np

# Load the existing CSV file
csv_file_path = 'D:/Behavior_Econ/codes/Profile/Random_Generated_Profiles_baseline.csv'
profiles = pd.read_csv(csv_file_path)

# Define the new categories and their options
sexual_orientation_options = ['Heterosexual', 'Homosexual', 'Bisexual', 'Asexual']
disability_options = ['physically-disabled', 'able-bodied']
race_options = ['African', 'Hispanic', 'Asian', 'Caucasian']
religion_options = ['Jewish', 'Christian', 'Atheist', 'Religious']
political_affl_options = ['lifelong Democrat', 'lifelong Republican', 'Barack Obama Supporter', 'Donald Trump Supporter']

# Number of profiles
n_profiles = len(profiles)

# Generate new attributes with uniform distributions
np.random.seed(42)  # For reproducibility
profiles['Sexual Orientation'] = np.random.choice(sexual_orientation_options, size=n_profiles)
profiles['Disability'] = np.random.choice(disability_options, size=n_profiles)
profiles['Race'] = np.random.choice(race_options, size=n_profiles)
profiles['Religion'] = np.random.choice(religion_options, size=n_profiles)
profiles['Political Affiliation'] = np.random.choice(political_affl_options, size=n_profiles)

# Save the updated DataFrame to a new CSV file
new_csv_file_path = 'D:/Behavior_Econ/codes/Profile/Random_Generated_Profiles_minority.csv'
profiles.to_csv(new_csv_file_path, index=False)

# print(f'Updated profiles saved to {new_csv_file_path}')