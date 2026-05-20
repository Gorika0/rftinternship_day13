import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75,
         78, 80, 82, 85, 88, 90, 92, 95, 97, 100]

df = pd.DataFrame({"Marks": marks})
print(df)

plt.figure(figsize=(8,5))
sns.histplot(df["Marks"], bins=8, kde=True)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
print("Skewness of data:", df["Marks"].skew())
