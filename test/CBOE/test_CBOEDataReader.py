import math
import unittest
import numpy as np

from src.CBOE import CBOEDataReader

class Test(unittest.TestCase):
    def test_getoptionContractsByCondition(self):
        options_chain = CBOEDataReader.readCSVFile("test/resources/UnderlyingOptionsEODCalcs_2016-06-01.csv")

        option_contracts = CBOEDataReader.getoptionsContractsByCondition(options_chain,
                                                                        expiration="2016-06-29",
                                                                        option_type="C",
                                                                        strike=15.0)
        self.assertTrue(len(option_contracts) == 1)

        option_contract = option_contracts.iloc[0]

        self.assertTrue(isinstance(option_contract["underlying_symbol"], str))
        self.assertEqual(option_contract["underlying_symbol"], "^VIX")

        self.assertTrue(isinstance(option_contract["quote_date"], str))
        self.assertEqual(option_contract["quote_date"], "2016-06-01")

        self.assertTrue(isinstance(option_contract["root"], str))
        self.assertEqual(option_contract["root"], "VIX")

        self.assertTrue(isinstance(option_contract["expiration"], str))
        self.assertEqual(option_contract["expiration"], "2016-06-29")

        self.assertTrue(isinstance(option_contract["strike"], float))
        self.assertEqual(option_contract["strike"], 15.0)

        self.assertTrue(isinstance(option_contract["option_type"], str))
        self.assertEqual(option_contract["option_type"], "C")

        self.assertTrue(isinstance(option_contract["open"], float))
        self.assertEqual(option_contract["open"], 2.06)

        self.assertTrue(isinstance(option_contract["high"], float))
        self.assertEqual(option_contract["high"], 2.06)

        self.assertTrue(isinstance(option_contract["low"], float))
        self.assertEqual(option_contract["low"], 1.88)

        self.assertTrue(isinstance(option_contract["close"], float))
        self.assertEqual(option_contract["close"], 1.88)

        self.assertTrue(isinstance(option_contract["trade_volume"], (int, np.integer)))
        self.assertEqual(option_contract["trade_volume"], 3)

        self.assertTrue(isinstance(option_contract["bid_size_1545"], (int, np.integer)))
        self.assertEqual(option_contract["bid_size_1545"], 8)

        self.assertTrue(isinstance(option_contract["bid_1545"], float))
        self.assertEqual(option_contract["bid_1545"], 1.8)

        self.assertTrue(isinstance(option_contract["ask_size_1545"], (int, np.integer)))
        self.assertEqual(option_contract["ask_size_1545"], 313)

        self.assertTrue(isinstance(option_contract["ask_1545"], float))
        self.assertEqual(option_contract["ask_1545"], 1.9)

        self.assertTrue(isinstance(option_contract["underlying_bid_1545"], float))
        self.assertEqual(option_contract["underlying_bid_1545"], 14.24)

        self.assertTrue(isinstance(option_contract["underlying_ask_1545"], float))
        self.assertEqual(option_contract["underlying_ask_1545"], 14.24)

        self.assertTrue(isinstance(option_contract["implied_underlying_price_1545"], float))
        self.assertEqual(option_contract["implied_underlying_price_1545"], 15.9967)

        self.assertTrue(isinstance(option_contract["active_underlying_price_1545"], float))
        self.assertEqual(option_contract["active_underlying_price_1545"], 14.24)

        self.assertTrue(isinstance(option_contract["implied_volatility_1545"], float))
        self.assertEqual(option_contract["implied_volatility_1545"], 0.7579)

        self.assertTrue(isinstance(option_contract["delta_1545"], float))
        self.assertEqual(option_contract["delta_1545"], 0.6603)

        self.assertTrue(isinstance(option_contract["gamma_1545"], float))
        self.assertEqual(option_contract["gamma_1545"], 0.1096)

        self.assertTrue(isinstance(option_contract["theta_1545"], float))
        self.assertEqual(option_contract["theta_1545"], -0.0221)

        self.assertTrue(isinstance(option_contract["vega_1545"], float))
        self.assertEqual(option_contract["vega_1545"], 0.0162)

        self.assertTrue(isinstance(option_contract["rho_1545"], float))
        self.assertEqual(option_contract["rho_1545"], 0.6622)

        self.assertTrue(isinstance(option_contract["bid_size_eod"], (int, np.integer)))
        self.assertEqual(option_contract["bid_size_eod"], 8)

        self.assertTrue(isinstance(option_contract["bid_eod"], float))
        self.assertEqual(option_contract["bid_eod"], 1.8)

        self.assertTrue(isinstance(option_contract["ask_size_eod"], (int, np.integer)))
        self.assertEqual(option_contract["ask_size_eod"], 418)

        self.assertTrue(isinstance(option_contract["ask_eod"], float))
        self.assertEqual(option_contract["ask_eod"], 1.95)

        self.assertTrue(isinstance(option_contract["underlying_bid_eod"], float))
        self.assertEqual(option_contract["underlying_bid_eod"], 14.2)

        self.assertTrue(isinstance(option_contract["underlying_ask_eod"], float))
        self.assertEqual(option_contract["underlying_ask_eod"], 14.2)

        self.assertTrue(isinstance(option_contract["vwap"], float))
        self.assertEqual(option_contract["vwap"], 2.0)

        self.assertTrue(isinstance(option_contract["open_interest"], (int, np.integer)))
        self.assertEqual(option_contract["open_interest"], 5137)

        self.assertTrue(isinstance(option_contract["delivery_code"], float))
        self.assertTrue(math.isnan(option_contract["delivery_code"]))

    def test_getClosestStrikeToDelta(self):
        options_chain = CBOEDataReader.readCSVFile("test/resources/UnderlyingOptionsEODCalcs_2016-06-01.csv")

        CBOEDataReader.getClosestStrikeToDelta(options_chain, "C", "2016-07-20", 0.25)

