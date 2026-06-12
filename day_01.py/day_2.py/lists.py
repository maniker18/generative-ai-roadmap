sports = ["cricket", "football", "basketball", "tennis"]
# s1=sorted(sports) # cricket
# print(s1)
# s1.remove("cricket") # 0
# print('tennis' in sports) # True

# for ind, sport in enumerate(sports,start=1):
#     print(f"{ind}: {sport}")


set1 = set(sports)
set2 = {'boxing', 'badminton', 'volleyball', 'cricket'}

print(set1.intersection(set2)) # {'cricket'}
print(set1.union(set2))
print(set1.difference(set2)) # {'cricket', 'football', 'tennis', 'basketball'}
print(set2.difference(set1)) # {'boxing', 'badminton', 'volleyball'}