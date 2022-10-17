# Programming portfolio - Week four
from statistics import mean

def inRange(val):
    if val >= 0 and val <= 100:
        return True
    else:
        return False

def letters(msg):
    upper = 0
    lower = 0
    for c in msg:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1
    return upper, lower

print(letters("This is a Test Message!"))

def greeting():
    name = input("What is your name?")
    print("Greetings", name.capitalize())

greeting()

def lastLetter():
    msg = input("What is your message?")
    if len(msg) > 1:
        msg = msg[:-1]
    return msg

print(lastLetter())

def convertToFahrenheit(deg):
    return (deg * 9/5) + 32

def convertToCelcius(fa):
    return (fa - 32) * 5/9

def fahrenheitConverter():
    c = input("What would you like to convert to fahrenheit? (include C)")
    c = c.strip("C")
    print(convertToFahrenheit(float(c)), "F")

fahrenheitConverter()

def temperatures():
    temps = []
    while True:
        val = input("Enter a value: ")
        if val != "":
            temps.append(convertToFahrenheit(float(val)))
        else:
            break

    print("Min: ", min(temps))
    print("Max: ", max(temps))
    print("Mean: ", mean(temps)) # Uses the statistics library for ease

temperatures()