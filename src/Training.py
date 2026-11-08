model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)
print("Logistic Regression model trained successfully!")

y_pred = model.predict(X_test_scaled)

print("First 10 predicted values:", y_pred[:10])
print("First 10 actual values   :", y_test.iloc[:10].to_numpy())

correct = 0
for i in range(10):
    if y_pred[i] == y_test.iloc[i]:
        correct = correct + 1
print("Correct predictions out of the first 10:", correct)
