import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

#Getting hold of a single column
print(data["temp"])

#Calculating the average temperature
my_temp = data["temp"].to_list()
print(my_temp)

avg = sum(my_temp) / len(my_temp)
print(f"Average Temperature: {avg}")

#Easier Method
my_avg = data["temp"].mean()
print(f"My Average = {my_avg}")

#Maximum Value from the series
my_max = data["temp"].max()
print(my_max)

#Row where the temperature was maximum
max_temp_row = data[data.temp == data["temp"].max()] # or data.temp.max()
print(max_temp_row)

#Get the temperature of monday and convert it to celsius from fahrenheit
monday_series = data[data.day == "Monday"]
monday_temp = monday_series.temp[0]
f = (monday_temp * 9/5 ) + 32
print(f"Fahrenheit = {f}F")

#Creating a data frame from scratch
data_dict = {
    "students" : ["A", "B", "C"],
    'scores' : [76, 65, 54]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")