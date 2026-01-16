from pywin.framework.interact import valueFormatOutputError

try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Division by zero")

try:
    x=int(input("Enter a number:"))
    print(10/x)
except valueError:
    print("invalid entry")
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("exception is successful")