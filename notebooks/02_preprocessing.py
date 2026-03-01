import pandas as pd

df = pd.read_csv("data/anxiety_dataset.csv")

# Check missing values
print(df.isnull().sum())

# Remove missing text rows (if any)
df = df.dropna(subset=["statement"])

print("After removing missing values:")
print(df.isnull().sum())
print("Unique Original Labels:")
print(df["status"].unique())

print("\nLabel Distribution:")
print(df["status"].value_counts())
label_mapping = {
    "Normal": "Low",
    "Anxiety": "Moderate",
    "Stress": "Moderate",
    "Depression": "High",
    "Suicidal": "High",
    "Bipolar": "High",
    "Personality disorder": "High"
}

df["anxiety_level"] = df["status"].map(label_mapping)

print(df[["status", "anxiety_level"]].head())
numerical_mapping = {
    "Low": 0,
    "Moderate": 1,
    "High": 2
}

df["label"] = df["anxiety_level"].map(numerical_mapping)

print(df[["anxiety_level", "label"]].head())
print("New Anxiety Level Distribution:")
print(df["anxiety_level"].value_counts())

print("\nNumerical Label Distribution:")
print(df["label"].value_counts())

print("\nCheck for unmapped values:")
print(df[df["label"].isnull()])
# Keep only required columns
final_df = df[["statement", "label"]]

# Save cleaned dataset
final_df.to_csv("data/cleaned_anxiety_dataset.csv", index=False)

print("Final dataset saved successfully!")