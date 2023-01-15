import pandas

class CBOEDataReader:
    def readCSVFile(self, path_to_file : str) -> pandas.DataFrame:
        return pandas.read_csv(path_to_file)

    def getOptionContractsByCondition(self,
                                      optionsChain : pandas.DataFrame,
                                      underlying_symbol : str = "",
                                      quote_date : str = "",
                                      root : str = "",
                                      expiration : str = "",
                                      strike : float = -1.0,
                                      option_type : str = "",
                                      open : float = -1.0,
                                      high : float = -1.0,
                                      low : float = -1.0,
                                      close : float = -1.0,
                                      trade_volume : int = -1,
                                      bid_size_1545 : int = -1,
                                      bid_1545 : float = -1.0,
                                      ask_size_1545 : int = -1,
                                      ask_1545 : float = -1.0,
                                      underlying_bid_1545 : float = -1.0,
                                      underlying_ask_1545 : float = -1.0,
                                      implied_underlying_price_1545 : float = -1.0,
                                      active_underlying_price_1545 : float = -1.0,
                                      implied_volatility_1545 : float = -1.0,
                                      delta_1545 : float = -1.0,
                                      gamma_1545 : float = -1.0,
                                      theta_1545 : float = -1.0,
                                      vega_1545 : float = -1.0,
                                      rho_1545 : float = -1.0,
                                      bid_size_eod : int = -1,
                                      bid_eod : float = -1.0,
                                      ask_size_eod : int = -1,
                                      ask_eod : float = -1.0,
                                      underlying_bid_eod : float = -1.0,
                                      underlying_ask_eod : float = -1.0,
                                      vwap : float = -1.0,
                                      open_interest : int = -1,
                                      delivery_code : float = -1.0,) -> pandas.DataFrame:

        optionContracts = optionsChain

        if len(str(underlying_symbol)) > 0:
            optionContracts = optionContracts.loc[(optionContracts["underlying_symbol"] == underlying_symbol)]

        if len(str(quote_date)) > 0:
            optionContracts = optionContracts.loc[(optionContracts["quote_date"] == quote_date)]

        if len(str(root)) > 0:
            optionContracts = optionContracts.loc[(optionContracts["root"] == root)]

        if len(str(expiration)) > 0:
            optionContracts = optionContracts.loc[(optionContracts["expiration"] == expiration)]

        if strike != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["strike"] == strike)]

        if len(option_type) > 0:
            optionContracts = optionContracts.loc[(optionContracts["option_type"] == option_type)]

        if open != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["open"] == open)]

        if high != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["high"] == high)]

        if low != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["low"] == low)]

        if close != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["close"] == close)]

        if trade_volume != -1:
            optionContracts = optionContracts.loc[(optionContracts["trade_volume"] == trade_volume)]

        if bid_size_1545 != -1:
            optionContracts = optionContracts.loc[(optionContracts["bid_size_1545"] == bid_size_1545)]

        if bid_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["bid_1545"] == bid_1545)]

        if ask_size_1545 != -1:
            optionContracts = optionContracts.loc[(optionContracts["ask_size_1545"] == ask_size_1545)]

        if ask_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["ask_1545"] == ask_1545)]

        if underlying_bid_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["underlying_bid_1545"] == underlying_bid_1545)]

        if underlying_ask_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["underlying_ask_1545"] == underlying_ask_1545)]

        if implied_underlying_price_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["implied_underlying_price_1545"] == implied_underlying_price_1545)]

        if active_underlying_price_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["active_underlying_price_1545"] == active_underlying_price_1545)]

        if implied_volatility_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["implied_volatility_1545"] == implied_volatility_1545)]

        if delta_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["delta_1545"] == delta_1545)]

        if gamma_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["gamma_1545"] == gamma_1545)]

        if theta_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["theta_1545"] == theta_1545)]

        if vega_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["vega_1545"] == vega_1545)]

        if rho_1545 != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["rho_1545"] == rho_1545)]

        if bid_size_eod != -1:
            optionContracts = optionContracts.loc[(optionContracts["bid_size_eod"] == bid_size_eod)]

        if bid_eod != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["bid_eod"] == bid_eod)]

        if ask_size_eod != -1:
            optionContracts = optionContracts.loc[(optionContracts["ask_size_eod"] == ask_size_eod)]

        if ask_eod != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["ask_eod"] == ask_eod)]

        if underlying_bid_eod != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["underlying_bid_eod"] == underlying_bid_eod)]

        if underlying_ask_eod != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["underlying_ask_eod"] == underlying_ask_eod)]

        if vwap != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["vwap"] == vwap)]

        if open_interest != -1:
            optionContracts = optionContracts.loc[(optionContracts["open_interest"] == open_interest)]

        if delivery_code != -1.0:
            optionContracts = optionContracts.loc[(optionContracts["delivery_code"] == delivery_code)]

        return optionContracts

