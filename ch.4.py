a=int(input("Enter a number:"))
if(a%400==0) or(a%4==0) and (a%100!=0):
    print(a,"is a Leap year")
else:
    print(a," is not leap year")