
av = 10
x = int(input("enter number"))
i = 1;
while i<=x:
    if i>av:
        print("Out of stock")
        break
    print("Candy")
    i = i+1
print("BYE")



for i in range(1,101):
    if(i%3==0 and i%5==0):
        continue
    print(i)
