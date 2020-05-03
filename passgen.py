import random

#random.choice

def passwordGen():
    lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers=['1','2','3','4','5','6','7','8','9','0']
    special=['#','@','!','$','&']
    password=""

    #let the length of the password be 9 characters long (5 letters, 1 special char, and 3 numbers)

    for i in range(0,5):
        password=password+random.choice(lower)

    ind=random.randint(0,4)
    c=password[ind]
    c=c.upper()
    password = password[:ind] + c + password[ind + 1:]
    #print(c)

    for i in range(0,3):
        password=password+random.choice(numbers)

    password = password + random.choice(special)

    print(password)

passwordGen()