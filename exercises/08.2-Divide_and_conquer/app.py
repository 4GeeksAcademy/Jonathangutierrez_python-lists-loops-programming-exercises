list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list (list):

    even_numbers = [] 
    odd_numbers = [] 
    all_numbers = [odd_numbers, even_numbers]
    
    for item in list_of_numbers:
        if item % 2 == 0:
            even_numbers.append(item)
        else:
            odd_numbers.append(item)
       
    return all_numbers

print(merge_two_list(list_of_numbers))

