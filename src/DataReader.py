import pandas

class DataReader:
    def read_CBOE_csv_data(self, path_to_file):
        data_frame = pandas.read_csv(path_to_file)
        print(data_frame.iloc[0])