from random import randint
import datetime

def generate_sa_id():
    _id = ""
    _id += str(randint(0,9))  # First digit must be between 0 and 9
    _id += str(randint(0,4))  # Second digit must be between 0 and 4
    _id += str(datetime.datetime.now().year)[-2:]  # Third and fourth digit are the last two digits of the current year
    _id += str(randint(1,12)).zfill(2)  # Fifth and sixth digit are the month of birth
    _id += str(randint(1,30)).zfill(2)  # Seventh and eighth digit are the day of birth
    _id += str(randint(0,9))  # Ninth digit is random
    _id += str(randint(0,9))  # Tenth digit is random
    _id += str(randint(0,9))  # Eleventh digit is random
    _id += str(randint(0,9))  # Twelfth digit is random
    _id += str(randint(0,9))  # Thirteenth digit is random
    _id += str(randint(0,6))  # Fourteenth digit must be between 0 and 6 (gender indicator)
    
    return _id

# Example of generating a random South African ID number
print(generate_sa_id())