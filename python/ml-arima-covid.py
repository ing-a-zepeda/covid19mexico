import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from pandas import datetime
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

df = pd.read_csv("corona2.csv")
df.head(6)

plt.figure()
lag_plot(df['InfectadosDia'], lag = 1)
plt.title('TESLA Stock - Autocorrelation plot with lag = 1')
plt.show()

plt.plot(df["Date"], df["InfectadosDia"])
plt.xticks(np.arange(0,200,5), df['Date'][0:200:5], rotation="vertical")
plt.title("TESLA stock price over time")
plt.xlabel("time")
plt.ylabel("deaths")
plt.show()

train_data, test_data = df[0:int(len(df)*0.7)], df[int(len(df)*0.7):]
training_data = train_data['InfectadosDia'].values
test_data = test_data['InfectadosDia'].values
history = [x for x in training_data]
model_predictions = []
N_test_observations = len(test_data)
for time_point in range(N_test_observations):
    model = ARIMA(history, order=(4,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    model_predictions.append(yhat)
    true_test_value = test_data[time_point]
    history.append(true_test_value)
MSE_error = mean_squared_error(test_data, model_predictions)
print('Testing Mean Squared Error is {}'.format(MSE_error))


test_set_range = df[int(len(df)*0.7):].index
plt.plot(test_set_range, model_predictions, color='blue', marker='o', linestyle='dashed',label='Muertes pronosticadas python')
plt.plot(test_set_range, test_data, color='red', label='Muertes reales')
plt.title('Muertes covid')
plt.xlabel('Fecha')
plt.ylabel('Muertes')
plt.xticks(np.arange(125,200,1), df.Date[125:200:1], rotation="vertical")
plt.legend()
plt.show()
