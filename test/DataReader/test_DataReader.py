import unittest

import pandas

from src.DataReader import DataReader

class Test(unittest.TestCase):
    def testgetOptionContractsByCondition(self):
        cboeDataReader = DataReader.CBOEDataReader()
        optionsChain = cboeDataReader.readCSVFile("test/resources/UnderlyingOptionsEODCalcs_2016-06-01.csv")

        optionContracts = cboeDataReader.getOptionContractsByCondition(optionsChain,
                                                     expiration="2016-06-29",
                                                     option_type="C",
                                                     strike=15.0)

        print(optionContracts.iloc[0]["underlying_symbol"])
        print(optionContracts.iloc[0]["quote_date"])
        print(optionContracts.iloc[0]["root"])
        print(optionContracts.iloc[0]["expiration"])
        print(optionContracts.iloc[0]["strike"])
        print(optionContracts.iloc[0]["option_type"])
        print(optionContracts.iloc[0]["open"])
        print(optionContracts.iloc[0]["high"])
        print(optionContracts.iloc[0]["low"])
        print(optionContracts.iloc[0]["close"])
        print(optionContracts.iloc[0]["trade_volume"])
        print(optionContracts.iloc[0]["bid_size_1545"])
        print(optionContracts.iloc[0]["bid_1545"])
        print(optionContracts.iloc[0]["ask_size_1545"])
        print(optionContracts.iloc[0]["ask_1545"])
        print(optionContracts.iloc[0]["underlying_bid_1545"])
        print(optionContracts.iloc[0]["underlying_ask_1545"])
        print(optionContracts.iloc[0]["implied_underlying_price_1545"])
        print(optionContracts.iloc[0]["active_underlying_price_1545"])
        print(optionContracts.iloc[0]["implied_volatility_1545"])
        print(optionContracts.iloc[0]["delta_1545"])
        print(optionContracts.iloc[0]["gamma_1545"])
        print(optionContracts.iloc[0]["theta_1545"])
        print(optionContracts.iloc[0]["vega_1545"])
        print(optionContracts.iloc[0]["rho_1545"])
        print(optionContracts.iloc[0]["bid_size_eod"])
        print(optionContracts.iloc[0]["bid_eod"])
        print(optionContracts.iloc[0]["ask_size_eod"])
        print(optionContracts.iloc[0]["ask_eod"])
        print(optionContracts.iloc[0]["underlying_bid_eod"])
        print(optionContracts.iloc[0]["underlying_ask_eod"])
        print(optionContracts.iloc[0]["vwap"])
        print(optionContracts.iloc[0]["open_interest"])
        print(optionContracts.iloc[0]["delivery_code"])



