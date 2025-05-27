mystring = "hello"
myfloat = 10.0
myint = 20

# This code checks the type and value of variables and prints them if they match the expected values.
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
