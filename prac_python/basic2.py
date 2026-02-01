# # a = {1, 2, 3}
# # b = a.copy()

# # b.add(10)
# # print(a)  # {1,2,3}
# # print(b)  # {1,2,3,10}

# # x = 10

# # def my_func():
# #     print(x) # Hum global x ko access kar rahe hain
# #     x = 20 
# #     print(x)# Ab hum use local bana rahe hain

# # my_func()
# # List (Saari memory ek sath le li)

# def adds_item(item,lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst

# print(adds_item(5))
# print(adds_item(6))
# print(adds_item([7]))


# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst
# print(add_item(1))
# # print(add_item(2))

# # my_list = [i for i in range(1000000)] 

# # # Generator (Sirf 'formula' yaad rakha, memory nahi li)
# # my_gen = (i for i in range(1000000)) 

# # print(next(my_gen)) # Ab 0 milega
# # print(next(my_gen)) # Ab 1 milega

# a = [3,4,5,[7,8]]
# print(a[3])
# b = a.copy()
# a[3].append(6)
# print("\n")
# print(id(a[3]))
# print(id(b[3]))
# print("\n")
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# def outer():
#     x = 1
#     print(f"first {x}")
#     def inner():
#          print(f"second {x}")
#     x = 2
#     print(f"third {x}")
#     inner()
#     print(f"fourth {x}")
# outer()


# def my_magic():
#     print("Pehla")
#     yield 1
#     print("Dusra")
#     yield 2

# g = my_magic()
# print(next(g))


# funcs = [lambda x: x + i for i in range(3)]
# for f in funcs:
#     print(f(10))

# def my_decorator(func):
#     def wrapper():
#         print("Bhai, function shuru hone wala hai...")
#         func()
#         print("Bhai, kaam ho gaya!")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Oye, Hello!")

# say_hello()

# # # a = [1,2,3]
# # # b = a
# # # print(id(a))
# # # print(id(b))
# # # print(a is b)

# # # import sys

# # # my_list = [1, 2, 3]
# # # my_tuple = (1, 2, 3)

# # # print(sys.getsizeof(my_list))
# # # print(sys.getsizeof(my_tuple))


db = [
  {
    "id": 1,
    "name": "give me the name",
    "age": 10,
    "course": "string",
    "email": "string"
  },
  {
    "id": 2,
    "name": "give me the name",
    "age": 10,
    "course": "string",
    "email": "string"
  },
  {
    "id": 3,
    "name": "give me the name",
    "age": 10,
    "course": "string",
    "email": "string"
  },
  {
    "id": 5,
    "name": "give me the name",
    "age": 10,
    "course": "string",
    "email": "string"
  }
]

# print(db)


for i in db:
  print(f"this is {i}")
  if i.get("id") == 3:
    break