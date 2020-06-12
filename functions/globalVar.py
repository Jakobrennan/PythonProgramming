# basic use of global variable

def notAffectGlobal():
    value = -10
    print("value from notAffectGlobal() is : " + str(value))

def affectGlobal():
    global value
    value = -10
    print("print 'value' from within affectGlobal() : " + str(value))

value = 10
print("initial value: " + str(value))
notAffectGlobal()
print("value after notAffectGloabl() : " + str(value))
affectGlobal()
print("value after affectGlobal() : " + str(value))
