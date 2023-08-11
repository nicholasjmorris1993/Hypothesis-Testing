import pandas as pd
import sys
sys.path.append("/home/nick/Hypothesis-Testing/src")
from average import test


data = pd.read_csv("/home/nick/Hypothesis-Testing/test/LungCap.csv")

x = data.loc[data["Smoke yes"] == 1, "LungCap"].tolist()
y = data.loc[data["Smoke yes"] == 0, "LungCap"].tolist()

# make sure x and y have the same number of observations
length = min(len(x), len(y))
x = x[:length]
y = y[:length]

center = test(x, y)

center.result
center.stat
center.p
