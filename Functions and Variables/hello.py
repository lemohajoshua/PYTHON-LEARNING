# Ask user their name
name = input("What is your name? ")

#remove any Leading or trailing whitespace from the name and capitalise the user's name
name = name.strip().title()

# Say Hello user name
print("Hello, " + name)
print("Hello", name , "Welcome to the programming world!")

print("hello,", name, sep=" ")

#the f-string method (this f tells python that this is a format string)
print(f"hello, {name}")


