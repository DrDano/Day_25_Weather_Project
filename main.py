import csv
import pandas

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

# data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
# print(type(data))
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# temp_avg = sum(temp_list) / len(temp_list)
#
# temp_max = data["temp"].max()

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)

# data_dict = {
#     "students":["Amy", "James", "Angela"],
#     "scores":[76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_colors = ["Gray", "Cinnamon", "Black"]
color_count = {}
squirrel_data = pandas.read_csv(filepath_or_buffer="NYC_Squirrel_Data.csv")
for color in squirrel_colors:
    fur_color_col = squirrel_data[squirrel_data["Primary Fur Color"] == color]
    color_count = fur_color_col["Primary Fur Color"].count()
    print(f"{color}: {color_count}")

