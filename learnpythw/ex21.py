def add(a,b):
    print "Adding {0} + {1}".format(a, b)
    return a + b

def subtract(a, b):
    print "Subtracting {0} - {1}".format(a, b)
    return a - b

def multiply(a, b):
    print "Multiplying {0} * {1}".format(a, b)
    return a * b

def divide(a, b):
    print "Dividing {0} / {1}".format(a, b)
    return a / b

print "Let's do some math with just functions."

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

kwargs = {
    'age': age,
    'h': height,
    'w': weight,
    'iq': iq
}

print "Age: {age}, Height: {h}, Weight: {w}, IQ: {iq}".format(**kwargs)

# A puzzle for extra credit, type it in anyway
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
