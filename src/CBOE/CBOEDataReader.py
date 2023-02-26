import pandas


def readCSVFile(path_to_file : str) -> pandas.DataFrame:
    return pandas.read_csv(path_to_file)


def getoptionsContractsByCondition(options_chain : pandas.DataFrame,
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

    option_contracts = options_chain

    if len(str(underlying_symbol)) > 0:
        option_contracts = option_contracts.loc[(option_contracts["underlying_symbol"] == underlying_symbol)]

    if len(str(quote_date)) > 0:
        option_contracts = option_contracts.loc[(option_contracts["quote_date"] == quote_date)]

    if len(str(root)) > 0:
        option_contracts = option_contracts.loc[(option_contracts["root"] == root)]

    if len(str(expiration)) > 0:
        option_contracts = option_contracts.loc[(option_contracts["expiration"] == expiration)]

    if strike != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["strike"] == strike)]

    if len(option_type) > 0:
        option_contracts = option_contracts.loc[(option_contracts["option_type"] == option_type)]

    if open != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["open"] == open)]

    if high != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["high"] == high)]

    if low != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["low"] == low)]

    if close != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["close"] == close)]

    if trade_volume != -1:
        option_contracts = option_contracts.loc[(option_contracts["trade_volume"] == trade_volume)]

    if bid_size_1545 != -1:
        option_contracts = option_contracts.loc[(option_contracts["bid_size_1545"] == bid_size_1545)]

    if bid_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["bid_1545"] == bid_1545)]

    if ask_size_1545 != -1:
        option_contracts = option_contracts.loc[(option_contracts["ask_size_1545"] == ask_size_1545)]

    if ask_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["ask_1545"] == ask_1545)]

    if underlying_bid_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["underlying_bid_1545"] == underlying_bid_1545)]

    if underlying_ask_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["underlying_ask_1545"] == underlying_ask_1545)]

    if implied_underlying_price_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["implied_underlying_price_1545"] == implied_underlying_price_1545)]

    if active_underlying_price_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["active_underlying_price_1545"] == active_underlying_price_1545)]

    if implied_volatility_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["implied_volatility_1545"] == implied_volatility_1545)]

    if delta_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["delta_1545"] == delta_1545)]

    if gamma_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["gamma_1545"] == gamma_1545)]

    if theta_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["theta_1545"] == theta_1545)]

    if vega_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["vega_1545"] == vega_1545)]

    if rho_1545 != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["rho_1545"] == rho_1545)]

    if bid_size_eod != -1:
        option_contracts = option_contracts.loc[(option_contracts["bid_size_eod"] == bid_size_eod)]

    if bid_eod != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["bid_eod"] == bid_eod)]

    if ask_size_eod != -1:
        option_contracts = option_contracts.loc[(option_contracts["ask_size_eod"] == ask_size_eod)]

    if ask_eod != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["ask_eod"] == ask_eod)]

    if underlying_bid_eod != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["underlying_bid_eod"] == underlying_bid_eod)]

    if underlying_ask_eod != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["underlying_ask_eod"] == underlying_ask_eod)]

    if vwap != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["vwap"] == vwap)]

    if open_interest != -1:
        option_contracts = option_contracts.loc[(option_contracts["open_interest"] == open_interest)]

    if delivery_code != -1.0:
        option_contracts = option_contracts.loc[(option_contracts["delivery_code"] == delivery_code)]

    return option_contracts


def getClosestStrikeToDelta(options_chain : pandas.DataFrame, option_type : str, expiration : str, target_option_delta : float) -> pandas.DataFrame:

    # Get all option contracts for the given type and expiration in the given chain
    option_contracts = getoptionsContractsByCondition(options_chain=options_chain,
                                                      option_type=option_type,
                                                      expiration=expiration)

    # Get all available deltas from all option_contracts
    available_option_deltas = option_contracts.loc[:, "delta_1545"]

    absolute_distances_from_target = available_option_deltas.apply(lambda x: abs(x - target_option_delta))

    min_distance_from_target = min(absolute_distances_from_target)

    min_distance_from_target_index = absolute_distances_from_target[absolute_distances_from_target == min_distance_from_target].index[0]

    return options_chain.iloc[[min_distance_from_target_index]]