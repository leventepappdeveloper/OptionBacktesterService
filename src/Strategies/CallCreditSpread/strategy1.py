from src.CBOE import Util

class Strategy1:

    def executeStrategy(self):
        entry_Date = "2016-06-01"
        end_Date = Util.getDateFromDaysDelta(entry_Date, 49)
        risk_Management_Dates = Util.getDateListFromDaysDeltaList(entry_Date, [7, 14, 21, 28, 35, 42])
        

