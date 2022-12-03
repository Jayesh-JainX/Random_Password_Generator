import random
import datetime

a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "1234567890"
d = "!@#$%^&*()?><|\~"
f = open("password.txt", 'a')
f.write("--------------------------------------------------\n")
f.write("----------- Random Password's History ------------\n")
x = datetime.datetime.now()
f.write("- "+x.strftime("%c")+"\n\n")
f.close()
while(1):
    print("\n\n------------------------------------------------------\n")
    print("-------------------- Get Password --------------------\n")
    s = int(input(("\n1: Get an Alphanumeric Password\n2: Get Only Alphabetical Password\n3: Get Only Digits Password\n4: See Passwords History\n5: Enter '0' to Exit\n\nEnter Your Choice: ")))
    if(s == 1):
        p = a+b+c+d
        l = int(input("\nEnter the Length of Password: "))
        final = "".join(random.sample(p, l))
        print("\n\n---------------- Password Generated ----------------")
        print("\nYour Password is: "+final+"\n")
        f = open("password.txt", 'a')
        f.write("- "+final+"\n")
        f.close()
    elif(s == 2):
        p = a+b+d
        l = int(input("\nEnter the Length of Password: "))
        final = "".join(random.sample(p, l))
        print("\n\n---------------- Password Generated ----------------")
        print("\nYour Password is: "+final+"\n")
        f = open("password.txt", 'a')
        f.write("- "+final+"\n")
        f.close()
    elif(s == 3):
        p = c+c+c
        l = int(input("\nEnter the Length of Password: "))
        final = "".join(random.sample(p, l))
        print("\n\n---------------- Password Generated ----------------")
        print("\nYour Password is: "+final+"\n")
        f = open("password.txt", 'a')
        f.write("- "+final+"\n")
        f.close()
    elif(s == 4):
        print("\n\n")
        f = open("password.txt", 'r')
        for d in f:
            print(d, end='')
        f.close()
        print("------------ Password History Ends ------------")
    elif(s == 0):
        print("\n\n------------------------------------------------------\n")
        print("-------------Thanks For Using Our Service-------------\n")
        f = open("password.txt", 'a')
        f.write("\n-------------------- App Closed --------------------\n\n\n\n")
        f.close()
        break
    else:
        print("\nWrong Choice Try Again")
