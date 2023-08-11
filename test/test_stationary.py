import pandas as pd
import sys
sys.path.append("/home/nick/Hypothesis-Testing/src")
from stationary import test


data = pd.read_csv("/home/nick/Hypothesis-Testing/test/traffic.txt", sep="\t")

stable = test(data["Vehicles"].tolist())

stable.result
stable.stat
stable.p
