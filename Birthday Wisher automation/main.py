import smtplib
import datetime as dt
import random
import pandas

# From email
my_email = "nphuc0111dev@gmail.com"
my_password = "sqgt ibln tfai tzzj"

# Get today date
today = dt.datetime.now()
day = today.day
month = today.month

# Get birthday lists
data = pandas.read_csv("birthday.csv").to_dict(orient="records")
print(pandas.read_csv("birthday.csv").iterrows())
for person in data:
    if person['day'] == day and person['month'] == month:
        # Prepare content to send
        random_letter = f"letter_{random.randint(1,3)}.txt"
        with open(f"letter_templates/{random_letter}") as file:
            content = file.read()
            birthday_wisher = content.replace("[NAME]", person['name'])

        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person['email'],
                msg=f"Subject:TODAY IS A WONDERFUL DAY FOR YOU\n\n{birthday_wisher}"
            )

