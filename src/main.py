from DataReader import DataReader

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataReader = DataReader()
    dataReader.read_CBOE_csv_data("test/resources/UnderlyingOptionsEODCalcs_2016-06-01.csv")

