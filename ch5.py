'''#*---* five times
n=5
for i in range(n):
    print("*---*",end="")
    print()'''
#*-----*
#*----*
#*---*
#*--*
#*-*
##n=5
#for i in range(n,0,-1):
 #   print("*" + "-" * (i-1) + "*")


#*****
#****

for i in range(5):
    for j in range(1,5-i):
        print(" ",end="")

    for j in range(i+1):
        print("*",end="")
    print()
