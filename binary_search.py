pos = -1
list = [4,6,7,8,9,13,45,67,89,100]

def search(list,n):
    l =0
    u = len(list)
    while l<=u:
        m = (l+u)//2
        if list[m] == n:
            globals()['pos']= m
            return True
        else:
            if list[m] < n:
                l = m
            else:
                u = m



n = 67
if search(list,n):
     print("FOund at ", pos)
else:
    print("not Found")


