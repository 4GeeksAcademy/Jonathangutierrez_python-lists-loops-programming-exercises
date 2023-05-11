parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot():
    parking_state = [
      [1,1,1],
      [0,0,0],
      [1,1,2]
    ]
    
    total_slots = 0
    available_slots = 0
    occupied_slots = 0
    
    for row in parking_state:
        for space in row:
            total_slots += 1
            if space == 0:
                available_slots += 1
            elif space > 0:
                occupied_slots += 1
    
    return {
        "total_slots": total_slots,
        "available_slots": available_slots,
        "occupied_slots": occupied_slots
    }