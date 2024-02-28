import requests
import time
import smtplib
import os

my_email = "ibro73222@gmail.com"
password = os.environ.get("password")
access = os.environ.get("access")
url = "https://the-one-api.dev/v2/movie"
header = {"Authorization": f"Bearer {access}"}
response = requests.get(url, headers=header)
response.raise_for_status()
data = response.json()
print(data)
my_lord = data["docs"]

# from datetime import datetime, timedelta
# from threading import Timer
#
# x=datetime.today()
# y = x.replace(day=x.day+5, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
# delta_t=y-x
#
# secs=delta_t.total_seconds()
#
# def hello_world():
#     print("hello world")
#     #...
#
# t = Timer(secs, hello_world)
# t.start()
#
#
#

for movie in my_lord:
    print("goat")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gbadegesinibrahim24@gmail.com",
                            msg=f"subject: Lord of The Rings InFo\n\n"
                                f"\n{movie['name']}"
                                f"\nrun time in minutes {movie['runtimeInMinutes']}"
                                f"\nbudget in millions is {movie['budgetInMillions']}"
                                f"\nbox office revenue is {movie['boxOfficeRevenueInMillions']}"
    )
    time.sleep(2880)
    print("haa")
