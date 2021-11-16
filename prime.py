n = int(input("Enter number"))
for i in range(2,n):
    if(n%i==0):
        print("Not a prime")
        break
else:
        print("prime number")