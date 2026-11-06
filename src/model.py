feature_columns = ["Junction","Hour",'DayOfWeek","Month"]
X = pd.get_dummies(df[feature_columns], columns=feature_columns, drop_first=True, dtype=int)
y = df["Congestion"]
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)
print()
print("Some of the columns in X:")
print(X.columns.tolist()[:12], "...")
print()
print(X.head())
