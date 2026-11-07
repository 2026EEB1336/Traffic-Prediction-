#Accuracy
accuracy = accuracy_score(y_test, y_pred)
baseline_accuracy = 1 - y_test.mean()

print("Model accuracy    :", round(accuracy, 4), f"({accuracy * 100:.2f}%)")
print("Baseline accuracy :", round(baseline_accuracy, 4), f"({baseline_accuracy * 100:.2f}%)")

#confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print()
print("True Negative  (TN):", cm[0, 0])
print("False Positive (FP):", cm[0, 1])
print("False Negative (FN):", cm[1, 0])
print("True Positive  (TP):", cm[1, 1])

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Predicted Normal", "Predicted Congested"],
            yticklabels=["Actual Normal", "Actual Congested"])
plt.title("Confusion Matrix")
plt.show()
