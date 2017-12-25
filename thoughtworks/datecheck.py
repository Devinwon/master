'''check the date'''
def dateCheck(sDate):
    import re
    daysinmonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    validdate = 0
    match = re.search("^(?P<year>[0-9]{4})-(?P<month>[0-3]?[0-9])-(?P<day>[0-3]?[0-9])$", sDate)
    if match:
        month = int(match.group("month"))
        day = int(match.group("day"))
        year = int(match.group("year"))

        if year < 50:
            year += 2000
        if year < 100:
            year += 1900
        if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day >= 1 and day <= 29:
                validdate = 1
        elif month >=1 and month <= 12:
            if day >=1 and day <= daysinmonth[month-1]:
                validdate = 1
    if validdate == 0:
        # print( 'date %s is invalid!' % sDate)
        return False
    else:
        # print( 'date %s is valid!' % sDate)
        return True
