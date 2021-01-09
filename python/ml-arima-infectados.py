#ARIMA

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from pandas import datetime
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

#load data
df = pd.read_csv("corona3.csv")
df.head(6)

#verify crossrelation in data
plt.figure()
lag_plot(df['InfectadosDia'], lag = 2)
plt.title('Infectados por día - Lag = 1')
plt.show()

#gráfica total
plt.plot(df["Date"], df["MuertesDia"])
plt.xticks(np.arange(0,200,2), df['Date'][0:200:2], rotation="vertical")
plt.title("Muertes por día")
plt.xlabel("Fecha")
plt.ylabel("Muertes")
plt.show()

#build ARIMA model, training 70%, test 30%, p=4, d=1 y q=0 (originalmente)
#p number of lag observations
#d degree of differencing
#q size of the moving average window
train_data, test_data = df[0:int(len(df)*0.7)], df[int(len(df)*0.7):]
training_data = train_data['MuertesDia'].values
test_data = test_data['MuertesDia'].values
history = [x for x in training_data]
model_predictions = []
N_test_observations = len(test_data)
for time_point in range(N_test_observations):
    model = ARIMA(history, order=(3,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    model_predictions.append(yhat)
    true_test_value = test_data[time_point]
    history.append(true_test_value)
MSE_error = mean_squared_error(test_data, model_predictions)
print('Testing Mean Squared Error is {}'.format(MSE_error))


test_set_range = df[int(len(df)*0.7):].index
print(df[int(len(df)*0.7):].index)
plt.plot(test_set_range, model_predictions, color='blue', marker='o', linestyle='dashed',label='Muertes pronosticadas python')
plt.plot(test_set_range, test_data, color='red', label='Muertes reales')
plt.title('Infectados por día covid')
plt.xlabel('Fecha')
plt.ylabel('Infectados')
plt.xticks(np.arange(125,180,1), df.Date[125:180:1], rotation="vertical")
plt.legend()
plt.show()

