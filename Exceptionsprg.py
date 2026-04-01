
try:
    val=int(input("Enter a value"))
    a=int(input("Enter a value to divide"))
    print("Entered Value:",val)
    val1=val/a
except ZeroDivisionError:
    print("Cannot divide a number with zero")

except Exception:
    print("Entered value is a string type")

