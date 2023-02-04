import unittest

from src.CBOE import Util

class Test(unittest.TestCase):
    def testgetDateFromDaysDelta(self):
        self.assertEqual(Util.getDateFromDaysDelta("2016-06-01", 49), "2016-07-20")

    def testgetDateListFromDaysDeltaList(self):
        self.assertEqual(Util.getDateListFromDaysDeltaList("2016-06-01", [0, 7, 14, 21, 28, 35, 42, 49]),
                         ['2016-06-01', '2016-06-08', '2016-06-15', '2016-06-22', '2016-06-29', '2016-07-06', '2016-07-13', '2016-07-20'])

