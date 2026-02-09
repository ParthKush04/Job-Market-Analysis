# Job-Market-Analysis
This project analyzes over 1,000 real-world job postings to uncover trends in technical skill demand and geographic hiring patterns. Using Python and data analysis techniques, the project extracts insights from raw job descriptions and transforms unstructured data into meaningful, business-level conclusions.

The objective was to independently clean, process, and analyze a messy dataset to identify:

1.Most in-demand technical skills

2.Top hiring countries

3.Most common job roles

Overall hiring trends in the data market

🧠 Problem Statement

Job postings often contain unstructured and inconsistent data. Locations may be listed as states, countries, abbreviations, or contain invalid characters. Skills are embedded inside long text descriptions rather than structured columns.

This project demonstrates how to:

1.Clean incomplete and inconsistent data

2.Normalize location values

3.Extract technical skills from text descriptions

4.Generate meaningful insights from raw data

🛠️ Technologies Used

* Python

* Pandas

* Matplotlib

* Collections (Counter)

CSV export for result storage

🔍 Key Steps in the Analysis
1️⃣ Data Cleaning

* Removed completely empty columns

* Dropped rows with critical missing fields (company, location, description)

* Standardized country names and mapped US state abbreviations to “United States”

* Handled corrupted entries (e.g., symbols like *****)

2️⃣ Skill Extraction

* Defined a list of technical skills

* Converted job descriptions to lowercase

* Scanned each description to detect skill occurrences

* Counted and ranked skill frequency

3️⃣ Location Normalization

* Extracted country information from messy location strings

* Implemented a custom cleaning function to standardize values

* Consolidated US states under “United States”

4️⃣ Visualization

* Created bar charts for:

* Top 10 most in-demand skills

* Top hiring countries

* Exported cleaned results to CSV files

📈 Key Insights

* SQL and Python are the most demanded skills.

* Excel remains highly relevant in analytics roles.

* The United States dominates hiring in the dataset.

* Cloud technologies like AWS and Azure show significant demand.

Machine Learning skills are increasingly required.

🚀 Output Files

* The project generates:

* top_skills_output.csv

* top_countries_output.csv

These contain structured results ready for dashboard integration or further analysis.

💡 What This Project Demonstrates

* Independent dataset analysis

* Handling messy, real-world data

* Data normalization and preprocessing

* Text-based skill extraction

Insight generation for non-technical audiences

Clear analytical thinking and structured problem solving
