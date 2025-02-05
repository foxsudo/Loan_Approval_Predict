# -*- coding: utf-8 -*-
"""loanApprovalPredict.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ombzFPLXKgRwM0mTM61twLOTHpwI64kI
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load your dataset /content/drive/MyDrive/Colab Notebooks/Loan Approval Predict/loan_approval_dataset.csv
file_path = '/content/drive/MyDrive/Colab Notebooks/Loan Approval Predict/loan_approval_dataset.csv'
loan_data = pd.read_csv(file_path)

loan_data

loan_data.head()

loan_data.tail(7)

loan_data.info()

# Count missing values in each column
missing_values = loan_data.isnull().sum()
print("Missing values per column:\n", missing_values)

# Calculate the total number of missing values
total_missing = missing_values.sum()
print("\nTotal missing values:", total_missing)

# Percentage of missing values
percentage_missing = (total_missing / (loan_data.shape[0] * loan_data.shape[1])) * 100
print(f"\nPercentage of missing values: {percentage_missing:.2f}%")

loan_data.describe()

# Correction des noms de colonnes (suppression des espaces superflus)
loan_data.columns = loan_data.columns.str.strip()

# Encodage des colonnes catégoriques
loan_data['education'] = LabelEncoder().fit_transform(loan_data['education'])
loan_data['self_employed'] = LabelEncoder().fit_transform(loan_data['self_employed'])
loan_data['loan_status'] = LabelEncoder().fit_transform(loan_data['loan_status'])

loan_data.head()

# Sélection des variables explicatives (X) et de la cible (y)
X = loan_data.drop(columns=['loan_id', 'loan_status'])  # Exclure les colonnes inutiles
y = loan_data['loan_status']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X.head()

y.head()

X_train.head()

print(len(X_train))
print(len(X_test))

# Construction du modèle de régression logistique
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Affichage des résultats
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

# chose Random Forest
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

# fit model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model (example: Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Most important factors
importances = model.feature_importances_
feature_names = X.columns
print(importances)

# A horizontal bar char for import features
import matplotlib.pyplot as plt
plt.barh(feature_names, importances)
plt.xlabel('Importance')
plt.ylabel('Features')
plt.title('Feature Importance')
plt.show()

import matplotlib.pyplot as plt
# Assuming `feature_names` and `importances` are already defined
# Sort the features by importance
sorted_indices = np.argsort(importances)[::-1]  # Sort in descending order
sorted_feature_names = [feature_names[i] for i in sorted_indices]
sorted_importances = importances[sorted_indices]

# Plot the horizontal bar chart
plt.barh(sorted_feature_names, sorted_importances, color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.title('Feature Importance')
plt.gca().invert_yaxis()  # Invert the y-axis for descending order
plt.show()