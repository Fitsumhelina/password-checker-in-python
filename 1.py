password=input("enter the password :  ")

if len(password)>0:
    if password.islower() and len(password)>8 :
       print("-------------------------------------------------")
       print("       password is valid    ")
      
      
    else :
       print("-------------------------------------------------")
       print("       password is invalid it must be lowercase and more than 8 character  ")

else :
       print("       password is reqired")
print("-------------------------------------------------")
print("       your password is : " ,password)
print("-------------------------------------------------")
print("       type of your password : " ,type(password))
print("-------------------------------------------------")
print("       the length of your password ; " ,len(password))
print("-------------------------------------------------")
    