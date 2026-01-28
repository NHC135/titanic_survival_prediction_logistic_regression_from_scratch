# Titanic Survival Prediction 

## Project Overview

This project explores the classic **Titanic dataset** to understand the factors that influenced passenger survival and to build a **logistic regression model from scratch** to predict survival outcomes. The goal is both **analytical** (insights from data) and **educational** (demonstrating core machine‑learning concepts without relying entirely on high‑level libraries).

The project covers:

* Exploratory Data Analysis (EDA)
* Data cleaning and feature engineering
* Logistic regression implemented from scratch
* Model evaluation using standard classification metrics
* Validation techniques and learning curves

---

## Dataset

**Source:** Titanic passenger dataset - Kaggle

**Target variable:**

* `Survived` (0 = Did not survive, 1 = Survived)

**Key features used:**

* `Pclass` – Passenger class
* `Sex` – Gender
* `Age` – Passenger age
* `SibSp` – Number of siblings/spouses aboard
* `Parch` – Number of parents/children aboard
* `Fare` – Ticket fare
* Engineered features such as binned age or encoded categorical variables

---

## Exploratory Data Analysis (EDA)

EDA was conducted to understand distributions, missing values, and relationships between features and survival.

some visuals created to understand the data:

**Correlation Between Features:**  
<img width="448" height="364" alt="Screenshot 2026-01-27 031312" src="https://github.com/user-attachments/assets/3d8e3044-0ef5-46ed-ba8f-2796995e0e63" />  

**Gender Survivabilty:**  
<img width="423" height="326" alt="Screenshot 2026-01-27 031256" src="https://github.com/user-attachments/assets/ec4cbd17-e563-440e-80ea-4be99ede4521" />  

**Age Bin:**  
<img width="414" height="321" alt="Screenshot 2026-01-27 031219" src="https://github.com/user-attachments/assets/d14607be-4a19-43db-9468-9792c6447907" />  

**Log Fare:**  
<img width="520" height="351" alt="Screenshot 2026-01-27 031153" src="https://github.com/user-attachments/assets/1154a530-4efd-4516-8da5-9395a7512094" />  

**ROC Curve:**  
<img width="643" height="415" alt="Screenshot 2026-01-27 031119" src="https://github.com/user-attachments/assets/a115846d-051e-41d2-90a6-8204876cb0b7" />


### Key Findings

* **Gender:** Females had a significantly higher survival rate than males.
* **Passenger Class:** First‑class passengers were more likely to survive than those in second or third class.
* **Age:** Children had higher survival rates compared to adults.
* **Fare:** Higher fares were loosely correlated with higher survival probability.

### Missing Data Handling

* `Age` contained missing values and was either imputed (mean/median) or discretized into bins.
* Non‑informative or high‑missing columns were excluded when appropriate.

---

## Feature Engineering

The following preprocessing steps were applied:

* **Categorical encoding:**

  * `Sex` encoded numerically
* **Binning:**

  * `Age` grouped into meaningful age ranges
* **Scaling:**

  * Numerical features normalized or standardized when needed
* **Train / Validation split:**

  * Dataset split into training and validation sets for model evaluation

---

## Logistic Regression (From Scratch)

Instead of using `sklearn`’s logistic regression, the model was implemented manually to demonstrate understanding of the underlying math.

### Model Components

* Sigmoid function
* Binary cross‑entropy loss
* Gradient descent optimization
* Weight and bias updates per epoch

### Training Configuration

* Learning rate (`alpha`)
* Number of epochs
* Optional kfold cross validation 

Loss curves were tracked to diagnose underfitting or overfitting.

---

## Model Evaluation

The model was evaluated using multiple classification metrics:

* **Accuracy** – Overall correctness
* **Precision** – Correct positive predictions
* **Recall** – Ability to capture actual survivors
* **F1 Score** – Balance between precision and recall
* **Confusion Matrix** – Breakdown of predictions
* **ROC_AUC** - Comparing generalizations to random guessing 

These metrics provide a more complete picture than accuracy alone, especially for imbalanced classes.

---

## Validation Strategy

* A validation set was held out from training
* Performance was monitored across epochs
* Learning curves were analyzed to ensure stable convergence
* (Optional extension) Stratified K‑Fold Cross‑Validation for robust performance estimates

---

## Results & Interpretation

* The custom logistic regression model achieved reasonable performance comparable to baseline sklearn implementations.
* Passenger class and gender emerged as the most influential predictors.
* The project demonstrates that even simple linear models can be powerful with proper feature engineering.

---

## Project Structure
**Note: data_cleaning.py is unnecessary to include or download as the functions are included into the notebook.  
It does contain useful functions for general data cleaning that I would import if it weren't on a notebook**
```
Titanic-Survival-Prediction/
│
├── notebook/
│   └── Titanic EDA and Logistic Regression.ipynb
├── data_cleaning.py
├── README.md
└── requirements.txt
```

---

## How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook:

   ```bash
   jupyter notebook
   ```
4. Run all cells sequentially

---

## Skills Demonstrated

* Data cleaning and EDA
* Feature engineering
* Logistic regression from scratch
* Gradient descent optimization
* Model evaluation and validation
* Clear ML project documentation

---

## Possible Improvements

* Hyperparameter tuning (grid/random search)
* Regularization (L1 / L2)
* More advanced models (Random Forest, XGBoost)
* Deployment as a small web app or API

---

## Author

**Nathaniel Choi**
