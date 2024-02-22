from datetime import datetime, timedelta

def datedif(datetime1_str, datetime2_str):
    datetime1 = datetime.strptime(datetime1_str, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.strptime(datetime2_str, "%Y-%m-%d %H:%M:%S")
    dif = (datetime1 - datetime2)
    return dif.total_seconds()

datetime1_str = "2024-02-22 15:13:00"
datetime2_str = "2023-02-22 15:13:00"
print(datedif(datetime1_str, datetime2_str))

