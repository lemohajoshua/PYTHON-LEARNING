name = input("What is your Name? ")

'''
#this program uses a match statement to check the value of the variable name and print the corresponding house in Hogwarts. If the name is "Joeck", "Hermione", or "Ron", it prints "Gryffindor". If the name does not match any of these cases, it prints "Who?".
match name:
    case "Joeck":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    #then this case statement is used to handle any other input that does not match the previous cases. It prints "Who?" to indicate that the name is not recognized.
    case _:
        print("Who?")
'''

match name:
    #this case statement uses the pipe operator | to combine multiple cases that have the same output. If the name is "Joeck", "Hermione", or "Ron", it prints "Gryffindor". If the name does not match any of these cases, it prints "Who?".
    case "Joeck" | "Hermione" | "Ron":
        print("Gryffindor")
    case _:
        print("Who?")