# ============================================================
# TECH STACK RECOMMENDER
# A Beginner-Level Content-Based Recommendation System
# ============================================================


# ------------------------------------------------------------
# STEP 1: Import the required libraries
# ------------------------------------------------------------

# pandas is used to read and work with the CSV file
import pandas as pd

# TfidfVectorizer converts text into numerical vectors
from sklearn.feature_extraction.text import TfidfVectorizer

# cosine_similarity calculates how similar two vectors are
from sklearn.metrics.pairwise import cosine_similarity


# ------------------------------------------------------------
# STEP 2: Load the CSV file
# ------------------------------------------------------------

# Read the raw_skills.csv file
data = pd.read_csv("raw_skills.csv")

# Display a message to confirm that the file was loaded
print("CSV file loaded successfully!")

# Display the available job roles
print("\nAvailable Job Roles:")
print(data["job_role"].to_string(index=False))


# ------------------------------------------------------------
# STEP 3: Take 3 skills from the user
# ------------------------------------------------------------

print("\nEnter your 3 skills.")
print("Example: Python, SQL, Machine Learning")

# Ask the user for the first skill
skill1 = input("Skill 1: ").lower().strip()

# Ask the user for the second skill
skill2 = input("Skill 2: ").lower().strip()

# Ask the user for the third skill
skill3 = input("Skill 3: ").lower().strip()


# ------------------------------------------------------------
# STEP 4: Create the user's skill profile
# ------------------------------------------------------------

# Combine the three skills into one text string
user_profile = skill1 + " " + skill2 + " " + skill3


# ------------------------------------------------------------
# STEP 5: Prepare all text for TF-IDF
# ------------------------------------------------------------

# Get the skills column from the CSV file
job_skills = data["skills"].fillna("").astype(str)

# Add the user's skills to the job skills
# This allows TF-IDF to use the same vocabulary
all_text = list(job_skills) + [user_profile]


# ------------------------------------------------------------
# STEP 6: Convert skills into TF-IDF vectors
# ------------------------------------------------------------

# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert all skill text into numerical TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(all_text)


# ------------------------------------------------------------
# STEP 7: Separate job vectors and user vector
# ------------------------------------------------------------

# All rows except the last one belong to job roles
job_vectors = tfidf_matrix[:-1]

# The last row belongs to the user's skill profile
user_vector = tfidf_matrix[-1]


# ------------------------------------------------------------
# STEP 8: Calculate Cosine Similarity
# ------------------------------------------------------------

# Compare the user's skills with every job role
similarity_scores = cosine_similarity(
    user_vector,
    job_vectors
).flatten()


# ------------------------------------------------------------
# STEP 9: Add similarity scores to the data
# ------------------------------------------------------------

# Convert similarity scores into percentages
data["match_percentage"] = similarity_scores * 100


# ------------------------------------------------------------
# STEP 10: Sort recommendations
# ------------------------------------------------------------

# Sort job roles from highest match to lowest match
data = data.sort_values(
    by="match_percentage",
    ascending=False
)


# ------------------------------------------------------------
# STEP 11: Select the Top 3 recommendations
# ------------------------------------------------------------

# Select the first three job roles
top_3 = data.head(3)


# ------------------------------------------------------------
# STEP 12: Display the results
# ------------------------------------------------------------

print("\n==========================================")
print("      TOP 3 JOB ROLE RECOMMENDATIONS")
print("==========================================")

# Display each recommended job role
for index, row in top_3.iterrows():

    # Print the job role
    print("\nJob Role:", row["job_role"])

    # Print the match percentage rounded to 2 decimal places
    print("Match:", round(row["match_percentage"], 2), "%")


# ------------------------------------------------------------
# STEP 13: Finish the program
# ------------------------------------------------------------

print("\nRecommendation process completed!")