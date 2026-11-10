HIGH_LIMIT = 0.70
MODERATE_LIMIT = 0.40


def predict_congestion_probability(junction, date_time):

    if junction not in thresholds:
        raise ValueError(
            f"Invalid junction! Available junctions: {list(thresholds.keys())}"
        )

    timestamp = pd.to_datetime(date_time)

    input_data = pd.DataFrame(
        0, index=[0], columns=X.columns
    )

    features = {
        "Junction_" + str(junction),
        "Hour_" + str(timestamp.hour),
        "DayOfWeek_" + str(timestamp.dayofweek),
        "Month_" + str(timestamp.month)
    }

    for feature in features:
        if feature in input_data.columns:
            input_data.loc[0, feature] = 1

    scaled_data = scaler.transform(input_data)
    congestion_chance = model.predict_proba(scaled_data)[0][1]

    return congestion_chance


def get_alert_level(probability):

    if probability >= HIGH_LIMIT:
        return "🔴 HIGH"

    if probability >= MODERATE_LIMIT:
        return "🟡 MODERATE"

    return "🟢 LOW"


def congestion_alert(junction, date_time):

    timestamp = pd.to_datetime(date_time)

    chance = predict_congestion_probability(
        junction, timestamp
    )

    alert = get_alert_level(chance)

    print("\n" + "-" * 50)
    print("       TRAFFIC CONGESTION ALERT")
    print("-" * 50)

    print(f"Junction       : {junction}")
    print(f"Date & Time    : {timestamp.strftime('%d-%m-%Y %H:%M')}")
    print(f"Congestion     : {chance * 100:.2f}%")
    print(f"Alert Status   : {alert}")
    print(f"Vehicle Limit  : {thresholds[junction]:.0f} vehicles/hour")

    print("-" * 50)


print("Congestion Alert System initialized successfully!")


congestion_alert(1, "2017-07-03 08:00:00")
congestion_alert(1, "2017-07-02 03:00:00")
congestion_alert(2, "2017-07-05 18:00:00")

check_time = "2017-07-03 18:00:00"

print("CONGESTION ALERT BOARD")
print("=" * 50)

for junction in sorted(thresholds.keys()):
    congestion_alert(junction, check_time)

print("Alert board generated successfully!")

junction = 1
selected_date = "2017-07-03"

hours = []
probabilities = []
alert_levels = []
alert_colors = []

for hour in range(24):

    time_value = f"{selected_date} {hour:02d}:00:00"

    probability = predict_congestion_probability(junction, time_value)
    alert = get_alert_level(probability)

    hours.append(hour)
    probabilities.append(probability)
    alert_levels.append(alert)

    if probability >= HIGH_LIMIT:
        alert_colors.append("red")
    elif probability >= MODERATE_LIMIT:
        alert_colors.append("orange")
    else:
        alert_colors.append("green")


forecast_data = pd.DataFrame({
    "Hour": hours,
    "Probability (%)": [round(value * 100, 1) for value in probabilities],
    "Alert Level": alert_levels
})

print(forecast_data)
colors = [
    "red" if p >= HIGH_LIMIT else "orange" if p >= MODERATE_LIMIT else "green"
    for p in probabilities
]
plt.figure(figsize=(11, 5))
plt.bar(hours, probabilities, color=colors)
plt.axhline(HIGH_LIMIT, linestyle="--", color="red", label="HIGH limit (70%)")
plt.axhline(MODERATE_LIMIT, linestyle="--", color="orange", label="MODERATE limit (40%)")
plt.xticks(range(24))
plt.xlabel("Hour of the Day")
plt.ylabel("Probability of Congestion")
plt.title(f"Congestion Forecast for Junction {junction_to_check} on {date_to_check}")
plt.legend()
plt.show()

try:
    junction_number = int(input("Enter junction number (1-4): "))
    selected_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")

    congestion_alert(junction_number, selected_time)

except (ValueError, TypeError) as error:
    print("Invalid input:", error)
