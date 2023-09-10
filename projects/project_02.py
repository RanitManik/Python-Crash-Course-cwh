# This is project 2

import requests
import json

# credits ==>
print("Welcome to weather app v1.6 created by Ranit Kumar Manik.")

# takes the input of the location ==>
city = input("Enter the name of the city: ")

# api url to fetch the weather data ==>
url = f"https://api.weatherapi.com/v1/current.json?key=b62f52e89b4c423c8a572303231009&q={city}"

# request to get the url ==>
r = requests.get(url)

# loads the weather data ==>
weather_dic = json.loads(r.text)

# prints only the required data ==>
print(f"The current celsius temperature in {city} is: ", weather_dic["current"]["temp_c"])
print(f"The current fahrenheit temperature in {city} is: ", weather_dic["current"]["temp_f"])
print(f"The current condition in {city} is: ", weather_dic["current"]["condition"]["text"])
