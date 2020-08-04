import pandas as pd
import matplotlib.pyplot as plt

# create the dataframes using json files
# df = pd.read_json(r'./rain.json')
df = pd.read_json('C:/Users/user/Documents/Coding/Python/Data Visualisation/rain.json')
print(df) 

print("df statistics: ",df.describe())

df.plot(x='Month',y='Temperature')
df.plot(x='Month',y='Rainfall')
plt.show()

# iris_data = pd.read_json("https://raw.githubusercontent.com/domoritz/maps/master/data/iris.json")
# iris_data.head()
# print(iris_data)

# iris_data.plot(x='sepalLength',y='sepalWidth')
# plt.show()