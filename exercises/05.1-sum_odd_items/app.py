arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

def sum_odds (items):

    total_odds = 0

    for i in items:
        if i % 2 != 0:
            total_odds += i
    return total_odds

print(sum_odds(arr))         
