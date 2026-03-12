# Gender_Predictor
A simple gender predictor using a Decision Tree Classifier trained on height, weight, and shoe size data.
# Gender Predictor

A beginner machine learning project that uses a Decision Tree Classifier 
to predict gender based on physical attributes.

## Features
- Trains a decision tree model on labeled sample data
- Predicts gender based on height, weight, and shoe size

## Requirements
- Python 3
- scikit-learn

## Installation
pip install scikit-learn

## Usage
Run the script with:
python3 gender_predictor.py

Modify the prediction input at the bottom of the file to test different values:
prediction = clf.predict([[190, 70, 43]])  # [height (cm), weight (kg), shoe size]

## How It Works
The model is trained on a small dataset of height, weight, and shoe size 
measurements labeled by gender. It uses scikit-learn's DecisionTreeClassifier 
to learn patterns and predict the gender of new inputs.

## Limitations
- Trained on a very small dataset (11 samples), so accuracy is limited
- For learning purposes only
