import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', low_memory=False)
# print(df['usedHeap'])
plt.plot(df['timestamp'], df['maxHeap'])
plt.show()
