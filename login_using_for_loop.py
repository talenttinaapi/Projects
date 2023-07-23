def login(username: str, password: str) ->bool:
    is_aunthenticated = False

    if username == "admin" and password == "1234":
        is_aunthenticated = True

    return is_aunthenticated

user = input("Username: ")
passw = input("Password: ")

is_aunthenticated = False

for attempt in range(5):
    if login(user, passw) == True:
     is_aunthenticated = True
     break
else:
   print("Login failed, Re-enter your credentals")
   user = input("Username: ")
   passw = input("Password: ")

print("Login is succesful" if is_aunthenticated else "Your account has bee locked temporarily")



