chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    new_list = []

    for item in chunk_one:
        new_list.append(item)

    for item in chunk_two:
        new_list.append(item)  

    return new_list    

    
    
print(merge_list(chunk_one, chunk_two))
