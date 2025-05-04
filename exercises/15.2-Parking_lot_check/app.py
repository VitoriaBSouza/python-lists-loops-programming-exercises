parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here

def get_parking_lot(dct):
  state = {
    "total_slots": 0,
    "available_slots": 0,
    "occupied_slots": 0
  }

  for i in range(len(dct)):
    for x in range(len(dct[i])):
      if dct[i][x] == 1:
        state["total_slots"] += 1
        state["occupied_slots"] += 1
      elif dct[i][x] == 2:
        state["total_slots"] += 1
        state["available_slots"] += 1

  return state

print(get_parking_lot(parking_state))