
'''
if date is valid,return index of weekday (0-6)
'''
import datetime
def get_week_day(datestr):
    week_day_dict = {
        0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天',
      }
    day = datetime.datetime.strptime(datestr ,"%Y-%m-%d").weekday()
    # print(week_day_dict[day])
    return int(day)


