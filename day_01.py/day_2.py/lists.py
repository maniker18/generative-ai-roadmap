# # sports = ["cricket", "football", "basketball", "tennis"]
# # # s1=sorted(sports) # cricket
# # # print(s1)
# # # s1.remove("cricket") # 0
# # # print('tennis' in sports) # True

# # # for ind, sport in enumerate(sports,start=1):
# # #     print(f"{ind}: {sport}")


# # set1 = set(sports)
# # set2 = {'boxing', 'badminton', 'volleyball', 'cricket'}

# # print(set1.intersection(set2)) # {'cricket'}
# # print(set1.union(set2))
# # print(set1.difference(set2)) # {'cricket', 'football', 'tennis', 'basketball'}
# # print(set2.difference(set1)) # {'boxing', 'badminton', 'volleyball'}




# dict1 = {'name': 'Manik', 'age': 25, 'city': 'New York'}
# dict1.update({'age': 26, "course": 'cse'}) # Correct way to update the value of an existing key
# del dict1['city'] # Correct way to delete a key-value pair
# # dict1['degree'] = 'Computer Science' # Correct way to add a new key-value pair
# print(dict1) # Manik
# # print(dict1.get('agae','not found')) # 20
# for key, value in dict1.items():
#     print( value)
# # print(dict1.keys()) # dict_keys(['name', 'age', 'course'])
# # print(dict1.values()) # dict_values(['Manik', 26, 'cse'])   
# # print(dict1.items()) # dict_items([('name', 'Manik'), ('age', 26), ('course', 'cse')])

# name = 'zoro'
# profession = 'swordsman'
# name1 ='luffy' 
# profession1 = 'pirate'

# if name == 'zoros':
#     print(f"{name} is a swordsman.")
# elif name1 == 'luffys':
#     print(f"{name1} is a pirate.")

# else:
#     print(f"{name} is not a man.")

# from re import match
# from unittest import case


# name = "luffy"


# match   name :
#     case "zoro":
#         print("Zoro is a swordsman.")
#     case "luffy":
#         print("Luffy is a pirate.") 
#     case _:
#         print("Zoro is not ateam member.")

# loops 
# for 
set_numbers = {1, 2, 3}
for i in 'acd':
    
    for num in set_numbers:
      print(i, end="")
    print()




x=10  

while x<10:
    print(x)
    x+=1

for i in range(5):
    while True:
        print(i)
        
        break
      