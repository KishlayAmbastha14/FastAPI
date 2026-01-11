from typing import List,Dict,Optional
from fastapi import FastAPI


app = FastAPI(title='revision mode')

def students_name(first_Name:str, last_Name:str):
    total_name = first_Name.title()+ " " + last_Name.title()
    print(total_name)

def students_List(items:List[str]):
    for item in items:
        print(item)

def processing_items(prices:Dict[str,float]):
    for item_name,item_price in prices.items():
        print(item_name)
        print(item_price)

# it means items could be string or float any things 
def items(item:str|float):
    print(item)

# OPTIONAL

def optin(name:Optional[str] = None):
    if name is not None:
        print(f"hello buddy {name}")
    else:
        print(f"none is none")


async def namess(name:str|None = None):
    if name is not None:
        print(f"hello {name}")
    else:
        print("you dont have name")



# @app.get("/")
# async def calling():
#     result = await namess("rohan")
#     return result

# @app.get("/")
# async def called():
#     # results = optin("kishlay")
#     return {"hello to fastapi"}
#     # return results

@app.get("/run")
async def run():
    return {"he is running"}

async def int_number(nam1:str):
    return 'kumar'+nam1

async def float_number(nam2:str):
    return 'rohan'+nam2

@app.get("/")
async def called():
    # a1 = await int_number(5)
    # a2 = await float_number(7.3)
    a1 = await int_number("rohan")
    a2 = await float_number("kuumarrr")
    return a1 +" " +  a2
    # results = optin("kishlay")
    # return {"hello to fastapi"}
    # return results

if __name__ == "__main__":
    # students_name("rohan","kumar")
    # students_List(['kishaly','rohan','rahul'])
    # processing_items({'maggi':34,'apple':40})
    # items("apple")
    # namess()
    # run()
    called()
