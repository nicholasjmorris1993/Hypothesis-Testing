import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller


def test(x):
    model = Test()
    model.testing(x)

    return model


class Test:
    def testing(self, x):
        self.stat, self.p, lags, obs, crit, t = adfuller(x)

        if self.p > 0.05:
            self.result = "Probably Not Stationary"
        else:
            self.result = "Probably Stationary"
