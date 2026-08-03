# ==========================================
# OPERATORS IN PYTHON
# ==========================================

a = 20
b = 5

# ------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("----------------------------")

# ------------------------------------------
# 2. Comparison Operators
# ------------------------------------------

print("Comparison Operators")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("----------------------------")

# ------------------------------------------
# 3. Assignment Operators
# ------------------------------------------

print("Assignment Operators")

x = 10

x += 5
print("+= :", x)

x -= 2
print("-= :", x)

x *= 2
print("*= :", x)

x /= 2
print("/= :", x)

print("----------------------------")

# ------------------------------------------
# 4. Logical Operators
# ------------------------------------------

print("Logical Operators")

x = True
y = False

print("AND :", x and y)
print("OR  :", x or y)
print("NOT :", not x)

print("----------------------------")

# ------------------------------------------
# 5. Membership Operators
# ------------------------------------------

print("Membership Operators")

fruits = ["Apple", "Banana", "Orange"]

print("Apple" in fruits)
print("Mango" not in fruits)

print("----------------------------")

# ------------------------------------------
# 6. Identity Operators
# ------------------------------------------

print("Identity Operators")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 == list3 :", list1 == list3)

print("----------------------------")

# ------------------------------------------
# 7. Bitwise Operators
# ------------------------------------------

print("Bitwise Operators")

a = 5
b = 3

print("AND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)
print("NOT :", ~a)
print("Left Shift :", a << 1)
print("Right Shift:", a >> 1)