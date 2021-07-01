arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")

print(arr)

avg = sum(arr[0:])/len(arr[0:])

print(avg)

maxtemp = max(arr[0:])

print(maxtemp)

weather_dict ={}
with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("not a valid dict")


print(weather_dict['Jan 9'])
