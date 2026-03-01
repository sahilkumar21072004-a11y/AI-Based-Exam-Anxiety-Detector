import pandas as pd

# Load dataset
df = pd.read_csv("data/anxiety_dataset.csv")

print("Dataset Loaded Successfully")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nClass Distribution:")
print(df["status"].value_counts())
import matplotlib.pyplot as plt

df["status"].value_counts().plot(kind="bar")
plt.title("Class Distribution")
plt.show()