people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    new_people = []    
    for item in people:
        if item != person_name:
            new_people.append(item)
    return new_people        

    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))