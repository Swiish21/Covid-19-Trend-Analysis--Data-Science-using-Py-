import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the provided URL
data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

# Data cleaning: Drop rows with any missing values
data.dropna(inplace=True)

# Reshape the data from wide format to long format
# 'melt' function is used to unpivot the DataFrame from wide format to long format
data = data.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Confirmed')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Exploratory data analysis (EDA)
# Print summary statistics of the data
print(data.describe())

# Print information about the DataFrame including the data types and non-null values
print(data.info())

# Data visualization: Plot the trend of confirmed COVID-19 cases over time for different countries/regions
plt.figure(figsize=(10, 6))

# Create a line plot with 'Date' on the x-axis and 'Confirmed' cases on the y-axis, colored by 'Country/Region'
sns.lineplot(data=data, x='Date', y='Confirmed', hue='Country/Region')

# Add title and labels to the plot
plt.title('Covid-19 cases trend analysis')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')

# Adjust the legend to be outside the plot
plt.legend(title='Country/Region', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()

# Save the cleaned and reshaped data to a CSV file
data.to_csv('covid19_cleaned_data.csv', index=False)