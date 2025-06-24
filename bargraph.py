
import pandas as pd
import matplotlib.pyplot as plt
#read the csv file
df = pd.read_csv('taxi_5.csv')
#print the first 5 rows
print(df.head())
#plot the graph

plt.xlabel('fare_amount')
plt.ylabel('trip_distance')

#showing bar graph
x=df['fare_amount']
y=df['trip_distance']
plt.bar(x, y, color=['blue', 'green', 'red', 'purple'])
plt.show()










