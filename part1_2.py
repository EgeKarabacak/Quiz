import pandas as pd
import requests

# Part 1

# Suggested dataset: NYC Tree Census does not work leads to 404 I have pulled different csv file from same api.

# Pandas supports fetching from url's so no need for requests package.
# https://data.cityofnewyork.us/Housing-Development/Community-Development-Block-Grant-CDBG-Eligibility/qmcw-ur37/data_preview
df = pd.read_csv('https://data.cityofnewyork.us/resource/qmcw-ur37.csv')

# Data frame is redundant since pandas read_csv automatically creates a Dataframe from fetched csv.
dff = pd.DataFrame(df)
# By default head reads first 5 lines of DataFrame. you can modify this number by dff.head(n=20) if you want first 20 lines. 
print(dff.head())


# Part 2 using pandas 
# OpenWeather api does not conatin ID, I have omitted that series from the table.

df2 = pd.read_json('https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&hourly=temperature_2m')
print("Part 2 using pandas")
print(df2)

# part 2 using requests
params = {'longitude': '-74.0060', 'latitude': '40.7128',"hourly": "temperature_2m"}
r = requests.get('https://api.open-meteo.com/v1/forecast',params= params)
data = r.json()
df3 = pd.DataFrame(data)

print("Part 2 using requests")
print(df3.head())
