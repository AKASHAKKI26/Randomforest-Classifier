# Randomforest-Classifier
# Heart Disease Prediction using Random Forest Classifier

This project is a Machine Learning web application built using Streamlit and Random Forest Classifier.

The application predicts whether a person has heart disease based on medical parameters.

---

## Features Used

- Age
- Chest Pain Type
- Maximum Heart Rate
- Oldpeak
- Number of Major Vessels
- Thal
- Exercise Induced Angina
- Slope

---

## Machine Learning Algorithm

- Random Forest Classifier

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pickle

---

## Project Structure

```text
HeartDiseasePrediction/
│
├── classapp.py
├── ranf.pkl
├── heart.csv
├── requirements.txt
└── README.md
```

---

## Installation

Install required libraries using:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run classapp.py
```

---

## Input Features

| Feature | Description |
|---|---|
| Age | Person's age |
| Chest Pain Type | Type of chest pain |
| Maximum Heart Rate | Maximum heart rate achieved |
| Oldpeak | ST depression value |
| Number of Major Vessels | Number of colored vessels |
| Thal | Thalassemia value |
| Exercise Induced Angina | Exercise chest pain |
| Slope | Slope of peak exercise ST segment |

---

## Output

The application predicts:

```text
Heart Disease Status
```

Example:

```text
Heart Disease Detected
```

or

```text
No Heart Disease Detected
```

---

## Model Description

The model is trained using:

- Heart Disease Dataset
- Random Forest Classifier
- Medical feature analysis

---

## Author

Machine Learning Mini Project
