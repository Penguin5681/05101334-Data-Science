import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle as pk

dataFrame = pd.read_csv(
    r'C:\Users\prana\DataspellProjects\05101334-Data-Science\Datasets\heart_failure_clinical_records_dataset.csv')

model = LinearRegression()

x = ['age']
y = ['diabetes']

x_data = dataFrame[x]
y_data = dataFrame[y]

x_train, x_test, y_train, y_data = train_test_split(x_data, y_data, train_size=0.85, test_size=0.15, random_state=50)

model.fit(x_train, y_train)

# model.predict([[65]])

pickle_out = open("model.pkl", "wb")
pk.dump(model, pickle_out)
pickle_out.close()
