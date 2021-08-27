import csv

data_list = []
# with open("weather_data.csv", mode="r") as weather_file:
#     data_0 = weather_file.readlines()
#     for line in data_0:
#         data.append(line[:-1])

# temperatures = []
# with open("weather_data.csv", mode="r") as weather_file:
#     data = csv.reader(weather_file)
#     for line in data:
#         data_list.append(line[1])
#         new_list = data_list[1:]
#     for index in new_list:
#         temperatures.append(int(index))
# print(temperatures)

import pandas
data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
print(data["temp"])
