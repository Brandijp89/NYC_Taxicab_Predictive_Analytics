
import matplotlib.pyplot as plt

import pandas as pd

#import the data
df = pd.read_csv('taxi_5.csv')
#visualize the data with different colors
plt.scatter(df['pickup_location_id'], df['dropoff_location_id'], c=df['trip_distance'], cmap=plt.cm.Reds)
plt.xlabel('pickup_location_id')
plt.ylabel('dropoff_location_id')
plt.title('trip_distance')
plt.show()
