import requests
from datetime import datetime
import smtplib  # lib for send email
import time

MY_LAT = 21.027763
MY_LONG = 105.834160

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def can_see():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
print(sunrise, sunset, time_now)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# From email
my_email = "nphuc0111dev@gmail.com"
my_password = "sqgt ibln tfai tzzj"

# To email
another_email = "nphuc44078@gmail.com"

while True:
    time.sleep(60)
    if can_see():
        if time_now == 23 or time_now < 10:
            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=another_email,
                    msg=f"Subject:PLEASE SEE THE SKY\n\nISS is appeared in the sky. Time to view."
                )
