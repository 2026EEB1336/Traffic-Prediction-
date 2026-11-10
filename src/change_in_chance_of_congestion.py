#showing coefficients

coefficients = pd.Series(model.coef_[0], index=X.columns).sort_values()

print("10 columns that INCREASE the chance of congestion the most:")
print(coefficients.tail(10)[::-1])


print("10 columns that DECREASE the chance of congestion the most:")
print(coefficients.head(10))


  #plotting about coefficients
top_positive = coefficients.tail(10)

plt.figure(figsize=(8, 5))
plt.barh(top_positive.index, top_positive.values)
plt.xlabel("Coefficient")
plt.ylabel("Feature")
plt.title("Top 10 Features that Increase Congestion Probability")
plt.grid(alpha=0.25)
plt.show()
