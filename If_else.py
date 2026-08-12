# ==========================================
# IF, ELIF AND ELSE IN PYTHON
# ==========================================


# 1. Simple if
age = 20

if age >= 18:
    print("You are an adult")


print("----------------------------")


# 2. if and else
age = 16

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


print("----------------------------")


# 3. if, elif and else
marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


print("----------------------------")


# 4. Check whether a number is positive, negative or zero
number = -5

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


print("----------------------------")


# 5. Find the largest of two numbers
a = 25
b = 40

if a > b:
    print("A is larger")
elif b > a:
    print("B is larger")
else:
    print("Both are equal")


print("----------------------------")


# 6. Check even or odd
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


print("----------------------------")


# 7. Nested if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("ID is required")
else:
    print("You are not eligible")