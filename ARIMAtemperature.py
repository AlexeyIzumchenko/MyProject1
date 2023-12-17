import pandas as pd
import numpy as np

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.tools import diff
from statsmodels.tsa.arima_model import ARMAResults,ARIMAResults
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tools.eval_measures import rmse
from statsmodels.graphics.tsaplots import month_plot,quarter_plot
from statsmodels.tsa.stattools import adfuller


from pandas.plotting import lag_plot
import matplotlib.pyplot as plt
from dateutil.parser import parse
from scipy import stats
from scipy.stats import normaltest
from sklearn.metrics import mean_squared_error
from pmdarima import auto_arima

df=pd.read_csv("/home/sdl/temperature.csv", index_col="Time", parse_dates=True)
# df=pd.read_csv('/home/sdl/temperature.csv', names=["Time", "Temperature"], header=0)
# df=df.dropna()
print("Shape of data", df.shape)
df.head()

df['Temperature'].plot(figsize=(12,5))

import csv

# with open('example.csv', 'w') as file:
#     fieldnames = ['Temperature']
#     writer = csv.writer(file)
#     writer.writerow(data[1])

gfg_csv_data = pred.to_csv('2Temperature.csv', header='Temperature', index = True) 
print('\nCSV String:\n', gfg_csv_data) 
