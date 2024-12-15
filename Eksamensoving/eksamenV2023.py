# #Oppgave 1
# x = hello
# y = x.upper()
# print(y)

# #Oppgave 2
# lst = [1, 2, 3]
# lst.insert(1, 4)
# print(lst)

# #Oppgave 3
# d = {"apple": 2, "banana": 3, "cherry": 5}
# print(d["cherry"])

# for i in range(2, 7, 2):
#     print(i)

# def add_nums(a, b=2):
#     return a + b
# print(add_nums(2))

# def count_vowels(s):
#     vowels = "aeiou"
#     count = 0
#     for c in s:
#         if c in vowels:
#             count += 1
#     return count
# print(count_vowels("hello world"))

# lst = [1, 2, 3]
# lst.remove(2)
# print(lst)

# lst1 = [1, 2, 3]
# lst2 = lst1
# lst2.append(4)
# print(lst1)

# d = {"apple": 2, "banana": 3, "cherry": 5}
# for k, v in d.items():
#     print(k, v)

# lst = [1, 2, 3, 4, 5]
# lst2 = lst[2:10]
# print(lst2)

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# print(fib(5))

# def foo(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = filter(foo, lst)
# print(list(res))

# lst1 = [1, 2, 3, 4]
# lst2 = []
# for x in lst1:
#     if x % 2 == 0:
#         lst2.append(x * 2)
# print(lst2)

# def foo(x, y):
#     z = x + y
#     return z
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# res = []
# for x in lst1:
#     for y in lst2:
#         res.append(foo(x, y))
# print(res)

# def foo(lst):
#     return lst[::-1]
# lst1 = [1, 2, 3, 4, 5]
# lst2 = foo(lst1)
# lst2[0] = 0
# print(lst2)

# liste = [1,2,3,4,5,6]

# print(liste[::2])

# def foo(lst):
#     res = []
#     for i in range(len(lst)):
#         if i % 2 == 0:
#             res.append(lst[i])
#     return res
# lst1 = [1, 2, 3, 4, 5]
# lst2 = foo(lst1)
# lst2[1] = 0
# print(lst2)