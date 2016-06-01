# Date overlap checking

This solution is try to solved my friend question: "How to detect date overlap using sql syntax?"
Unfortunately, I am not the SQL expert. Just an idea to solve this issues in another way.  

## Question
We have pre-defined holidays for 2016, how to know that our input dates overlap with holidays? The input maybe a range of date (start - end).

## Question analysis
* We have a set of holidays distributed in 365 days. 
* We have a set of QUERY DAYS, maybe continuous or maybe not.
* We have to compare does the QUERY DAYS overlap with holidays. 

## Data structure: (NumberOfWeeks, code)
1. NumberOfWeeks range should be from 1 ~ 53. (we split 365 days to 52 weeks)
2. Code format = 0000 0000b =  (X|Sat|Fri|Thu|Wed|Tue|Mon|Sun)b
  1. Zip one week event into 1 byte, 1 = holidays/query_date, 0 = nothing happen. 


`
 
    Example:
    holiday_list = ["2016-05-01(SUN)", "2016-05-02(MON)", "2016-05-03(TUE)"]
    num_of_week, code = conv_date_string(holiday_list)
    num_of_week, code = 18, 7(0000 0111b)

    if we build the Dictionary base on years:
    holidays = {
         1: 0,   # 0000 0000b  # Week 1, no holidays
        ...
        18: 7,   # 0000 0111b  # Week 18, TUE, MON, SUN is holidays
        19: 127, # 0111 1111b  # Week 19, whole weeks is holidays
        ...
        53: 0,   # 0000 0000b
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
`
