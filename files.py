f = open('data','r')
#full data
#print(f.read())
#first line
#print(f.readline(),end="")
#print(f.readline())


#print till nth character in line
# print(f.readline(7))


f2= open('abc','w')
#f2.write("Laptop")
# f2.write("Something")
# f2.write("People")
#
#f2 = open('abc','a')
#f2.write("Mobile")

for data in f:
    f2.write(data)

#read binary then ill give hex values
i1 = open('img.jpg','rb')
i2 = open('myPic.jpg','wb')

for i in i1:
    i2.write(i)
