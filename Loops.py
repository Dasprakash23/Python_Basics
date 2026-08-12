# ==========================================
# LOOPS IN PYTHON
# ==========================================


# 1. For loop
print("For Loop")

for i in range(5):
    print(i)


print("----------------------------")


# 2. Print numbers from 1 to 10
print("Numbers from 1 to 10")

for i in range(1, 11):
    print(i)


print("----------------------------")


# 3. Even numbers from 1 to 10
print("Even Numbers")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


print("----------------------------")


# 4. Multiplication table
number = 5

print("Multiplication Table")

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


print("----------------------------")


# 5. Loop through a list
fruits = ["Apple", "Banana", "Orange"]

print("Fruits")

for fruit in fruits:
    print(fruit)


print("----------------------------")


# 6. While loop
print("While Loop")

count = 1

while count <= 5:
    print(count)
    count += 1


print("----------------------------")


# 7. Break
print("Break Example")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


print("----------------------------")


# 8. Continue
print("Continue Example")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


print("----------------------------")


# 9. Pass
print("Pass Example")

for i in range(5):
    pass

print("Loop completed")