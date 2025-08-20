# # Human activity recognition using smartphones dataset with random forest
# # import required libraries
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
# import seaborn as sns
# import matplotlib.pyplot as plt

# # load the data set
# df = pd.read_csv('day5.csv')

# # prefrocess the dataset
# X = df.drop('Activity', axis=1)
# y = df['Activity']

# # split the dataset into traning and test sets
# X_train, X_test, y_train, y_test = train_test_split (X, y,test_size=0.2, random_state=42)

# # train the random forest classifier
# model = RandomForestClassifier (n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # make predictions on the test srt
# y_pred =  model.predict(X_test)

# # Evalutae the model usin accuracuy, precision, recall, f1 score

# accuracy = accuracy_score(y_test, y_pred)
# precision = precision_score (y_test, y_pred)
# recall = recall_score(y_test, y_pred)
# f1 = f1_score(y_test, y_pred)

# print(f"Accuracy:{accuracy * 100: 2f}%")
# print(f"Precision:{precision * 100: 2f}%")
# print(f"Recall:{recall * 100: 2f}%")
# print(f"F1_Score:{f1 * 100: 2f}%")


# #  Vis
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True, fmt='d', cmap='blue')
# plt.title('Confusion Matrix')
# plt.show()



# Human activity recognition using smartphones dataset with random forest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt

# load the data set
df = pd.read_csv('day5.csv')

# preprocess the dataset
X = df.drop('Activity', axis=1)
y = df['Activity']

# split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the random forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")
print(f"F1 Score: {f1 * 100:.2f}%")

# Confusion Matrix Visualization
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig("day5.png")  # Save the heatmap as PNG
print("Confusion matrix saved as 'day5.png'")
