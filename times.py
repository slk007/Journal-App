import time

month = {1: "Jan",
         2: "Feb",
         3: "Mar",
         4: "Apr",
         5: "May",
         6: "June",
         7: "July",
         8: "Aug",
         9: "Sept",
         10: "Oct",
         11: "Nov",
         12: "Dec"
         }


def get_timestamp():

    a = time.localtime()

    x = str(a.tm_mday) + " " + str(month[a.tm_mon]) + " " + str(a.tm_year) + " " + str(a.tm_hour) + ":" + str(a.tm_min)

    # 25 Jun 2019 10.30pm
    return x
