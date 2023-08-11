import numpy as np
import pandas as pd
from scipy.stats import shapiro


def test(x):
    model = Test()
    model.testing(x)

    return model


class Test:
    def testing(self, x):
        self.stat, self.p = shapiro(x)

        if self.p > 0.05:
            self.result = "Probably Normal"
        else:
            self.result = "Probably Not Normal"
