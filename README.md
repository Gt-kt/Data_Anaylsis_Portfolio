# Bank Marketing Campaign Analysis and Prediction

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Key Insights](#key-insights)


---

## Project Overview

This project analyzes the **Bank Marketing Dataset** from the UCI Machine Learning Repository to identify factors that influence a client's decision to subscribe to a term deposit. The analysis includes data cleaning, exploratory data analysis (EDA), feature engineering, and building a predictive model using logistic regression.

---

## Dataset

The dataset contains information collected from direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls, aiming to convince clients to subscribe to a term deposit.

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
- **Data Format:** CSV file (`bank-additional-full.csv`)
- **Attributes:** 21 columns including client information, contact details, and campaign outcomes.

**Note:** Due to licensing restrictions, the dataset is not included in this repository. Please download it directly from the [source](https://archive.ics.uci.edu/ml/datasets/bank+marketing).

---

## Project Structure

Bank_marketing_analysis/
├── data/                           # Data folder (not included)
│   └── bank-additional-full.csv    # Dataset (to be added by the user)
├── Bank_Analysis.ipynb         # Jupyter notebook with analysis
├── images/                         # Folder for result images
│   ├── Age_distribution.png
│   ├── Subscription_by_job.png
│   └── etc..
├── requirements.txt                # Required Python packages
├── README.md                       # Project documentation
└── LICENSE                         # License information


## Installation
Clone the repository and install the required libraries:

git clone https://github.com/Gt-kt/Bank_marketing_analysis.git
cd Bank_marketing_analysis
pip install -r requirements.txt


## Usage


1. Download the Dataset:

 - Download bank-additional-full.csv from the UCI Repository.
 - Place the CSV file in the data/ directory within the project folder.

2. Run the Jupyter Notebook:
jupyter notebook notebooks/Bank_Analysis.ipynb

3. Follow the Analysis:
 - Open the notebook in your browser.
 - Execute the cells sequentially to reproduce the analysis.
 - Ensure that all required packages are installed.


## Results
The logistic regression model achieved an accuracy of 90.98% on the test set. However, due to class imbalance, precision and recall are more informative:

Precision (Subscribed): 66%
Recall (Subscribed): 43%
F1-Score (Subscribed): 52%
The model performs well in predicting clients who will not subscribe but has difficulty identifying potential subscribers.



## Key Insights
1. Age and Subscription:
Clients aged 56 and above have significantly higher subscription rates.
2. Job Influence:
'Retired' and 'student' job categories show the highest likelihood of subscription.
3. Previous Contact:
Clients previously contacted in past campaigns are more likely to subscribe.
4. Communication Method:
Cellular phone contacts are more effective than traditional telephone calls.
5. Economic Indicators:
Lower interest rates and negative employment variation rates correlate with higher subscription rates.