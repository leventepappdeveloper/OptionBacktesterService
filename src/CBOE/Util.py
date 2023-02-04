from datetime import datetime, timedelta

def getDateFromDaysDelta(startDate : str, daysDelta : float) -> str:
    startDateObject = datetime.strptime(startDate, '%Y-%m-%d')
    return "{:%Y-%m-%d}".format(startDateObject + timedelta(days=daysDelta))

def getDateListFromDaysDeltaList(startDate : str, daysDeltaList : list) -> list:
    if len(daysDeltaList) == 0:
        return []

    endDateList = []
    for daysDelta in daysDeltaList:
        endDateList.append(getDateFromDaysDelta(startDate, daysDelta))

    return endDateList



