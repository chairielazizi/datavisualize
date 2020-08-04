import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# create the dataframe from the data.csv
# data= pd.read_csv(r'./birthYearly.csv')
data = pd.read_csv('C:/Users/user/Documents/Coding/Python/Data Visualisation/birthYearly.csv')
print(data)

dataP = data.pivot("month","year","births")
print(dataP)

sns.heatmap(dataP, annot=True, fmt="d")

plt.show()