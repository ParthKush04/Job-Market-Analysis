import pandas as pd

df = pd.read_csv("data/jobs.csv")

# Drop completely empty columns
df = df.drop(columns=['work_type', 'employment_type'])

print("\nColumns after dropping empty ones:")
print(df.columns)

# Drop rows where critical fields are missing
df = df.dropna(subset=['company', 'location', 'description'])

print("\nMissing values AFTER dropping critical rows:")
print(df.isnull().sum())

print("\nTotal rows after cleaning:", len(df))

# Define important technical skills to search for
skills_list = [
    "python", "sql", "excel", "tableau", "power bi",
    "machine learning", "deep learning", "nlp",
    "react", "node", "aws", "azure",
    "pandas", "numpy", "tensorflow", "pytorch"
]

# Convert descriptions to lowercase
df['description'] = df['description'].str.lower()

from collections import Counter

skill_counter = Counter()

for description in df['description']:
    for skill in skills_list:
        if skill in description:
            skill_counter[skill] += 1

print("\nSkill Frequency:")
print(skill_counter)


# Convert counter to DataFrame
skills_df = pd.DataFrame(skill_counter.items(), columns=['Skill', 'Count'])

# Sort descending
skills_df = skills_df.sort_values(by='Count', ascending=False)

print("\nTop Skills:")
print(skills_df.head(10))

# Top 10 job locations
location_counts = df['location'].value_counts().head(10)

print("\nTop 10 Job Locations:")
print(location_counts)

# Extract country (last part after comma)
df['country'] = df['location'].apply(lambda x: x.split(",")[-1].strip())

country_counts = df['country'].value_counts().head(10)

# Clean country names

def clean_country(x):
    x = x.strip()

    # If contains United States or US
    if "United States" in x or x == "US":
        return "United States"

    # If it's a 2-letter uppercase code (likely US state)
    if len(x) == 2 and x.isupper():
        return "United States"

    # Remove obvious garbage
    if "*" in x or x.lower() == "unknown":
        return "Unknown"

    return x



df['country'] = df['country'].apply(clean_country)

country_counts = df['country'].value_counts().head(10)

print("\nTop 10 Countries AFTER cleaning:")
print(country_counts)

title_counts = df['title'].value_counts().head(10)

print("\nTop 10 Job Titles:")
print(title_counts)


import matplotlib.pyplot as plt


top_countries = df['country'].value_counts().head(10)

plt.figure()
plt.bar(top_countries.index, top_countries.values)

plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("Number of Job Postings")
plt.title("Top Hiring Countries")

plt.tight_layout()
plt.show()

# Plot top 10 skills
top_10 = skills_df.head(10)

plt.figure()
plt.bar(top_10['Skill'], top_10['Count'])

plt.xticks(rotation=45)
plt.xlabel("Skills")
plt.ylabel("Demand Count")
plt.title("Top 10 Most In-Demand Skills")

plt.tight_layout()
plt.show()


print("\n===== INSIGHT SUMMARY =====")
print("1. SQL and Python are the most in-demand technical skills.")
print("2. Excel remains highly relevant in analytics roles.")
print("3. The United States dominates job postings in this dataset.")
print("4. Machine Learning and Cloud (AWS/Azure) skills are increasingly important.")


skills_df.to_csv("top_skills_output.csv", index=False)
top_countries.to_csv("top_countries_output.csv")
