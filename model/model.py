import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

data_path = "/home/azadm/Desktop/Flask/dataset/insurance.csv"
data = pd.read_csv(data_path)
le = LabelEncoder()
le.fit(data['sex'])
data['Sex'] = le.transform(data['sex'])
le.fit(data['smoker'])
data['Smoker'] = le.transform(data['smoker'])
le.fit(data['region'])
data['Region'] = le.transform(data['region'])
#independent and dependent columns
x = data[["age", "bmi", "children", "Sex", "Smoker", "Region"]]
y = data['charges']

#split the data into train and text data
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.3, random_state=0)

#model training
linreg = LinearRegression()
linreg.fit(x_train, y_train)

#model testing
prediction = linreg.predict(x_test)
score = linreg.score(x_test, y_test)
print(score)

#save model
file = open("expense_model.pkl", 'wb')
pickle.dump(linreg, file)