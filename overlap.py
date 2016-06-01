import datetime

def conv_date_string(date_strs):
    """
    Data structure (Dict):
    ===
    Key=NumOfWeek, Val=code
    code = 1 byte = int( X|Sat|Fri|Thu|Wed|Tue|Mon|Sun )


    Example:
    ===
    holiday_list = ["2016-05-01(SUN)", "2016-05-02(MON)", "2016-05-03(TUE)"]
    num_of_week, code = conv_date_string(holiday_list)
    num_of_week, code = 18, 7(0000 0111b)

    if we build the table base on years:
    holidays = {
         1: 0, # 0000 0000b
        ...
        18: 7,   # 0000 0111b
        19: 127, # 0111 1111b
        ...
        52: 0, # 0000 0000b
    }

    dates_for_check = ["2016-05-03(TUE)", "2016-05-04(WED)", "2016-05-05(THU)"]
    num_of_week, code = conv_date_string(dates_for_check)
    num_of_week, code = 18, 28(0001 1100b)

    Compare:
    holidays[18] = 0000 0111b
    query_code   = 0001 1100b (AND)
    ===============================
                   0000 0100b

    ANS: weeks 18, Tuedays conflict.

    so, 52 bytes should be cover whole years holidays.
    code range from 0 ~ 127 (only 7 bit)
    """

    date_code = {}
    for date_str in date_strs:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        num_of_week = date_obj.isocalendar()[1]
        weekday = date_obj.weekday()

        if num_of_week not in date_code:
            date_code[num_of_week] = 0
        date_code[num_of_week] = date_code[num_of_week] | 1 << weekday
    return date_code

def overlap_report(holidays, query_dates):
    for num_of_week, query_code in query_dates.items():
        overlap = query_code & holidays.get(num_of_week, 0)
        if overlap > 0:
            print ("overlap detected: Number of week: %s, conflict code: %s(%s)"
                   % (num_of_week, bin(overlap), overlap))


if __name__ == '__main__':
    holidays_list = ["2016-04-30",
                     "2016-05-01",
                     "2016-05-02",
                     "2016-05-03",
                     "2016-05-04",
                     "2016-05-05",
                     "2016-05-06",
                     "2016-05-07",
                     "2016-05-08",
                     "2016-05-09",
                     "2016-05-10"]

    holidays = conv_date_string(holidays_list)

    dates_for_check = ["2016-05-02",
                       "2016-05-03",
                       "2016-05-04",
                       "2016-05-21"]
    query_dates = conv_date_string(dates_for_check)

    overlap_report(holidays, query_dates)
