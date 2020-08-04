import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# 
# data = pd.read_csv(r'./tempYearly.csv')
data = pd.read_csv('C:/Users/user/Documents/Coding/Python/Data Visualisation/tempYearly.csv')
print(data)

sns.jointplot("Rainfall","Temperature",data = data)
sns.jointplot("Rainfall","Temperature",data = data, kind="hex")
sns.jointplot("Rainfall","Temperature",data = data, kind="reg")
plt.show()