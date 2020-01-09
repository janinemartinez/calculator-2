from arithmetic import *

def user_input():

    prefix = input("> ")
    tokens = prefix.split(" ")
    for i in range(len(tokens)):
        if i > 0:
            tokens[i] = float(tokens[i])

    print(tokens)
    return tokens


def call_arithmetic_functions(tokens):
    if tokens[0] == "+":
        print(add(tokens[1], tokens[2]))
    elif tokens[0] == "-":
        print(subtract(tokens[1], tokens[2]))
    elif tokens[0] == "*":
        print(multiply(tokens[1], tokens[2]))
    elif tokens[0] == "/":
        print(divide(tokens[1], tokens[2]))
    elif tokens[0] == "square":
        print(square(tokens[1]))
    elif tokens[0] == "cube":
        print(cube(tokens[1]))
    elif tokens[0] == "pow":
        print(power(tokens[1], tokens[2]))
    elif tokens[0] == "mod":    
        print(mod(tokens[1], tokens[2]))
    elif tokens[0] == "x+":
        print(add_mult(tokens[1], tokens[2], tokens[3]))
    elif tokens[0] == "cube+":
        print(add_cubes(tokens[1], tokens[2]))
    else:
        print("INVALID INPUT, PLEASE TRY AGAIN!")


while True:

    tokens = user_input()

    if tokens[0] == "Q" or tokens[0] == "q" or tokens[0] == "Quit" or tokens[0] == "quit" or tokens[0] == "QUIT":
        print("Good riddance!")
        break

    call_arithmetic_functions(tokens)

