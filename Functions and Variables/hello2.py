# to define a funtion in python you use the def keyword followed by the function name and parentheses. The code block within every function starts with a colon (:) and is indented.
''''
def hello():
    print("Hello")

name = input("what's your Name? ")
hello()
print(name)
'''

'''
def hello(to):
    #this function takes a parameter 'to' and prints a message using that parameter.
    print("Hello,", to)

name  = input("what's your Name? ")
hello(name)
'''


def main():
    name = input("what's your Name? ")
    hello(name)


def hello(to):
    print("Hello,", to)

main()