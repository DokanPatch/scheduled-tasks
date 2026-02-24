import requests
import smtplib
import os

API_KEY = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_MAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
RECIPIENT_EMAIL = "jimmyredsolo@gmail.com"

weather_params = {
    "lat": 50.583452,
    "lon": 11.143583,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()

weather_data = response.json()
will_rain = False
print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg="Subject:Rain Alert\n\nIt's going to rain today. Remember to bring an umbrella."
        )

