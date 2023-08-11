import pandas as pd
import sys
sys.path.append("/home/nick/Hypothesis-Testing/src")
from normality import test


data = pd.read_csv("/home/nick/Hypothesis-Testing/test/LungCap.csv")

distribution = test(data["LungCap"].tolist())

distribution.result
distribution.stat
distribution.p
