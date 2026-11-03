'''
score =int(input("Student Score: "))
if 80 <= score <= 100:
    print("Grade: A")
elif 60 <= score < 80:
    print("Grade: B")
elif 45 <= score < 60:
    print("Grade: C")
else:
    print("Grade: F")
'''

score = int(input("Student Score: "))
if score >= 80:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 45:
    print("Grade: C")
else:
    print("Grade: F")