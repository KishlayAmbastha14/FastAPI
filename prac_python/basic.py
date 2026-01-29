# # # # # Online Python compiler (interpreter) to run Python online.
# # # # # Write Python 3 code in this online editor and run it.
# # # # print("Try programiz.pro")

# # # # dict1 = {"a":4,"b":5,"c":7}
# # # # print(dict1.items())
# # # # ans = dict()
    
# # # # print(dict1['a'])
# # # # print(dict1.get('b'))
# # # # print(dict1.get('f',0))
# # # # print(dict1.get('z'))

# # # # k = [1,2,3]
# # # # j = k
# # # # j.append(4)
# # # # print(k)
# # # # print(id(k))
# # # # print(id(j))
# # # # print("\n")

# # a = [1,2,3]
# # print(a.pop(1))
# # # # b = a.copy()
# # # # a.append(4)
# # # # b.append(9)
# # # # print(a)
# # # # print(b)
# # # # print(id(a))
# # # # print(id(b))

# # # # a = [[1,2], [3,4]]

# # # # b = a.copy()
# # # # # b[0].append(9)
# # # # b.extend([5,6])

# # # # print(a)
# # # # print(b)

# # # a = [[1,2], [3,4]]
# # # b = a.copy()
# # # b[0] = [8,9]
# # # print(b)
# # # print(a)


# # # d1 = {"x":[4,5,6]}
# # # d2 = d1.copy()
# # # d1["x"].append(7)
# # # print(d1)
# # # print(d2)



# # # d3 = {"x":[4,5,6]}
# # # d4 = d3.copy()
# # # d3["x"] = 8
# # # print(d3)
# # # print(d4)

# # # s1 = {1,2,3}
# # # s2 = s1.copy()
# # # s1.add(6)
# # # print(s1)
# # # print(s2)


# # # s3 = {1,2,3}
# # # s4 = s3
# # # s3.add(6)
# # # print(s3)
# # # print(s4)
# # # print(f"len of s3 is {len(s3)}")







# # a = [3,2,1,5]
# # b = sorted(a)
# # print(a,b)

# # print(list(enumerate(["a","b","c"])))

# # res = (list(zip([1,2,3],['a','b'])))
# # print(res)

# # print(any([0,False,5]))
# # print(all([0,False,5]))
# # print(all([1,True]))

# # k = ['a','b','c']
# # print("-".join(k))

# # l = "a,b,c"
# # print(l)
# # print(l.strip(","))
# # a = {1,2,3}
# # b = {3,4,5}
# # print(a & b)
# print(type(type(int)))
# print(3==3.0)
# x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
# print(x[1][2][1])

# x = 5
# def change():
#     global x
#     x = 10
# change()
# print(x)

# # d1 = {"a":1,"b":2}
# # print(d1.items())
# # print(list(d1.items())[0])

prices = [100, 250, 50, 400]
rest = list(filter(lambda x : x>=200 , prices))
print(rest)
rest_map = list(map(lambda x : x+100 , prices))
print(rest_map)

checks = [True,True,False]
print(all(checks))
print(any(checks))

names = ['login','logout']
for index,name in enumerate(names,start=0):
    print(f"{index}:{name}")

## ZIP
keys = ['id','status']
values = [1,0],['active','non-active']

mapping = dict(zip(keys,values))
print(mapping)

age = 5
print(isinstance(age,float))

foo = [print(i) for i in range(5)]
print(foo)

a = ['one','two','three']
b = a.pop(1)
c = a
print('c[0]', 'b', 'c[1]')

def custom_function(data):
    for i in range(len(data)):
        if i % 2 == 0:
            data[i] = True
        else:
            data[i] = False
    return data
# What will be the output when
ans = custom_function([0, 0, 0, 0, 0])
print(ans)

# numbers = [1, 2, 3]
# # and a tuple
# data = (4, 5, 6)
# # , what will be the output of the command
# numbers.append(data)
# print(numbers)

# num_list = [34,12,93,783,330,896,1,55]
# result = (lambda x: (x%10==0),num_list)
# print(result)


# # d = {"a":1,"b":2}
# # print("a" in d)
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9]
# list1.extend(list2)
# print(list1)

# def test(**kwargs): 
#   for i in kwargs: 
#      print(i, kwargs[i]) 
# test(name='John', age=22)

# a = [1,2,3]
# # b = a.extend([4,5])
# print(a.extend([4,5]))
# # print(a)
# # print(b)
# a = [1,2,3]
# print(a.extend([4,5]))


# # a = [{"x":1},{"x":2}]
# # print([d["x"] for d in a])

