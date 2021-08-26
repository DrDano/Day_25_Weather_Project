data = []

with open("weather_data.csv", mode="r") as weather_file:
    data_0 = weather_file.readlines()
    for line in data_0:
        data.append(line[:-1])

print(data)