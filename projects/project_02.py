# This is project 2
import requests
import json

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=b62f52e89b4c423c8a572303231009&q={city}"

r = requests.get(url)
# print(r.text)
# print(type(r.text))

weather_dic = json.loads(r.text)
print(f"The current celsius temperature in {city} is: ", weather_dic["current"]["temp_c"])
print(f"The current fahrenheit temperature in {city} is: ", weather_dic["current"]["temp_f"])
print(f"The current condition in {city} is: ", weather_dic["current"]["condition"]["text"])
