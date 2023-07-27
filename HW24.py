import math
from datetime import datetime

# #HW24.1
# def sector_area(r, alpha):
#     return (math.pi * r ** 2) * math.degrees(alpha) / 360
#
#
# print(sector_area(2, math.pi))
#


# # HW24.2
# def week_day(y, m, d):
#
#     week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
#     return week_days[datetime.strptime(f"{y}-{m}-{d}", "%Y-%m-%d").weekday()]
#
#
# year = input("Enter the year: ")
# month = input("Enter the month: ")
# day = input("Enter the day: ")
#
#
# print(week_day(year, month, day))


# # HW24.3
#
# def arab_to_roma(num):
#     roma = ""
#     while num > 0:
#         if num >= 1000:
#             roma += "M" * (num // 1000)
#             num %= 1000
#         elif num >= 500:
#             roma += "D"
#             num %= 500
#         elif num >= 100:
#             roma += "C" * (num // 100)
#             num %= 100
#         elif num >= 50:
#             roma += "L"
#             num %= 50
#         elif num >= 10:
#             roma += "X" * (num // 10)
#             num %= 10
#         elif num == 9:
#             roma += "IX"
#             num -= 9
#         elif num >= 5:
#             roma += "V"
#             num -= 5
#         elif num == 4:
#             roma += "IV"
#             num -= 4
#         else:
#             roma += "I" * num
#             num %= 1
#     return roma
#
#
# print(arab_to_roma(524))
#





