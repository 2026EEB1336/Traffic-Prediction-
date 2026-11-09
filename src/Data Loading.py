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

#Average traffic at each junction
plt.figure(figsize=(7, 4))
sns.barplot(data=df, x="Junction", y="Vehicles", errorbar=None)
plt.xlabel("Junction")
plt.ylabel("Average Vehicles per Hour")
plt.title("Average Traffic at Each Junction")
plt.show()

#Traffic during the day
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Hour", y="Vehicles", hue=df["Junction"].astype(str), errorbar=None)
plt.xlabel("Hour of the Day (0 - 23)")
plt.ylabel("Average Vehicles")
plt.title("Average Traffic by Hour of the Day")
plt.xticks(range(0, 24))
plt.legend(title="Junction")
plt.grid(alpha=0.25)
plt.show()

#Traffic on different days of week
plt.figure(figsize=(8, 4))
sns.barplot(data=df, x="DayOfWeek", y="Vehicles", errorbar=None)
plt.xticks(range(7), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
plt.xlabel("Day of the Week")
plt.ylabel("Average Vehicles per Hour")
plt.title("Average Traffic by Day of the Week")
plt.show()

#Distribution of the number of vehicles
plt.figure(figsize=(8, 4))
plt.hist(df["Vehicles"], bins=30, edgecolor="black")
plt.xlabel("Vehicles per Hour")
plt.ylabel("Number of Readings")
plt.title("Distribution of Vehicles per Hour")
plt.show()

plt.figure(figsize=(14, 5))
sns.lineplot(data=df, x="DateTime", y="Vehicles", hue=df["Junction"].astype(str))
plt.title("Traffic at Each Junction Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Vehicles")
plt.legend(title="Junction")
plt.grid(alpha=0.25)
plt.show()
