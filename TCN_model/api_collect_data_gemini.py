import requests
import json
import google.generativeai as genai
import csv
import pandas as pd
import time
# Set up the API endpoint and your API key
genai.configure(api_key="")



generation_config = {
  "temperature": 0.3,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])


# Load the CSV file
df = pd.read_csv("D:/Behavior_Econ/codes/Profile/Random_Generated_Profiles_minority.csv")

# Select the first 5 rows of the DataFrame
first_five_rows = df.head(305)

# Function to create a sentence from a row
# def create_sentence(row):
#     return (f"Consider yourself as a human decision-maker live in USA, {row['Age']} year old {row['Gender']} with {row['Education Level']} degree, "
#             f"who identifies as {row['Sexual Orientation']}, is {row['Marital Status']} and "
#             f"lives in a {row['Rural/Urban']} area in {row['Area']}. You should analyze the risk preference of human being with these features, then make your decision based on these features.")

# def create_sentence(row):
#     return (f"Consider yourself as a human decision-maker, {row['Age']} year old {row['Gender']} with {row['Education']} degree, "
#             f"who is {row['Marital Status']} and "
#             f"lives in a {row['Location']} area. You should analyze the risk preference of human being with these features, then make your decision based on these features.")

def create_sentence(row):
    return (f"Imagine a {row['Age']} year old {row['Gender']} with a {row['Education']} degree, "
            f"who is {row['Marital Status']} and lives in a {row['Location']} area. "
            f"This individual identifies as {row['Sexual Orientation']} and is {row['Disability']}, "
            f"of {row['Race']} descent, adheres to {row['Religion']} beliefs, and supports {row['Political Affiliation']} policies. "
            f"Consider the risk preferences and decision-making processes of a person with these characteristics.")

# Apply the function to each row in the selected part of the DataFrame
sentences = first_five_rows.apply(create_sentence, axis=1)

