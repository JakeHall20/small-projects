'''
Jacob Hall
Implementation of FizzBuzz
Using Python 3.7.2
IDE: Atom
'''
################################################################################
# First Implementation - with if statements
def FizzBuzz1():
    for i in range(1, 101, 1):
        if i % 15 == 0:         # if divisible by both 3 & 5
            print("FizzBuzz")
        elif i % 3 == 0:        # just divisible by 3
            print("Fizz")
        elif i % 5 == 0:        # just divisible by 5
            print("Buzz")
        else:                   # not divisible by either
            print(i)
################################################################################
def MultiplesOf3(fizzBuzzDict):
    # loop from 3 to 100, stepping up by 3 each time
    for i in range(3, 101, 3):
        fizzBuzzDict[i] = "Fizz"
def MultiplesOf5(fizzBuzzDict):
    # loop from 5 to 100, stepping up by 5 each time
    for i in range(5, 101, 5):
        fizzBuzzDict[i] = "Buzz"
def MultiplesOfBoth(fizzBuzzDict):
    # loop from 15 to 100, stepping up by 15 each time
    for i in range(15, 101, 15):
        fizzBuzzDict[i] = "FizzBuzz"
# Second Implementation - without if statements
def FizzBuzz2():
    # creating the dictionary of 1 - 100
    fizzBuzzDict = {i:i for i in range(1, 101, 1)}
    # divisible by 3
    MultiplesOf3(fizzBuzzDict)
    # divisible by 5
    MultiplesOf5(fizzBuzzDict)
    # divisible by 3 and 5
    MultiplesOfBoth(fizzBuzzDict)

    [print(fizzBuzzDict[i]) for i in fizzBuzzDict]

if __name__=="__main__":
    FizzBuzz1()
    print()
    FizzBuzz2()
