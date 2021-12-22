import matplotlib.pyplot as plt
import pandas as pd

#reading in data from csv
df = pd.read_csv('Cyclist_Crashes.csv')
#converting column to datetime to pull out the years specifically, sorted in ascending order.
df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'])
years = sorted(df['CRASH_DATE'].dt.year.unique())
#calculating yearly crashes by counting the entries for each year.
yearly_crashes = df['CRASH_DATE'].groupby(df['CRASH_DATE'].dt.year).agg('count')

#drawing the figure and axis.
fig, ax = plt.subplots(dpi=100)
#plotting.
ax.bar(years, yearly_crashes)
#setting xticks to match bars, adding labels, neatening graph.
plt.xticks([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
plt.xlabel('Years')
plt.ylabel('Number of Crashes')
plt.title('Number of Cyclist Crashes per Year')
plt.tight_layout
plt.savefig('Cyclist_Crashes_Per_Year.png')
