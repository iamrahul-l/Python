ip_add = set()
with open('set\log.txt', 'r') as filerdr:
    for line in filerdr:
        ip_add.add(line.strip().split(' ')[0])
print(f"The set {ip_add}")
print(f"The length of set {len(ip_add)}")
                

# for ip in ip_add:
    
#     set_ip = set(ip_add)
# print(f"The length of set ip adress {len(set_ip)} ")    
# print(set_ip)  
# print(f"The length of ip adress {len(ip_add)} ")    
# print(ip_add) 
        
