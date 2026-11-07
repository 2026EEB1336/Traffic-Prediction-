import pandas as pd                     
import numpy as np                      
import matplotlib.pyplot as plt       
import seaborn as sns                   

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)
print("Libraries imported successfully!")

df = pd.read_csv("Traffic.csv")
print("Dataset shape (rows, columns):", df.shape)
print()
print("First 5 rows:")
print(df.head())
print()
print("Last 5 rows:")
print(df.tail())

print("Shape:", df.shape)
print()
print("Columns:", df.columns.tolist())
print()
df.info()

print("Missing values in each column:")
print(df.isnull().sum())
print()
print("Number of duplicate rows:", df.duplicated().sum())

print("Summary statistics of the numeric columns:")
print(df.describe())

print()
print("Number of readings for each junction:")
print(df["Junction"].value_counts().sort_index())

# 1. Remove duplicates and missing values
print("Shape before cleaning:", df.shape)
df = df.drop_duplicates()
df = df.dropna()
print("Shape after cleaning :", df.shape)

# 2. Drop the ID column (it is only an identifier)
df = df.drop("ID", axis=1)

# 3. Convert DateTime from text to a proper date-time
df["DateTime"] = pd.to_datetime(df["DateTime"])

# 4. Extract time information
df["Hour"] = df["DateTime"].dt.hour             # 0 - 23
df["DayOfWeek"] = df["DateTime"].dt.dayofweek   # 0 = Monday ... 6 = Sunday
df["Month"] = df["DateTime"].dt.month           # 1 - 12

print()
print(df.head())
print()
df.info()

junction_avg = df.groupby("Junction")["Vehicles"].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(data=junction_avg, x="Junction", y="Vehicles", color="skyblue")
plt.xlabel("Junction Number")
plt.ylabel("Mean Vehicle Count")
plt.title("Comparison of Average Traffic Across Junctions")
plt.show()

hourly_avg = df.groupby(["Hour", "Junction"])["Vehicles"].mean().reset_index()


plt.figure(figsize=(10, 5))
sns.lineplot(
    data=hourly_avg,
    x="Hour",
    y="Vehicles",
    hue="Junction",
    marker="o"
)

plt.xlabel("Time (Hours)")
plt.ylabel("Mean Number of Vehicles")
plt.title("Hourly Traffic Pattern at Different Junctions")
plt.xticks(range(24))
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend(title="Junction ID")
plt.show()

daily_avg = df.groupby("DayOfWeek")["Vehicles"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=daily_avg, x="DayOfWeek", y="Vehicles", color="cornflowerblue")

plt.xticks(range(7), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
plt.xlabel("Days of the Week")
plt.ylabel("Mean Vehicle Count")
plt.title("Weekly Traffic Comparison")
plt.show()


plt.figure(figsize=(9, 5))

plt.hist(df["Vehicles"], bins=25, color="skyblue",
         edgecolor="darkblue", alpha=0.8)

plt.xlabel("Number of Vehicles per Hour")
plt.ylabel("Frequency")
plt.title("Distribution of Hourly Vehicle Counts")

plt.grid(axis="y", alpha=0.3)
plt.show()

