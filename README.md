# Traffic Prediction & Congestion Alert System

Predicts whether a road junction will be congested at a given date and time from hourly vehicle counts, using **Logistic Regression** (pandas, matplotlib, seaborn, scikit-learn), and raises a **LOW / MODERATE / HIGH** alert.

**How it works**

1. Reads hourly vehicle counts for four junctions (`data/Traffic.csv`).
2. Labels an hour as **congested (1)** when its vehicle count is above the 75th percentile of that junction, otherwise **normal (0)**.
3. Trains a Logistic Regression model on junction, hour of day, day of week and month.
4. Evaluates it with accuracy, confusion matrix, precision, recall and F1-score.
5. Turns the predicted probability of congestion into an alert:

| Probability of congestion | Alert |
|---------------------------|-------|
| 70% or more               | HIGH |
| 40% to 70%                | MODERATE |
| Below 40%                 | LOW |

---

## Team and roles

| Member | Entry no. | Role |
|--------|-----------|------|
| Bhawishya Achary | 2026EEB1336 | Documentation Lead |
| Satyam | 2026AIB1078 | Execution Lead |
| Sarth | 2026MCB1564 | Video Lead |
| Naman | 2026EEB1383 | PPT Lead |

Each member's contributions are visible in the commit history.

---

## Project structure

```
/
├── src/                                    
│   ├── main.py                              # runs every step in order
│   ├── data_loading.py                      # loads the data, explores it, cleans it and plots graphs
│   ├── target_column.py                     # creates the Congestion column (1 = congested, 0 = normal)
│   ├── input_features.py                    # builds the input features (junction, hour, day, month)
│   ├── split.py                             # splits the data into training and test sets
│   ├── feature_scale.py                     # scales the features
│   ├── training.py                          # trains the Logistic Regression model and predicts
│   ├── evaluation.py                        # accuracy, confusion matrix, precision, recall, F1
│   ├── change_in_chance_of_congestion.py    # shows what the model learned (coefficients)
│   └── alert_system.py                      # gives a congestion alert for a junction and time                           
├── requirements.txt              # libraries to install
├── data/
│   ├── README.md                 # where the dataset goes and which columns it needs
│   └── Traffic.csv               # hourly vehicle counts, 4 junctions
├── docs/
│   ├── DATASET.md                # columns, target and features
│   └── images                    # screenshots used in this README
├──presentation/
|   ├── README.md                
│   └── Traffic_Prediction_PPT    # 5 Sildes PPT that summarises our project 
└── README.md                     # This README.md that you are reading (Ccontains the summary of the Repo)
```

---

## Setup & Installation

Tested on Python 3.14.7 (macOS) with numpy 2.5.4, pandas 3.1.1, scikit-learn 1.9.1, matplotlib 3.11.2 and seaborn 0.13.2. `requirements.txt` sets minimum versions, so other recent Python versions should also work, but we have not tested them. Git and Python 3 must be installed.

All commands below are typed in a **terminal**, one block at a time. Press Enter after each line.

### 0. Open a terminal



### 1. Clone the repository (in the terminal)

```bash
git clone https://github.com/2026EEB1336/Traffic-Prediction-.git
cd Traffic-Prediction-
```

### 2. Create a virtual environment (in the terminal)

- **Windows:**

```bash
python -m venv venv
```

- **macOS / Linux:**

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment (in the terminal)

- **Windows (Command Prompt):**

```bash
venv\Scripts\activate
```

- **macOS / Linux:**

```bash
source venv/bin/activate
```

`(venv)` now appears at the start of the terminal line.

### 4. Install the libraries (in the terminal)

```bash
pip install -r requirements.txt
```

### 5. Run the project (in the terminal)

Run this from the project folder (`Traffic-Prediction-`):

```bash
python src/main.py
```

Enter junction number (1-4): 1
Enter date and time (example: 2017-07-03 08:00): 2017-07-03 08:00

## Expected output

The script prints, in this order:

- the dataset shape, missing values and rows per junction
- the congestion limit of each junction (vehicles per hour)
- the model's accuracy next to a "lazy" baseline, then the confusion matrix, precision, recall and F1-score
- an alert message in this format:


=======================================================
Junction : 1
Time     : Monday, 03 July 2017, 08:00
Chance of congestion : <xx.x>%
ALERT LEVEL          : <HIGH / MODERATE / LOW>
(Congestion here means more than <N> vehicles in the hour)
=======================================================
```

![Traffic by hour of the day](doc/Traffic%20by%20hour.png)
![Confusion matrix](doc/Confusion%20Matrix.png)
![24-hour congestion forecast](doc/Congession%20forecast.png)
![Alert output in the terminal](doc/Alert%20Output.png)
![Traffic by year](doc/Yearly%20Traffic.png)

---

## Links

- Slides: [https://github.com/2026EEB1336/Traffic-Prediction-/blob/main/presentation/Traffic_Prediction_ppt_n.pdf]
- Video: []

**Limitations:** congestion is defined relative to each junction's own traffic; the model knows only the calendar (no weather, accidents or holidays); it does not use the previous hour's traffic.

---

## AI-use disclosure

- Claude: Helped us debug a PermissionError when loading the dataset, which was caused by traffic.csv being a folder instead of a file.
- Claude: First draft of this README; edited by Bhawishya 
- Claude: It helped us connect all the files together and run from a single file main.py using exec(open("file”).read()).
- Claude: Some functions, attributes and methods like pd.to_datetime(), .dt.hour, .dt.dayofweek, .dt.month, quantile(0.75), building a one-row table with
          pd.DataFrame(0, index=[0], columns=X.columns), plus strftime, plt.axhline was used in the code that was explained by claude for the proper functioning
          of the project.
- No AI was used to generate the dataset or the results.
