from faker import Faker
from random import randint

fake_info = {}
fake = Faker()
for num in range(1,100):
  name = fake.name()
  age = randint(10,30)
  address = fake.address()
  info = f"The Age is {age}. The Address is {address}"
  fake_info[name]= info

with open('file1.txt','w') as FileWr:
  for key, value  in fake_info.items():
    FileWr.write(f"The Name {key} ==> {value}\n")




