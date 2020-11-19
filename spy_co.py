import random
game_dictionary = {}
def game_finder(game_id):
  print(game_id)
  try:
    game_data=game_dictionary[game_id]
  except:
    game_data = None
  return game_data

def generator():
  number_generator=random.randint(0,999999999999999)
  speacil_id = (f"spy_co_{number_generator}")
  return speacil_id

def game_add(new_game):
  while True:
    game_id=generator()
    if game_id in game_dictionary:
      pass
    if not game_id in game_dictionary:
      break
  return game_id
