#this is the main function that will be called when the program is run
def main():
    x = int(input("What is the value of x: "))
    print("X squared is: ", square(x))

#this function takes a number as input and returns the square of that number
def square(n):
    #return n*n
    return pow(n, 2)

main()