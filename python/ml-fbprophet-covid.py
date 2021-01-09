#Facebook Prophet model

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#dataset
data = pd.read_csv("corona2.csv")
data.head(6)

data.describe()


#build model

#select only the important features
data= data[["Date","MuertesDia"]]

#rename the features: These names are NEEDED for the model fitting
data = data.rename(columns={"Date":"ds", "MuertesDia":"y"}) #renaming the columns of the dataset
data.head(5)

#import prophet (pip install fbprophet)
from fbprophet import Prophet

m = Prophet(daily_seasonality = True) #prophet class model
m.fit(data) #fit the model using all data

#plot prediction

future = m.make_future_dataframe(periods=365) #we need specify days in future
prediction = m.predict(future)
m.plot(prediction)

plt.title("Prediction covid")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.show()

