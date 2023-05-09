theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

def map_numbers (num):
    if num == 0:
        return 'woko'
    else:
        return 'wiki'
    
new_list = list(map(map_numbers, theBools))

print(new_list)




