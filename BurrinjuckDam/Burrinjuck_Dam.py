import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="darkgrid")

#reading in data from CSV
df = pd.read_csv('Burrinjuck_Dam_Percentage_Full.csv', delimiter=',', parse_dates=[0], skiprows=3)
#converting column to datetime to order data correctly
date = df.iloc[3:len(df), 0]
percentage_full = df.iloc[3:len(df), 1]

#drawing the figure and axis
fig, ax = plt.subplots()
#plotting
ax.plot(date, percentage_full)
ax.set_title("Burrinjuck Dam Water Levels")
plt.ylabel("Water Level in Percent")
plt.xlabel("Period Measured")
plt.tight_layout()
plt.show()