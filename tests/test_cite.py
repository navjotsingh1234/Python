
from datetime import datetime,timedelta
import unittest

import pandas as pd

import covid19dh

class TestCite(unittest.TestCase):
    def test_cite_verbose(self):
        # get data
        x,src = covid19dh.covid19("CZE", verbose = False)
        # cite
        src2 = covid19dh.cite(x, verbose = False)

__all__ = ["TestCite"]