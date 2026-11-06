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

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.20,
stratify=y
)
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape:{X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape:{y_test.shape}")
