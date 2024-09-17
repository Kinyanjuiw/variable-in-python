x = "good"
def myfunc():
    global x
    x = "awesome"
    print("my day was " + x);
myfunc()
print("my day is " +  x)


