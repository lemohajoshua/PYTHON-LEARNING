print("meow")
print("meow")
print("meow")

#this program uses a while loop to print "meow" three times. The variable i is initialized to 3, and the loop continues as long as i is not equal to 0. Inside the loop, it prints "meow" and then decrements the value of i by 1. When i reaches 0, the loop terminates
i = 3
while i != 0:
    print("meow")
    #this line decrements the value of i by 1, which is necessary to eventually terminate the loop. Without this line, the loop would run indefinitely because i would always be equal to 3. 
    #i = i - 1
    i -= 1