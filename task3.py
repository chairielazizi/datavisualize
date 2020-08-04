import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#create the dataframe using the json file
# df = pd.read_csv(r'./tempYearly.csv')
df = pd.read_csv('C:/Users/user/Documents/Coding/Python/Data Visualisation/tempYearly.csv')

sns.set(rc={'figure.figsize':(12,5)})
# sns.scatterplot(x='Year',y='Temperature',data = df)
# sns.regplot(x='Year',y='Temperature',data = df)
sns.regplot(x='Rainfall',y='Temperature',data = df)
plt.show()
