password = input("Password:") 
password_one = password

if len(password_one) > 8 :
    print("Your password : " + password + " has  been set")
elif len(password_one) < 8 :
    print("Invalid password!. Try again (Your password should be 8 or more characters)")
    password = input("Password:") 
    print("Your password : " + password + " has  been set.")
   

