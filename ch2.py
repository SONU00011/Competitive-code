#read n print sum  of digites in n
n = int(input("Enter a number: "))
s= 0  
while (n>0):
    digite =n%10
    n=n//10 
    s += digite
 
print("sum of digits:", s)