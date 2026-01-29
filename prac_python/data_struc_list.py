# # 🧪 PART 1 — Core Practice Questions (Write Code)

# # Ye questions sirf list methods par focus karte hain.

# # Q1.
# # Ek list me 5 numbers lo.
# # Last me 100 add karo
# # Phir second index par 50 insert karo
# # Final list print karo.

# res = [31,32,33,34,35]
# # print(res.append(100))
# res.insert(1,50)
# # print(res)

# # Q2.
# a = [1,2,3,4,5]
# # remove() use karke 3 hatao
# # pop() use karke last element hatao
# # Final list print karo.
# a.remove(3)
# ans = a.pop(-1)
# # print(ans)
# # print(a)

# # Q3.

# # Ek list:
# a = [10, 20, 30, 20, 40, 20]
# # count(20) print karo
# # index(30) print karo.

# # print(a.count(20))
# x = a.count(20)
# k = a.index(30)
# # print(x)
# # print(k)


# # Q4.

# # Ek unsorted list lo:

# a = [5, 1, 4, 2, 3]
# b = [5, 1, 4, 2]
# # Descending order me sort karo
# # Phir list reverse karo
# # Final output kya hoga?
# a.sort(reverse=True)
# # print(b.sort(reverse=True))
# # print(a)


# # Q5.
# a = [1,2,3]
# b = a.copy()
# b.append(10)
# # print(a, b)


# # Explain kyun a change nahi hua.

# # 🧪 PART 2 — Tricky Output Questions (Shallow + Methods Mix)
# # Q6.
# a = [1,2,3]
# b = a
# b.pop()
# # print(a)

# # Q7.
# a = [1,2,3]
# b = a.copy()
# b.pop()
# # print(a)
# # print(b)
# # print(id(a), id(b))

# # Q8.
# a = [[1,2],[3,4]]
# b = a.copy()
# b[0].remove(1)
# # print(b)
# # print(a)
# # print(id(a[0]),id(b[0]))

# # Q9.
# a = [1,2,3]
# # print(a.extend([4,5]))
# # print(a)

# # Q10.
# a = [3,1,2]
# x = a.sort()
# # print(x)
# # print(a)

# # 🔥 PART 3 — Backend-Oriented Mini Problems (FastAPI Style)

# # Ye wahi type ke problems hain jo real APIs me aate hain.

# # Q11. Remove Duplicates from Request Data

# # User se list aayi:
# data = [1,2,2,3,4,3,5]
# # Sirf list methods + set use karke
# # Unique list banao preserving order.
# ans = list(set(data))
# # print(ans)

# # Q12. Pagination Logic
# # Given:
# items = list(range(1, 101))  # 1 to 100
# # Page 2 ke 10 items nikaalo using slicing.
# page = 2
# size = 10
# start = (page-1) * size
# end = page * size
# # print(items)
# print(start,end)
# print(items[start:end])


# # Q13. Safe Deletion
# items = [10,20,30,40]
# # Agar 30 list me ho to remove karo
# # Warna kuch bhi error na aaye.

# if 30 in items:
#   items.remove(30)
# print(items)
  


# # Q14. Top 3 Largest Numbers
# a = [10, 4, 7, 20, 15, 3]
# # Top 3 largest numbers nikaalo
# # Using only sort() and slicing.
# a.sort(reverse=True)
# # print(a[:3])

# # Q15. Cleaning Input Data (Very Backend Important)
# raw = ["  apple ", " banana", "APPLE", "Banana "]
# # Sab ko strip karo
# # Lowercase karo
# # Unique list banao (order maintain karo)


# ans = [i.strip().lower()  for i in raw]
# print(ans)

# # res = []
# # for i in ans:
# #   if i not in res:
# #     res.append(i)

# # print(res)

# res2 = sorted(set(ans), key=ans.index)
# print(res2)

# res3 = list(dict.fromkeys(i.strip().lower() for i in raw))

# print(res3)

# k = list(dict.fromkeys(i.strip().lower() for i in raw))
# print(k)


# user_input = " ###Kishlay_Kumar_2026### "
# # Pehle aur aakhri ke spaces hatao.
# # Dono side ke '###' symbol ko remove karo (Hint: strip() mein characters pass kiye ja sakte hain, jaise strip('#')).
# # Jahan _ (underscore) hai, wahan space daal do.
# # Pure string ko Uppercase mein badlo.

# # print(user_input.strip('#'))
# ans = user_input.strip("# ")
# ans2 = ans.replace("_","").upper()
# print(ans)
# print(ans2)

# raw_data = " ID-405: Error found in the system. Status: CRITICAL "
# ans = raw_data.split(":")
# message = ans[2].strip()
# print(message)
# print(ans)

# res = message.endswith("CRITICAL")

# print(f"Clean Message: '{message}'")
# print(f"Ends with CRITICAL?: {res}")







# # Question: Ek input string ref_code = "INV-9928". Check karo kya ye "INV-" se shuru hota hai? Agar haan, toh sirf number wala part (9928) alag nikal kar dikhao.

