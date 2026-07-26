"""Geocoding_Test - Here We Are Trying to join API To Make Better Workflow"""

# part 1 ()
import requests
city_found = False
try:
    city = input("Enter City Name: ")
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}", timeout=5)
    if response.status_code == 200:
        data = response.json()
        result = data.get('results')
        if result:
            lat = data['results'][0]['latitude']
            long = data['results'][0]['longitude']
            city_found = True
        else:
            print("Error! - City Not Found Check Spelling.")
    else:
        print("Error! - API Issue")
except requests.exceptions.RequestException:
    print("Internet/Server Issue - Try Again!")

if city_found:
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true", timeout = 5)
        if response.status_code == 200:
            data = response.json()
            data1 = data['current_weather']['temperature']
            data2 = data['current_weather']['windspeed']
            print(f"Tempreature of {city}: {data1}°C & Wind Speed: {data2} Km/h")
        else:
            print("Weather API Issue!")
    except requests.exceptions.RequestException:
        print("Internet/Server Issue - Try Again!")


