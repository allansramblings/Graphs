import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import seaborn as sns

sns.set_theme(style="darkgrid")

#reading in data from CSV
df = pd.read_csv('Burrinjuck_Dam_Percentage_Full.csv', delimiter=',', parse_dates=[0], skiprows=3)

#converting column to datetime to order data correctly
#df.iloc[0] = pd.to_datetime(df.iloc[0]).dt.strftime('%d-%m-%y')
date = df.iloc[3:len(df), 0]
percentage_full = df.iloc[3:len(df), 1]
print(date)

#drawing the figure and axis
fig, ax = plt.subplots(dpi=200)
#plotting
#ax.plot(date, percentage_full)
plt.plot(date, percentage_full)
plt.show()
plt.savefig("Aku.png", dpi=200)
