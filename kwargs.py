#keyworded variable length argments [kwargs]
def person(name,*data):
    print(name)
    print(data)
person('Swetha',24,'HYD',89855)

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('Swetha',age = 24,city = 'HYD',num = 89855)

