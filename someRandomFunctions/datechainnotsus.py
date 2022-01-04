import time as t
from datetime import datetime

# If you're chinmay then don't

def dateGen():
    current_t = t.localtime()
    current_clock = t.strftime("%H:%M:%S", current_t)
    a = str((datetime.now()))
    b = a.split()[0]
    dob = []
    year_l = []
    month_l = []
    day_l = []
    for i in b:
        dob.append(i)

    for i in range(4):
        year_l.append(dob[i])

    for i in range(2):
        month_l.append(dob[i+5])
        day_l.append(dob[i+8])

    year = str(year_l[0] + year_l[1] + year_l[2] + year_l[3])
    month_n = str(month_l[0] + month_l[1])
    day_prev = str(day_l[0] + day_l[1])
    months = {
            "1":"January",
            "2":"February",
            "3":"March",
            "4":"April",
            "5":"May",
            "6":"June",
            "7":"July",
            "8":"August",
            "9":"Sepetember",
            "10":"October",
            "11":"November",
            "12":"December"
            }
    mon_list = list(map(int, month_n))
    day_list = list(map(int, day_prev))
    if mon_list[0] is 0:
        if day_list[0] is 0: 
            mon_list.remove(0)
            day_list.remove(0)
            month_prev = mon_list[0]
            day = day_list[0]
            month = months[str(month_prev)]
            date = f"{month} {day}, {year}"
            return date
        else:
            mon_list.remove(0)
            month_prev = mon_list[0]
            month = months[str(month_prev)]
            date = f"{month} {day_prev}, {year}"
            return date 
    else:
        month = months[str(month_n)]
        date = f"{month} {day_prev}, {year}"
        return date
