# fruits = ["apple", "banana", "cherry", "date"]
# fruits[2] = "grape"

# print(fruits[2])

# total = 0
# for num in range(1, 6):
#     total += num

# print(total)

# x = "10"
# y = 2.5
# z = int(x) + y

# print(z)

# numbers = [1, 2, 3, 4, 5]
# sliced = numbers[1:4]

# print(sliced)

# for i in range(5):
#     if i == 3:
#         break
#     else:
#         print("Done")

# x_value = 1.0e10
# increment= 1.23e-10
# for i in range(20):
#     x_value = x_value + increment

# print(x_value)

# b = 1

# def bracketing( func ):
#     for a in range(100):
#         if func(b) == 0:
#             return b, b
#         elif b > 0:
#             if func(a)*func(b) < 0:
#                 return a, a+1
#             else:
#                 return None

# try:
#     value = int("abc")
# except ValueError:
#     value = 0

# print(value)

# numbers = [1, 2, 3, 4, 5, 6, 7, 9]
# eve = []
# for num in numbers:
#     if num % 3 == 0:
#         eve.append(num)

# print(eve)

# data = {"name": "Alice", "age": 25, "country": "USA"}
# data["city"] = "New York"

# print(len(data))

# student_grades = {"Alice": 90, "Bob": 80, "Carol": 95}
# temp = 0
# for grade in student_grades.values():
#     if grade > temp:
#         temp = grade

# print(temp)

# for i in range(3):
#     for j in range(2):
#         print(i + j, end=" ")

# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     numbers[i] += 10
# print(numbers)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# result = factorial(5)
# print(result)

def greet(name, greeting="Hello"):
    return greeting + ", " + name
message = greet("Alice")
print(message)