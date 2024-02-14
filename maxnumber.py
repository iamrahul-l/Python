import random
list = []
for randomNumbers in range(1,6):
    randNum = random.randint(1,1000)
    list.append(randNum)

max_num = list[0]
print(f"Max number in the list is {max_num}")
print(list)
for element in list:
   if element > max_num: 
    max_num= element
print(f"The max num is : {max_num}")       