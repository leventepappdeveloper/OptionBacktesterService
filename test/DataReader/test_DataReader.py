import math
import unittest
import numpy as np

from src.DataReader import DataReader

class Test(unittest.TestCase):
    def testgetOptionContractsByCondition(self):
        cboeDataReader = DataReader.CBOEDataReader()
        optionsChain = cboeDataReader.readCSVFile("test/resources/UnderlyingOptionsEODCalcs_2016-06-01.csv")

        optionContracts = cboeDataReader.getOptionContractsByCondition(optionsChain,
                                                     expiration="2016-06-29",
                                                     option_type="C",
                                                     strike=15.0)
        self.assertTrue(len(optionContracts) == 1)

        optionContract = optionContracts.iloc[0]

        self.assertTrue(isinstance(optionContract["underlying_symbol"], str))
        self.assertEqual(optionContract["underlying_symbol"], "^VIX")

        self.assertTrue(isinstance(optionContract["quote_date"], str))
        self.assertEqual(optionContract["quote_date"], "2016-06-01")

        self.assertTrue(isinstance(optionContract["root"], str))
        self.assertEqual(optionContract["root"], "VIX")

        self.assertTrue(isinstance(optionContract["expiration"], str))
        self.assertEqual(optionContract["expiration"], "2016-06-29")

        self.assertTrue(isinstance(optionContract["strike"], float))
        self.assertEqual(optionContract["strike"], 15.0)

        self.assertTrue(isinstance(optionContract["option_type"], str))
        self.assertEqual(optionContract["option_type"], "C")

        self.assertTrue(isinstance(optionContract["open"], float))
        self.assertEqual(optionContract["open"], 2.06)

        self.assertTrue(isinstance(optionContract["high"], float))
        self.assertEqual(optionContract["high"], 2.06)

        self.assertTrue(isinstance(optionContract["low"], float))
        self.assertEqual(optionContract["low"], 1.88)

        self.assertTrue(isinstance(optionContract["close"], float))
        self.assertEqual(optionContract["close"], 1.88)

        self.assertTrue(isinstance(optionContract["trade_volume"], (int, np.integer)))
        self.assertEqual(optionContract["trade_volume"], 3)

        self.assertTrue(isinstance(optionContract["bid_size_1545"], (int, np.integer)))
        self.assertEqual(optionContract["bid_size_1545"], 8)

        self.assertTrue(isinstance(optionContract["bid_1545"], float))
        self.assertEqual(optionContract["bid_1545"], 1.8)

        self.assertTrue(isinstance(optionContract["ask_size_1545"], (int, np.integer)))
        self.assertEqual(optionContract["ask_size_1545"], 313)

        self.assertTrue(isinstance(optionContract["ask_1545"], float))
        self.assertEqual(optionContract["ask_1545"], 1.9)

        self.assertTrue(isinstance(optionContract["underlying_bid_1545"], float))
        self.assertEqual(optionContract["underlying_bid_1545"], 14.24)

        self.assertTrue(isinstance(optionContract["underlying_ask_1545"], float))
        self.assertEqual(optionContract["underlying_ask_1545"], 14.24)

        self.assertTrue(isinstance(optionContract["implied_underlying_price_1545"], float))
        self.assertEqual(optionContract["implied_underlying_price_1545"], 15.9967)

        self.assertTrue(isinstance(optionContract["active_underlying_price_1545"], float))
        self.assertEqual(optionContract["active_underlying_price_1545"], 14.24)

        self.assertTrue(isinstance(optionContract["implied_volatility_1545"], float))
        self.assertEqual(optionContract["implied_volatility_1545"], 0.7579)

        self.assertTrue(isinstance(optionContract["delta_1545"], float))
        self.assertEqual(optionContract["delta_1545"], 0.6603)

        self.assertTrue(isinstance(optionContract["gamma_1545"], float))
        self.assertEqual(optionContract["gamma_1545"], 0.1096)

        self.assertTrue(isinstance(optionContract["theta_1545"], float))
        self.assertEqual(optionContract["theta_1545"], -0.0221)

        self.assertTrue(isinstance(optionContract["vega_1545"], float))
        self.assertEqual(optionContract["vega_1545"], 0.0162)

        self.assertTrue(isinstance(optionContract["rho_1545"], float))
        self.assertEqual(optionContract["rho_1545"], 0.6622)

        self.assertTrue(isinstance(optionContract["bid_size_eod"], (int, np.integer)))
        self.assertEqual(optionContract["bid_size_eod"], 8)

        self.assertTrue(isinstance(optionContract["bid_eod"], float))
        self.assertEqual(optionContract["bid_eod"], 1.8)

        self.assertTrue(isinstance(optionContract["ask_size_eod"], (int, np.integer)))
        self.assertEqual(optionContract["ask_size_eod"], 418)

        self.assertTrue(isinstance(optionContract["ask_eod"], float))
        self.assertEqual(optionContract["ask_eod"], 1.95)

        self.assertTrue(isinstance(optionContract["underlying_bid_eod"], float))
        self.assertEqual(optionContract["underlying_bid_eod"], 14.2)

        self.assertTrue(isinstance(optionContract["underlying_ask_eod"], float))
        self.assertEqual(optionContract["underlying_ask_eod"], 14.2)

        self.assertTrue(isinstance(optionContract["vwap"], float))
        self.assertEqual(optionContract["vwap"], 2.0)

        self.assertTrue(isinstance(optionContract["open_interest"], (int, np.integer)))
        self.assertEqual(optionContract["open_interest"], 5137)

        self.assertTrue(isinstance(optionContract["delivery_code"], float))
        self.assertTrue(math.isnan(optionContract["delivery_code"]))



