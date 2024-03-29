import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


def test(x, y):
    model = Test()
    model.testing(x, y)

    return model


class Test:
    def testing(self, x, y):
        self.stat, self.p = ttest_ind(x, y)

        if self.p > 0.05:
            self.result = "Probably The Same Average"
        else:
            self.result = "Probably Different Averages"
