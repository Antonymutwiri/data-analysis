import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]  # Add species column

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check data types & missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Clean data (drop missing values if any)
df.dropna(inplace=True)
print("\nData cleaned (missing values dropped if any).")