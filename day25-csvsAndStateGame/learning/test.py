# with open("day25-csvsAndStateGame\learning\weather_data.csv") as data:
#   weather_data = data.readlines()
  
# print(weather_data)

# use the inbuilt
# import csv

# with open("day25-csvsAndStateGame\learning\weather_data.csv") as data_file:
#   data = list(csv.reader(data_file))
#   temperatures = []
#   for row in range(1, len(data)-1):
#     temperatures.append(int((data[row][1])))
    
#   print(temperatures)

import pandas

data = pandas.read_csv("day25-csvsAndStateGame\learning\weather_data.csv")

print(data)
print(type(data)) #<class 'pandas.core.frame.DataFrame'
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
sum=0
for temp in temp_list:
  sum+=temp
  
avg = sum/len(temp_list)
print(avg)

print(data["temp"].mean())

print(data["temp"].max())

print(data.condition)
print(data["condition"])

#get data in the rows 
print(data[data.day == "Monday"])

# print the row of data which had the highest temperature
hottest_day_temp = data["temp"].max()
hottest_day = data[data.temp == data["temp"].max()]
print(hottest_day)

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp[0]
monday_temp = monday_temp * 9/5 + 32
print(monday_temp)

# how to create data frame from scratch
data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)

#convert to csv
data.to_csv(r"day25-csvsAndStateGame\learning\new_data.csv")
print(data)
