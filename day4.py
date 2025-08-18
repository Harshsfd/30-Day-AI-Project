# Optimized Spam Email Detector using SCIKIT-LEARN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt

# 1️⃣ Load the dataset
data = pd.read_csv('spambase.csv')
X = data.drop('spam', axis=1)  # Features
Y = data['spam']  # Target variable

# 2️⃣ Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# 3️⃣ Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4️⃣ Train the Logistic Regression model
model = LogisticRegression(max_iter=5000)  # Increased iterations
model.fit(X_train, Y_train)

# 5️⃣ Make predictions
Y_pred = model.predict(X_test)

# 6️⃣ Evaluate the model
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred)
recall = recall_score(Y_test, Y_pred)
f1 = f1_score(Y_test, Y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# 7️⃣ Confusion matrix
cm = confusion_matrix(Y_test, Y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig("confusion_matrix.png")  # Save the heatmap as PNG
print("Confusion matrix saved as 'confusion_matrix.png'")
