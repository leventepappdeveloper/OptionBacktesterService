from CBOE import CBOEDataReader, Util

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options_chain = CBOEDataReader.readCSVFile("test/resources/UnderlyingOptionsEODCalcs_2016-06-01.csv")

    entry_date = "2016-06-01"
    end_date = Util.getDateFromDaysDelta(entry_date, 49)

    # (DTE, target_delta)
    stoploss_scenarios = [(35, 0.15), (28, 0.2), (21, 0.25), (14, 0.3), (7, 0.35)]

    closest_deltas_in_chain = []
    for dte, target_delta in stoploss_scenarios:
        target_date = Util.getDateFromDaysDelta(entry_date, 49 - dte)
        closest_contract = CBOEDataReader.getClosestStrikeToDelta(options_chain, "C", target_date, 0.25)
        print(closest_contract)

