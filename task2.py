import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#create the dataframe using the json file
# df = pd.read_json(r'./rain.json')
df = pd.read_json('C:/Users/user/Documents/Coding/Python/Data Visualisation/rain.json')

plt.figure(figsize=(17,5)) # (width,height)
plt.plot(df['Month'], df['Temperature'], label='Temparature')
# plt.show()

# plot rainfall
plt.figure(figsize=(17,5))
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
# plt.show()

# plot both of data
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
plt.plot(df['Month'], df['Temperature'], label='Temperature')
plt.legend()
plt.show()