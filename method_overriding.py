

class A:

    def fetch(self):
        print("fetching ... A")

class B(A):
    def fetch(self):
        print("fetching ... B")



a = A()
b=B()
a.fetch()
b.fetch()
