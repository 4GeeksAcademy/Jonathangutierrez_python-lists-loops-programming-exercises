my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
new_list = []
for item in my_list :
    if type(item) == dict or type(item) == list:
        new_list.append(item)

 
print(new_list)       
