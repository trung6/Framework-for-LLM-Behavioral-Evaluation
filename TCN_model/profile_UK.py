import numpy as np
import pandas as pd

# Number of profiles to generate
n_profiles = 305

# Probability distributions for each attribute
gender_distribution = ['Male', 'Female']
gender_probabilities = [0.4945, 0.5055]

education_levels = ['Below lower secondary', 'Lower secondary', 'Upper secondary',
                    'Short-cycle tertiary', 'Bachelor', 'Graduate']
education_probabilities = [0.002, 0.1989, 0.3267, 0.0996, 0.237, 0.1358]

marital_status = ['Never married', 'Married', 'Widowed', 'Divorced']
marital_probabilities = [0.379, 0.469, 0.061, 0.091]  # Adjusted probabilities to sum to 1

location_type = ['Rural', 'Urban']
location_probabilities = [0.156, 0.844]

age_groups = ['15 to 24', '25 to 34', '35 to 44', '45 to 54', '55 to 64', 'Over 65']
age_probabilities = [0.1149 / 0.8237, 0.1352 / 0.8237, 0.1343 / 0.8237,
                     0.1308 / 0.8237, 0.1237 / 0.8237, 0.1848 / 0.8237]  # Adjusted for ages over 15

# List to store generated profiles
profiles_list = []

# Continue generating until we have 300 valid profiles
while len(profiles_list) < n_profiles:
    np.random.seed()  # Remove seed for production to ensure randomness
    batch_size = n_profiles - len(profiles_list)
    genders = np.random.choice(gender_distribution, p=gender_probabilities, size=batch_size)
    educations = np.random.choice(education_levels, p=education_probabilities, size=batch_size)
    maritals = np.random.choice(marital_status, p=marital_probabilities, size=batch_size)
    locations = np.random.choice(location_type, p=location_probabilities, size=batch_size)
    ages = np.random.choice(age_groups, p=age_probabilities, size=batch_size)

    # Create DataFrame for the batch
    batch_profiles = pd.DataFrame({
        'Age': ages,
        'Gender': genders,
        'Education': educations,
        'Marital Status': maritals,
        'Location': locations
    })

    # Append valid profiles to the list
    profiles_list.extend(batch_profiles.values)

# Convert list to DataFrame
profiles = pd.DataFrame(profiles_list, columns=['Age', 'Gender', 'Education', 'Marital Status', 'Location'])


csv_file_path = 'D:/Behavior_Econ/codes/UK_Generated_Profiles_baseline.csv'
profiles.to_csv(csv_file_path, index=False)
# print(profiles.head())