'''
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

z = int(x) + int(y)
print(z)
'''

'''
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print(x + y)
'''


x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
# Round the result to the nearest integer
Z = round (x + y)

#to format the number with commas as thousands separators, you can use the format specifier `:,` in an f-string. This will automatically add commas to the number for better readability.
print(f"{Z:,}")