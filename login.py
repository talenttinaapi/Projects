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
