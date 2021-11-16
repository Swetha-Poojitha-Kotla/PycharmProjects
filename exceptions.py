#compile time - syntactical errors
#Run time - code ges compiled but also not giving logical error - > specific rong input (6/0)
#logical errors - rong outputs

a =9
b=2
k = int(input("Enter a number"))
print(k)
try:
    print("Resource open")
    print(a/b)

except ZeroDivisionError as e:
    print("Cannot be done",e)
except ValueError as e:
    print("value error")
except Exception as e:
    print("No idea on exception")
finally:
    print("Resource closed")

print("Bye")
