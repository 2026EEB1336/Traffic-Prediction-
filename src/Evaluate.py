accuracy = accuracy_score(y_test, y_pred)
baseline_accuracy = 1 - y_test.mean()

print("Model accuracy    :", round(accuracy, 4), f"({accuracy * 100:.2f}%)")
print("Baseline accuracy :", round(baseline_accuracy, 4), f"({baseline_accuracy * 100:.2f}%)")
