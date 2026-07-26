"""Practicing API System - how Its Works."""
import requests
# # part 1
# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.text)


# # part 2
# import requests

# response = requests.get("https://api.github.com")
# data = response.json()      # yeh JSON string ko Python dictionary mein convert karta hai

# print(data["current_user_url"])   # ab seedha ek specific value nikal sakte ho

# # part 3
# import requests

# city = input("Enter city name: ")
# response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=31.5&longitude=74.3&current_weather=true")

# data = response.json()
# print(data)

# # part 4
# import requests
# city = input("Enter city name: ")
# response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=31.5&longitude=74.3&current_weather=true")
# data = response.json()
# data1 = data['current_weather']['temperature']
# data2 = data['current_weather']['windspeed']
# print(f"Tempreature of Lahore: {data1}°C & Wind Speed: {data2} Km/h")


# part 4 (upgrade)
try:
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=31.5&longitude=74.3&current_weather=true", timeout = 5)
    if response.status_code == 200:
        data = response.json()
        data1 = data['current_weather']['temperature']
        data2 = data['current_weather']['windspeed']
        print(f"Tempreature of Lahore: {data1}°C & Wind Speed: {data2} Km/h")
    else:
        print("City Not Found! Or API Issue!")
except requests.exceptions.RequestException:
    print("Internet/Server Issue - Try Again!")
