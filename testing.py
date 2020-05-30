from datetime import date
from datetime import datetime as dt
from os import path
import json

format = "%Y-%m-%d"
# set_date = dt.strptime("2020-11-18",format )
# print(dt.strftime(date.today(),format))
# print((set_date - dt.now()).days)
# set_time = dt.strptime("2020-05-09 21:30:00","%Y-%m-%d %H:%M:%S")
# print(set_time)
# print((dt.now() -set_time).total_seconds()/3600 )


# test = None
# print(test != None)
#
test_json = {1:{"a b": "Test works"}, 2:"b", 3:"c"}
# print(test_json)
# print(len(test_json))
# test_json[1]['a b'] = "it works again"
# print(test_json[1]['a b'])
# length = len(test_json)
# for i in range(1, length):
#     test_json[i] = test_json[i + 1]
# del test_json[3]
# print(test_json)
# today = dt.today()
# print(today <dt.today().replace(hour = 21))

# print(dt.strptime(""))
del test_json[2]
print(test_json)