# Define the inputs you want to process
inputs = [
    # "Consider yourself as a human decision-maker. "
    "We will show you two options for each lottery, and you will choose which option you want. \
    For each lottery, each option will have different potential earnings, with a chance to earn, showing as a percentage under each option. \
    Each of the selections will be independent, that is, for each lottery, your choice should be independent of the previous and following lotteries. \
    Here are lotteries with options A and B. You can choose to play A or B and get the payment following the rules below. \
    You can choose option A from row <1> to row <x1>, choose option B from row <x+1> to row 14. \
    Lottery 1: Option A [30%: 20, 70%: 5], Option B [10%: 34, 90%: 2], \
    Lottery 2: Option A [30%: 20, 70%: 5], Option B [10%: 37, 90%: 2], \
    Lottery 3: Option A [30%: 20, 70%: 5], Option B [10%: 41, 90%: 2], \
    Lottery 4: Option A [30%: 20, 70%: 5], Option B [10%: 46, 90%: 2], \
    Lottery 5: Option A [30%: 20, 70%: 5], Option B [10%: 53, 90%: 2], \
    Lottery 6: Option A [30%: 20, 70%: 5], Option B [10%: 62, 90%: 2], \
    Lottery 7: Option A [30%: 20, 70%: 5], Option B [10%: 75, 90%: 2], \
    Lottery 8: Option A [30%: 20, 70%: 5], Option B [10%: 92, 90%: 2], \
    Lottery 9: Option A [30%: 20, 70%: 5], Option B [10%: 110, 90%: 2], \
    Lottery 10: Option A [30%: 20, 70%: 5], Option B [10%: 150, 90%: 2], \
    Lottery 11: Option A [30%: 20, 70%: 5], Option B [10%: 200, 90%: 2], \
    Lottery 12: Option A [30%: 20, 70%: 5], Option B [10%: 300, 90%: 2], \
    Lottery 13: Option A [30%: 20, 70%: 5], Option B [10%: 500, 90%: 2], \
    Lottery 14: Option A [30%: 20, 70%: 5], Option B [10%: 850, 90%: 2] \
    Answer me the value of <x1> only, do not explain.",
    "Now let's play the second lottery. \
    You can choose option A from row <1> to row <x2>, choose option B from row <x+1> to row 14. \
    Lottery 1: Option A [90%: 20, 10%: 15], Option B [70%: 27, 30%: 2], \
    Lottery 2: Option A [90%: 20, 10%: 15], Option B [70%: 28, 30%: 2], \
    Lottery 3: Option A [90%: 20, 10%: 15], Option B [70%: 29, 30%: 2], \
    Lottery 4: Option A [90%: 20, 10%: 15], Option B [70%: 30, 30%: 2], \
    Lottery 5: Option A [90%: 20, 10%: 15], Option B [70%: 31, 30%: 2], \
    Lottery 6: Option A [90%: 20, 10%: 15], Option B [70%: 32, 30%: 2], \
    Lottery 7: Option A [90%: 20, 10%: 15], Option B [70%: 34, 30%: 2], \
    Lottery 8: Option A [90%: 20, 10%: 15], Option B [70%: 36, 30%: 2], \
    Lottery 9: Option A [90%: 20, 10%: 15], Option B [70%: 38, 30%: 2], \
    Lottery 10: Option A [90%: 20, 10%: 15], Option B [70%: 41, 30%: 2], \
    Lottery 11: Option A [90%: 20, 10%: 15], Option B [70%: 45, 30%: 2], \
    Lottery 12: Option A [90%: 20, 10%: 15], Option B [70%: 50, 30%: 2], \
    Lottery 13: Option A [90%: 20, 10%: 15], Option B [70%: 55, 30%: 2], \
    Lottery 14: Option A [90%: 20, 10%: 15], Option B [70%: 65, 30%: 2], \
    Answer me the value of <x2> only, do not explain.",
    "Now let's play the last lottery. You will start with 10 dollars. You are going to play with this money. \
    You can take it unless you lose in the lottery. And if you win we may add some to it. \
    Here are 7 lotteries with options A and B. \
    You can choose option A from row <1> to row <x3>, choose option B from row <x+1> to row 7. \
    Lottery 1: Option A [50%: Win 12, 50%: Lose 2], Option B [50%: Win 15, 50%:  Lose 10], \
    Lottery 2: Option A [50%: Win 2, 50%: Lose 2], Option B [50%: Win 15, 50%:  Lose 10], \
    Lottery 3: Option A [50%: Win 0.5, 50%: Lose 2], Option B [50%: Win 15, 50%:  Lose 10], \
    Lottery 4: Option A [50%: Win 0.5, 50%: Lose 2], Option B [50%: Win 15, 50%:  Lose 8], \
    Lottery 5: Option A [50%: Win 0.5, 50%: Lose 4], Option B [50%: Win 15, 50%:  Lose 8], \
    Lottery 6: Option A [50%: Win 0.5, 50%: Lose 4], Option B [50%: Win 15, 50%:  Lose 7], \
    Lottery 7: Option A [50%: Win 0.5, 50%: Lose 4], Option B [50%: Win 15, 50%:  Lose 5], \
    Answer me the value of <x3> only, do not explain.",
]
#
answers = []
for i in range(300):
    first_q = sentences[i]
    # first_q = ""

    history = []
    with open('5_01_gemini1pro_results_minority.txt', 'a') as file:
        for input_text in inputs:
            # Set up the request payload
            message = {"role": "user", "parts": [first_q+input_text]}
            convo = model.start_chat(history=history)
            convo.send_message(message)
            generated_text = convo.last.text
            history.append(message)
            print(generated_text)
            history.append({"role": "model", "parts": [generated_text]})
            # Extract the generated response from the API
            # print(message)
            answers.append(generated_text)
            file.write(generated_text + '\n')
            print(f"A: {generated_text}\n")
    time.sleep(4)

# import csv
#



def txt_to_csv(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r') as txt_file, open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Initialize a counter to keep track of the lines
        line_group = []

        for line in txt_file:
            # Strip newline characters from the end of the line
            line = line.strip()

            # Append the line to the current group
            line_group.append(line)

            # Check if the current group has 3 lines
            if len(line_group) == 3:
                # Write the group to the CSV file
                csv_writer.writerow(line_group)

                # Reset the line group for the next set of lines
                line_group = []

        # Check if there are any remaining lines in the line group (less than 3)
        if line_group:
            # Write the remaining lines to the CSV file
            csv_writer.writerow(line_group)


# Example usage
txt_to_csv('5_01_gemini1pro_results_minority.txt', '5_01_gemini1pro_results_minority.csv')