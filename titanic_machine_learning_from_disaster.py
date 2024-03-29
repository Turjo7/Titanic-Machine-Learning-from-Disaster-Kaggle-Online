# -*- coding: utf-8 -*-
"""Titanic: Machine Learning from Disaster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12p2bhD-QlKqwpQPaMptCmN880V4QJPII
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# load data
train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")

# feature selection
features = ["Pclass", "Sex", "SibSp", "Parch"]

X = pd.get_dummies(train_data[features])
y = train_data['Survived']

# split data to train set and validation set
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# Random forest prediction
forest_model = RandomForestClassifier(n_estimators=100)
forest_model.fit(train_X, train_y)
forest_val_predictions = forest_model.predict(val_X)
print('MAE of Random Forests: %f' % (mean_absolute_error(val_y, forest_val_predictions)))

# Decision Tree prediction
tree_model = DecisionTreeRegressor(random_state=1)
tree_model.fit(train_X, train_y)
tree_val_predictions = tree_model.predict(val_X)
print('MAE of Decision Tree: %f' % (mean_absolute_error(val_y, tree_val_predictions)))

# generate CSV
output_1 = pd.DataFrame({'PassengerId': test_data.PassengerId})
print(output_1)
output_1.to_csv('my_submission_1.csv', index=False)

# generate CSV
output_2 = pd.DataFrame({'Survived': forest_val_predictions})
print(output_2)
output_2.to_csv('my_submission_2.csv', index=False)

"""**Code After Solving array length 223 does not match index length 418!!!!!!!!!!!!**"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

test_data = pd.read_csv("data/test.csv")
test_data.head()

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived", rate_women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)

from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
print(output)
output.to_csv('my_submission.csv', index=False)
print("Your submission was successfully saved!")