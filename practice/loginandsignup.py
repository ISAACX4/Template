username= input("Enter username:  ")
password= input('Enter password:  ')

print('Registered')
print("Login now")
x=input("Username:  ")
y=input("password:  ")
if str(x)==str(username) and str(y)==str(password):
    print("Login successfuly")
else:
    print("invalid credentials")