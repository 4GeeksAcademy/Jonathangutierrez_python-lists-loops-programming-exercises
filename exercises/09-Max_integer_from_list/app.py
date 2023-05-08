my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:

def max_integer (list):
    
    aux = 0

    for item in list:
        if item > aux:
            aux = item
    
    return aux
print(max_integer(my_list))




