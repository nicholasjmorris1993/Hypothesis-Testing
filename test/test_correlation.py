import pandas as pd
import sys
sys.path.append("/home/nick/Hypothesis-Testing/src")
from correlation import test


data = pd.read_csv("/home/nick/Hypothesis-Testing/test/LungCap.csv")

correlated = test(
    x=data["LungCap"].tolist(), 
    y=data["Height"].tolist(),
)

correlated.result
correlated.stat
correlated.p
