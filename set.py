# name = { "Sis" , "Bro" , "man"}
# name2={"sis", "Bro", "woman"}
# print(name.update(name2))
# print(name)
# print(name2)
# print(name.union(name2))
# print()
# print(name.intersection(name2))
# print(name.intersection_update(name2))
# print(name2)

# name.add("man 1")
# name.remove("man 1")
# name.pop() #rndm popping of one element
# name.discard("fefesvs") # does not give error for deleting a nonexistent mem , REMOVE would have given
# name.clear() # same set of 0 elements
# del name
# print(name) # gives error cuz DELETED name set entirely 

players = {"alex" , "sam" , "riya", "john"}
new = {"riya", "mira", "zain"}
ban = {"john"}

players.add("kabir")
print(players)
players.remove("sam")
print(players)
players.update(new)
print(players)
players.difference_update(ban)
print(players)

print(players.intersection(new))

if "mira" in players:
    print("yes")

print(players.symmetric_difference(new)) # A U B - A intersection B 
print(players.issuperset(new))
print(new.issubset(players))

players_updated = players.copy 
