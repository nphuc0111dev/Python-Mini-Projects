import requests
from twilio.rest import Client

account_sid = "AC3b76edec8d112550e7e30d622ad82c44"
auth_token = "f529bb1f6ee53693408bc2bb2221f018"

MY_LAT = 21.027763
MY_LONG = 105.834160

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "4c01518a1fbe8576b1372e02b70aa2ff"

weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': api_key,
    'cnt': 4,
}

will_rain = False
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()['list']

for hour_data in weather_data:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+12019480892",
        to="+840363959556"
    )
    print(message.status)
