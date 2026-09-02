# Student Database Dynamic Variable
first_name = input("What is your first name? ")
second_name = input("What is your surname? ")
age = input("What is your age? ")
gender = input("What's your gender? ")
student = input("Are you a student? ")
gpa = input("What is your gpa? ")

first_name = str(first_name)
second_name = str(second_name)
age = int(age)
gender = str(gender)
student = bool(student)
gpa = float(gpa)


print("First Name:", first_name)
print("Second Name:", second_name)
print("Age: ", age)
print("Gender: ", gender)
print("Student: ", student)
print("GPA: ", gpa)

if age >= 18:
    print(first_name, "is an adult.")
else:
    print(first_name, "is a minor.")

if student:
    print(first_name, "is currently a student.")
else:
    print(first_name, "is not currently a student.")

if gpa >= 3.5:
    print("That's a great GPA!")
elif gpa >= 2.0:
    print("That's a solid GPA.")
else:
    print("There's room to bring that GPA up.")