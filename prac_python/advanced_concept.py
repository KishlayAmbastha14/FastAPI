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
  }
]

# print(db)
# print(type(db))
for l1 in db:
  for key,value in l1.items():
    # print(key,value)
    if value == 1:
      print("hiii")
  # if i.get("id") == 2:
  #   print(i.get("name"))
  # print(i)
  # print(key)


for _todo in db:
  print(_todo.items())