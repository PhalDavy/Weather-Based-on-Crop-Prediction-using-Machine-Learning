import requests

api_key = "0cf12bb436cb1339b908188393f69676"
city_name = 'Berlin'

def get_location_coordinates(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
    # Let's parse the Json
    req = requests.get(url)
    data = req.json()

    # Let's get the name, the longitude, and latitude
    name = data['name']
    lon = data['coord']['lon']
    lat = data['coord']['lat']

    return lon, lat

def get_weather_forecast(api_key, city_name):
    exclude = "minute,hourly"
    lon, lat = get_location_coordinates(api_key, city_name)
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}'
    
    # Let's now parse the JSON
    req = requests.get(url)
    data = req.json()

    # Let's now get the temp for the day, the night, and the weather conditions
    days = []
    nights = []
    descr = []

    # We need to access 'daily'
    for i in data['daily']:
        # We notice that the temperature is in Kelvin, so we need to do -273.15 for every datapoint
        # Let's start by days
        # Let's round the decimal numbers to 2
        days.append(round(i['temp']['day'] - 273.15, 2))
        
        # Nights
        nights.append(round(i['temp']['night'] - 273.15, 2))
        
        # Let's now get the weather condition and the description
        # 'weather' [0] 'main' + 'weather' [0] 'description'
        descr.append(i['weather'][0]['main'] + ": " + i['weather'][0]['description'])

    return days, nights, descr

def format_weather_output(api_key, city_name):

    days, nights, descr = get_weather_forecast(api_key, city_name)
    output_string = f'[ {city_name} - 8 days forecast]\n'

    # Let's now loop for as much days as there are available (8 in this case):
    for i in range(len(days)):
        # We want to print out the day (day1,2,3,4..)
        # Also, day 1 = today and day 2 = tomorrow for reference

        if i == 0:
            output_string += f'\nDay {i+1} (Today)\n'

        elif i == 1:
            output_string += f'\nDay {i+1} (Tomorrow)\n'

        else:
            output_string += f'\nDay {i+1}\n'

        output_string += 'Morning:' + str(days[i]) + '°C' + "\n"
        output_string += 'Night:' + str(nights[i]) + '°C' + "\n"
        output_string += 'Conditions:' + descr[i] + '\n'

    return output_string

f = format_weather_output(api_key, city_name)
print(f)























# def get_weather_data(api_key, city_name, units):
#         base_url = "http://api.openweathermap.org/data/2.5/weather"
#         params = {
#             "q": city_name,
#             "units": units,
#             "appid": api_key
#         }
#         response = requests.get(base_url, params=params)
#         data = response.json()
#         return data

# def fetch_weather_data():
#     api_key = "0cf12bb436cb1339b908188393f69676"
#     city_name = 'Punjab'
#     units = 'metric'

#     try:
#         weather_data = get_weather_data(api_key, city_name, units)
#         return weather_data
#     except Exception as e:
#         st.error(f"Error fetching weather data: {e}")
#         return None