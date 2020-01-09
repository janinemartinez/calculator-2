import arithmetic

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
        print(arithmetic.add(tokens[1], tokens[2]))



while True:

    tokens = user_input()

    if tokens[0] == "Q" or tokens[0] == "q" or tokens[0] == "Quit" or tokens[0] == "quit" or tokens[0] == "QUIT":
        print("Good riddance!")
        break

    call_arithmetic_functions(tokens)

