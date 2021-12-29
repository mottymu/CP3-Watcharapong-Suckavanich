# Exercise While loop

usernameInput = input("username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    usernameInput = input("username : ")
    passwordInput = input("Password : ")
print("Done !")
