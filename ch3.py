#reverse of a number
A= int(input("enter a number:"))
answer=0
while(A>0):
    digite = A % 10
    A=A//10
    answer=answer*10 +digite
print(answer)
