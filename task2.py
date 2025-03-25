# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean
print("\nMean petal length by species:")
print(df.groupby('species')['petal length (cm)'].mean())

# Interesting findings
print("\nInteresting findings:")
print("- Setosa has the smallest petals.")
print("- Virginica has the longest petals.")