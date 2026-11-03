'''
x = int(input("What is x? "))

#This program checks if x is even or odd, which is determined by the remainder of x divided by 2. If the remainder is 0, then x is even; otherwise, it is odd.
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
'''

#the program below uses a function to check if x is even or odd. The function is_even() takes an integer n as input and returns True if n is even and False if n is odd. The main() function prompts the user for input, calls the is_even() function, and prints whether the number is even or odd.
def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")

'''
#the is_even() function checks if the input number n is even or odd by using the modulus operator %. If n is divisible by 2 (i.e., n % 2 == 0), then it returns True, indicating that n is even. Otherwise, it returns False, indicating that n is odd.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
'''
#instead of using an if-else statement, we can simplify the is_even() function to return the result of the expression n % 2 == 0 directly. This will return True if n is even and False if n is odd.
def is_even(n):
    return n % 2 == 0

main()