def lyrics_generator(lst):
    res = ""
    count = 0
    for beat in lst:
        if beat == 0:
            res += "Boom "
            count = 0
        elif beat == 1:
            res += "Drop the base "
            count += 1
            if count == 3:
                res += "!!!Break the base!!! "
                count = 0
    return res.strip()


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))