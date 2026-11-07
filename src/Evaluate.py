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
#Precision , Recall, F1-score
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1-score :", round(f1, 4))

#classification report
print(classification_report(y_test, y_pred, target_names=["Normal (0)", "Congested (1)"]))

#Actual vs Predicted class counts
actual_counts = y_test.value_counts().sort_index()
predicted_counts = pd.Series(y_pred).value_counts().sort_index()

x = np.arange(2)
width = 0.35

plt.bar(x - width / 2, actual_counts, width, label="Actual")
plt.bar(x + width / 2, predicted_counts, width, label="Predicted")

plt.xticks(x, ["Normal (0)", "Congested (1)"])
plt.xlabel("Class")
plt.ylabel("Number of Hours")
plt.title("Actual vs Predicted Class Counts")
plt.legend()
plt.show()