# s1 = "INV-9928"
# if s1.startswith("INV-"):
#   ans = s1.split("-")
#   print(ans[1])
# # 4. Advance "FastAPI Type" Backend Challenge
# # Ab ek advanced logic try karte hain jo aapko FastAPI models banate waqt kaam aayega.

# # Scenario: Aapke paas ek raw string aayi hai jo ek sensor se mil rahi hai: raw_payload = "TEMP:32.5;HUMID:65;LOC:Kolkata_Flat"

# # Task: 1. Is string ko ; se split karke ek list banao. 2. Us list se sirf LOC wala part nikalo. 3. LOC ke value (Kolkata_Flat) mein se _ hata kar space dalo. 4. Final location ko lowercase mein print karo.
# raw_payload = "TEMP:32.5;HUMID:65;LOC:Kolkata_Flat"
# ans = raw_payload.split(";")
# res = ans[2].replace("_"," ").lower()
# # final = "".join(res)
# print(res)
# # 🔥 Pro-Tip for your FastAPI/NLP Path:
# # Backend mein jab aap Pydantic Models banayenge, toh aap @validator ka use karenge. Wahan ye string methods gold ki tarah kaam aate hain.

# # Example (Aise click karega):

# # Data Validation? -> Use isdigit(), isalpha(), startswith().

# # Data Cleaning? -> Use strip(), replace().

# # Parsing (Data todna)? -> Use split().

# # Kya aap upar wala Advanced Challenge solve kar sakte hain? Ye exact waisa hi logic hai jo aap apne RAG chatbot ya crop prediction project ke backend mein use karenge.




# # Python

# # Task:

# Filter: Sirf un users ko nikalo jo is_active: True hain.
# Map: Jo filtered users mile, unke name ko Uppercase kar do.
# Final Step: len() use karke batao kitne active users mile.
# Click Concept: * Jab bhi list ko channa ho ⮕ Use filter.
# Jab bhi list ko badalna ho ⮕ Use map.
# Jab bhi check karna ho sab sahi hai? ⮕ Use all.
db_users = [
    {"id": 1, "name": "kishlay", "is_active": True},
    {"id": 2, "name": "amit", "is_active": False},
    {"id": 3, "name": "rahul", "is_active": True}
]

ans = list(filter(lambda x : x.get("is_active") , db_users))
def update_name(user):
  user['name']  = user['name'].upper()
  return user

final_data = list(map(update_name,ans))
ans3 = len(ans)
# print(ans3)
# print(final_data)



# # Python

# # Task:
# # Check karo any() use karke: Kya koi item out of stock hai? (in_stock == False)
# # filter() use karke sirf "In Stock" items ki list banao.
# # map() use karke un items par 10% discount apply karke naya price dikhao. (Formula: price * 0.9)

# orders = [
#     {"item": "Laptop", "price": 50000, "in_stock": True},
#     {"item": "Mouse", "price": 500, "in_stock": False},
#     {"item": "Monitor", "price": 10000, "in_stock": True}
# ]

# ## 1
# has_in_stock_false = any(not item["in_stock"]  for item in orders)
# print(has_in_stock_false)

# ## 2 
# in_stocks = (list(filter(lambda x: (x.get("in_stock")),orders)))
# print(in_stocks)

# def discount_10(order):
#   new_order = order.copy()
#   new_order['price'] = int(new_order['price'] * 0.9)
#   return new_order
# # print(500*0.9)
# discount = list(map(discount_10 , orders))
# print(discount)

# print(orders)


# Scenario: Ek user ne registration form bhara: user_form = {"username": "kishlay", "email": "k@pro.com", "password": ""}

# Task:
user_form = {"username": "kishlay", "email": "k@pro.com", "password": ""}

# print(user_form['email'])
# is_filled = all(not i for i in user_form)
# print(is_filled)

is_filled = all(user_form.values())
print(is_filled)

is_filled_key = all(user_form.keys())
print(is_filled_key)

if not is_filled:
    print("❌ Error: Please fill all fields (Password is missing!)")
else:
    print("✅ Success: Form is complete")

# print(f"Result of all(): {is_filled}")


projects = [
    {"title": "RAG Chatbot", "tech": ["Python", "LangChain", "FastAPI"], "status": "completed"},
    {"title": "Portfolio Web", "tech": ["React", "Vite", "Tailwind"], "status": "in-progress"},
    {"title": "Crop Recommendation", "tech": ["Python", "ML", "Scikit-learn"], "status": "completed"},
    {"title": "Discord Bot", "tech": ["Python", "Discord.py"], "status": "completed"}
]

print(projects)

def is_compeleted(num):
  new_num = num.copy()
  if new_num['status'] == "completed":
    return new_num

def is_python(num):
  new_num = num.copy()
  for n in new_num:
    if n.find("Python"):
     return new_num
    
result = list(filter(is_compeleted,projects))
# print(result)
ans = list(map(is_python,result))
# print(ans)

python_completed_titles = [p for p in projects if p['status'] == 'completed' and 'Python' in p['tech']]
# print(python_completed_titles)


## SET
skills_i_have = {"Python", "FastAPI", "ML"} 
job_requirements = {"Python", "React", "NodeJS"}

print(skills_i_have & job_requirements)
print(skills_i_have - job_requirements)

