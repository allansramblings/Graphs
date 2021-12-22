import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn')
#Reading in data from CSV
data = pd.read_csv('Bus_Service_Reliability.csv')
#Storing data from columns into variables
service_delivery = data['Service Delivery %']
service_failures = data['Service Failures']
services_delivered = data['Services Delivered']
date = data['Date']
#plotting
plt.scatter(service_failures, services_delivered, c=service_delivery, cmap="Blues", s=30, alpha=0.6, edgecolor='black', linewidth=1)
#Adding colour bar for extra readability
cbar = plt.colorbar()
cbar.set_label('Service Delivery Percentage')

plt.title('Service Reliability')
plt.xlabel('Service Failures')
plt.ylabel('Services Delivered')
#neatening graph, saving fig.
plt.tight_layout()
plt.savefig('Service Reliabilty.png')