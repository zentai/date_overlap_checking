import datetime

def conv_date_string(date_strs):
    date_code = {}
    for date_str in date_strs:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        num_of_week = date_obj.isocalendar()[1]
        weekday = date_obj.weekday()

        if num_of_week not in date_code:
            date_code[num_of_week] = 0
        date_code[num_of_week] = date_code[num_of_week] | 0x01 << weekday
    return date_code

def overlap_report(holidays, query_dates):
    for num_of_week, query_code in query_dates.items():

        holiday_code = holidays.get(num_of_week, 0)
        overlap = query_code & holiday_code

        if overlap == 0:
            continue  # no overlap, skip
        print ("overlap detected, NumOfWeek: %s, overlap: %s(%s)"
               % (num_of_week, bin(overlap), overlap))


if __name__ == '__main__':
    holidays_list = ["2016-01-01", "2016-01-06", "2016-01-07", "2016-01-08",
                     "2016-02-01", "2016-02-02", "2016-02-03",
                     "2016-03-01",
                     "2016-04-01",
                     "2016-05-01", "2016-05-02", "2016-05-03", "2016-05-04",
                     "2016-12-31"]

    holidays = conv_date_string(holidays_list)

    dates_for_check = ["2016-05-02", "2016-05-03", "2016-05-04", "2016-05-21"]
    query_dates = conv_date_string(dates_for_check)

    overlap_report(holidays, query_dates)
