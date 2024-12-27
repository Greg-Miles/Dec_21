from files_utils import *


data = """{
        "city" : "Иваново",
        "api_key" : "ebfcbecf95e3f82734882df8042875fc",
        "units" : "metric",
        "language" : "ru"
        }"""

data_dict = {
        "city" : "Иваново",
        "api_key" : "ebfcbecf95e3f82734882df8042875fc",
        "units" : "metric",
        "language" : "ru"
        }
data_list = [{
        "city" : "Иваново",
        "api_key" : "ebfcbecf95e3f82734882df8042875fc",
        "units" : "metric",
        "language" : "ru"
        }]
print(type(data_dict))
# write_json(data_dict, "test.json", encoding = "utf-8")
# print(read_json("test.json"))

write_csv(data_dict, "test.csv", delimiter=";")
print(read_csv("test.csv",";"))
