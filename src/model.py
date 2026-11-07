model = LogisticRegression(max_iter=1000)

model.fit(X_train_scaled, y_train)
