import pandas as pd
import random

series = pd.Series([random.randint(1, 100) for i in range(10)])

print("Series:")
print(series)

print("First 5:")
print(series.head())

print("Last 5:")
print(series.tail())

print("Maximum:", series.max())
print("Minimum:", series.min())
print("Mean:", series.mean())

print("Python List:")
print(series.tolist())