# Project 2: Data Classification using Iris Dataset
# DecodeLabs Internship Batch 2026

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset Shape:", X.shape)
print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)

# Step 2: Split data 80-20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)

# Step 3: Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Step 5: Predictions
predictions = model.predict(X_test)

# Step 6: Evaluation
accuracy = accuracy_score(y_test, predictions)
print("\nAccuracy:", accuracy * 100, "%")

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, predictions)
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))

# Step 7: Plot Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Iris Classification')
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.show()

print("\nProject 2 Complete!")