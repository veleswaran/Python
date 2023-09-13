num = int(input("enter the Number"))

if num%2==0 and num!=0:
    print("It is the even number")
    if num%4:
        print("It is divisible by 4")
    else:
        print("It is Not divisible by 4")
elif num%2!=0:
    print("It is the odd Number")
    if num%3==0:
        print("It is divisible by 3")
    else:
        print("It is not divisible by 3")
else:
    print("It is a zero")