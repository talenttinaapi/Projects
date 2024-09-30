def login(username: str, password: str) ->bool:
    is_aunthenticated = False

    if username == "admin" and password == "1234":
        is_aunthenticated = True

    return is_aunthenticated

user = input("Username: ")
passw = input("Password: ")

logged_in = login(user, passw)

message = "Login failed, Check your credentials"

#if logged_in:
   #message = "Login succesful"

    #print(message)

print ("Login succesful" if logged_in else "Login failed, Check your credentials")


"""
A script to show the user the current time.

Author: Matthew Pitkin
Email: m.pitkin@lancaster.ac.uk
Date: 22/06/2020
"""

# import the required modules
import datetime


def gettime():
    """
    A function to return the current time.

    Returns
    -------
    tuple:
        A tuple containing the hour, minutes and seconds.
    """

    now = datetime.datetime.now()

    return now.hour, now.minute, now.second + 1e-6 * now.microsecond

# get the time
hour, minute, seconds = gettime()

print(f"The current time is {hour}:{minute}:{seconds}")

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from the webpage
data = soup.find('div', class_='content')
print(data.text)