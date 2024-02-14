import names, random

dict = {}

for i in range (1,5):
    age = random.randint(20,30)
    name = names.get_first_name("female")
    dict[name]=age
print(dict)

for name in dict:
    print(f"Value of name is {name}")
    print(f"Value of {name} is {dict[name]}")


 

