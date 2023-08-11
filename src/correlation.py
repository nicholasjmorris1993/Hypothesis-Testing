import numpy as np
import pandas as pd
from scipy.stats import pearsonr


def test(x, y):
    model = Test()
    model.testing(x, y)

    return model


class Test:
    def testing(self, x, y):
        self.stat, self.p = pearsonr(x, y)

        if self.p > 0.05:
            self.result = "Probably Independent"
        else:
            self.result = "Probably Dependent"
