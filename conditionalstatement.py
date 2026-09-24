light = (input ("light:"))
if (light == "red"):
    print("Stop")

elif (light == "green"):
    print ("Move")

elif (light == "yellow"):
    print ("Look")

else:
    print("Light is broken")


light = (input ("light:"))
signal = "stop" if light == "red" else "move"
print (signal)

number = int (input ("num:"))
print ("pass") if number>50 or number == 50 else print ("fail")

age = int (input ("age:"))
vote = ("no","yes") [age >= 18]
print (vote)

salary = float (input ("salary:"))
tax = salary * (0.1, 0.2) [salary >= 5000]
print (tax)

age = int (input ("age:"))
if (age>=18):
    if (age >= 50):
        print("Elder")
    else:
        print("Younger")
else:
    print("Not Adult")
    