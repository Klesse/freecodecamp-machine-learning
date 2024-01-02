# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_opponent_play, opponent_history=[]):
  opponent_history.append(prev_opponent_play)
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  if prev_opponent_play == "":
    prev_opponent_play = 'R'
  if len(opponent_history) > 5 and len(opponent_history) % 7 == 1:
    last_five = opponent_history[-5:]
    most_frequent = max(set(last_five), key=last_five.count)
    return ideal_response[most_frequent]
  if len(opponent_history) > 6 and len(
      opponent_history) % 6 == 1 and opponent_history[-2] != "":
    return opponent_history[-2]
  return ideal_response[prev_opponent_play]

  