import datetime

class DateOverlap(object):
    """docstring for DateOverlap"""
    def __init__(self):
        self._holidays = {}

    def _conv_data_structure(self, date_str):
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        num_of_week = date_obj.isocalendar()[1]
        weekday = date_obj.weekday()
        return (num_of_week, weekday)

    def add(self, date_str):
        (num_of_week, weekday) = self._conv_data_structure(date_str)
        if num_of_week not in self._holidays:
            self._holidays[num_of_week] = 0
        self._holidays[num_of_week] = self._holidays[num_of_week] | 1 << weekday
        print "add date: %s, {%s: %s - %s}" % (date_str, num_of_week, weekday, self._holidays[num_of_week])

    def remove(self, date_str):
        pass

    def is_overlap(self, date_str_list=[]):
        # generate compare list
        temp = {}
        for date_str in date_str_list:
            (num_of_week, weekday) = self._conv_data_structure(date_str)
            if num_of_week not in temp:
                temp[num_of_week] = 0
            temp[num_of_week] = temp[num_of_week] | 1 << weekday

        for key, val in temp.items():
            result = self._holidays[key] | val
            if result > 0:
                print "W: %s, BIN: %s" % (key, bin(result))

if __name__ == '__main__':
    overlap = DateOverlap()
    overlap.add("2016-04-30")
    overlap.add("2016-05-01")
    overlap.add("2016-05-02")
    overlap.add("2016-05-03")
    overlap.add("2016-05-04")
    overlap.add("2016-05-05")
    overlap.add("2016-05-06")
    overlap.add("2016-05-07")
    overlap.add("2016-05-08")
    overlap.add("2016-05-09")
    overlap.add("2016-05-10")

    print "is overlap", overlap.is_overlap(["2016-05-05",
                                            "2016-05-06",
                                            "2016-05-07",
                                            "2016-05-08",
                                            "2016-05-09",
                                            "2016-05-10",
                                            "2016-05-01",])
