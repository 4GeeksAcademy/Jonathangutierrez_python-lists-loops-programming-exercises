
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def names_with_r (item):
    if item[0] == "R":
        return item

resulting_names = list(filter(names_with_r, all_names))
print(resulting_names)




