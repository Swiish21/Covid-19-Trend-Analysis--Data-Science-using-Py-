import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

# Data cleaning
data.dropna(inplace=True)

# Reshape the data
data = data.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Confirmed')
data['Date'] = pd.to_datetime(data['Date'])

# Exploratory data analysis (EDA)
print(data.describe())
print(data.info())

# Data visualization
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Date', y='Confirmed', hue='Country/Region')

plt.title('Covid-19 cases trend analysis')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.legend(title='Country/Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Save cleaned data
data.to_csv('covid19_cleaned_data.csv', index=False)