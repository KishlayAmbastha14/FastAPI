# ---

# ### 🚀 Top 10 Practice Questions (Basic to Advanced)

# Ye questions solve kar liye toh interview aur backend development dono set hain:

# 1.  **Numbers:** `1 se 20` tak ke numbers ki list banao jo sirf `3` se divisible hon.
a = []
for i in range(21):
  if i%3==0:
    a.append(i)
  
b = [i for i in range(21) if i%3==0]
# print(b)
# print(a)

# 2.  **Filtering:** Ek list `names = ["Kishlay", "Amit", "Ankan", "Raj"]` se wo names nikalo jo **'A'** se shuru hote hain.
names = ["Kishlay", "Amit", "Ankan", "Raj"]

anss = [i for i in names if not i.startswith("A")]
print(anss)


def my_decorator(my_fun):
  print("hlo 1")
  def my_closure():
    print("hlo 2")
    my_fun()
    print("hlo 3")
  return my_closure
  
@my_decorator
def my_Func_hlo():
  print("hloo kaise hoo ")

my_Func_hlo()

def source_1():
  yield "DATA A"
  yield "DATA B"

def source_2():
  yield "DATA C"
  yield "DATA D"


def combined_gen():
  yield from source_1()
  yield from source_2()

try: 
  for item in combined_gen():
    print(item)
except Exception as e:
  print(e)


names = ["kislay","rohan","akarsh","aditya"]
scores = [200,399]

from itertools import zip_longest
# print(tuple(zip(names,scores)))
# print(list(zip(names,scores)))
# print(dict(zip_longest(names,scores,fillvalue=0)))


# 3.  **Dict Mapping:** `keys = ['a', 'b']` aur `values = [1, 2]` hain. Bina `zip()` ke sirf comprehension se `{ 'a': 1, 'b': 2 }` banao.

keys = ['a','b']
values = [1,2]

ans = {keys[i]: values[i] for i in range(len(keys))}
# print(ans)

# Q.3.2 Aapke paas do lists hain: roll_nos = [101, 102, 103] aur names = ['Rahul', 'Ankit', 'Sneha']. Aapko ek aisi dictionary banani hai jisme Roll Number 'key' ho aur Name 'value' ho. Kaunsa code fragment sahi result dega?
roll_nos = [101,102,103]
names = ['Rahul', 'Ankit', 'Sneha']
# print(len(roll_nos))
ans2 = {roll_nos[i]:names[i] for i in range(len(roll_nos))}
# print(ans2)


# 4.  **Data Cleaning:** Ek list `prices = ["$100", "$200", "$500"]` se `$` hatao aur numbers ko `int` mein convert karo.

prices = ["$100", "$200", "$500"]
ans = [int(i.removeprefix("$")) for i in prices ]
# print(ans)
# print(prices)
# print(type(ans[0]))

# 5.  **Set Power:** Ek string `sentence = "hello world hello python"` se unique characters ki list banao jo space na ho.

sentence = "hello world hello python"
print(list(set(sentence.split(" "))))

# Task 1: The Character Counter
# Do lists hain: chars = ['a', 'b', 'a', 'c', 'b'] aur counts = [1, 2, 3, 4, 5]. Bina zip() ke ek dictionary banao { 'a': 1, 'b': 2, 'c': 4 }. (Hint: Agar key pehle se dictionary mein hai, toh use dobara update mat karo. Isse sirf pehli baar waali value save hogi).

chars = ['a', 'b', 'a', 'c', 'b']
counts = [1, 2, 3, 4, 5]


result = {}

for i in range(len(chars)):
  key = chars[i]
  value = counts[i]
  if key not in result:
    result[key] = value

print(result)

# Task 2: Filter & Map
# numbers = [1, 2, 3, 4, 5, 6] Ek dictionary comprehension se aisi dictionary banao jahan Key number ho aur Value uska square ho, lekin sirf Even numbers ke liye. Expected Output: {2: 4, 4: 16, 6: 36}

numbers = [1,2,3,4,5,6]
reslt = {}

for i in range(len(numbers)):
  # print(numbers[i])
  if numbers[i] %2 == 0:
    reslt.update({numbers[i] : numbers[i] ** 2})
    # reslt[numbers[i]] = numbers[i] ** 2

print(reslt)

reslts = {numbers[i]: numbers[i]**2 for i in range(len(numbers)) if numbers[i]%2==0}
print(reslts)


# 6.  **Conditional (If-Else):** Ek list `nums = [1, 2, 3, 4, 5]` lo. Agar number even hai toh `"Even"` likho, odd hai toh `"Odd"`. (Hint: `[exp_if_true if cond else exp_if_false for i in list]`).
nums = [1,2,3,4,5]
ans = ["even" if i%2==0 else "odd" for i in nums]
print(ans)



# 7.  **Nested List:** Ek Matrix `[[1, 2], [3, 4]]` ko flatten karke single list `[1, 2, 3, 4]` banao.
l1 = [[1,2] ,[3,4]]
ans = []
for i in l1:
  for j in i:
    ans.append(j)
print(ans)

# 8.  **Backend Mock:** Ek dict `inventory = {"apple": 10, "orange": 0, "banana": 5}` se sirf wo items nikalo jinka stock `> 0` hai.
inventory = {"apple": 10, "orange": 0, "banana": 5}
# for i in range(len(inventory)):
  # print(inventory[i])
new_dict = dict()
for key,value in inventory.items():
  # print(key,value)
  if value > 0:
    new_dict.update({key:value})

# print(new_dict)


# 9.  **Vowels Check:** Kisi string se saare vowels (`a,e,i,o,u`) nikal kar unka set banao.

# 10. **FastAPI Style:** Aapke paas list of dicts hai `users = [{"id": 1, "name": "Kishlay"}, {"id": 2, "name": "Amit"}]`. Isse ek naya dict banao jahan key `id` ho aur value `name`. Output should be: `{1: "Kishlay", 2: "Amit"}`.

users = [{"id": 1, "name": "Kishlay"}, {"id": 2, "name": "Amit"}]

new_dictt = dict()
# print(users[0])
for i in users:
  idd = i.get('id')
  namee = i.get('name')
  # print(idd,namee)
  new_dictt.update({idd:namee})

print(new_dictt)
# ---

# ### **Aapka Next Step:**
# Inme se koi bhi 3-4 solve karke mujhe dikhao, khaas karke **Question 6 (If-Else)** aur **Question 10 (FastAPI style)**. Ye dono thode tricky hain! 

# Kya main Question 6 ka syntax samjhaun? Isme `if` piche nahi, beech mein aata hai.