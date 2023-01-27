

super_heros = ["batman", "spiderman", "thor", "wonder woman", "jedi"]

len_list = []
for hero in super_heros:
    len_list.append(len(hero))

# print(len_list)

len_list_2 = [len(hero) for hero in super_heros]
# print(len_list_2)

double_len_list = [len(hero)*2 for hero in super_heros]

# print(double_len_list)

len_and_name = [(hero,len(hero)) for hero in super_heros]
# print(len_and_name)

# print(type(len_and_name[0]))
names = [1,2,3, 4, 5]
emoijis = ["🦓", "🦁", "🐘", "🐆","🦝", "😀"]
#
# animals = {}
# for i in range(0,len(names)):
#     # print(f"{names[i]} = {emoijis[i]}")
#     animals[names[i]] = emoijis[i]

animals = dict(zip(names,emoijis))
print(animals)



