df["Congestion"] = 0          
thresholds = {}               

for j in sorted(df["Junction"].unique()):
    j = int(j)                                  
    
    this_junction = df["Junction"] == j

    limit = df.loc[this_junction, "Vehicles"].quantile(0.75)
    thresholds[j] = limit

    df.loc[this_junction & (df["Vehicles"] > limit), "Congestion"] = 1

    print(f"Junction {j}: congestion if more than {limit} vehicles per hour")

print()
print("Count of each class:")
print(df["Congestion"].value_counts().sort_index())

print()
print(f"Percentage of congested hours:{round(df["Congestion"].mean() * 100, 2)}%")
