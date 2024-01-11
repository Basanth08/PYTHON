import random
import candy_land_card
from candy_land_card import make_deck
BOARD_SPOTS = 134
def create_board():
  board =["Start"]
  pattern = ['R','P','Y','B','O','G']
  for i in range(BOARD_SPOTS-1):
    board = [pattern[i%len(pattern)] for i in range(BOARD_SPOTS-1)]
  
  # Adding special spots
  board[9] = 'CC'
  board[20] = 'IC'
  board[42] = 'JJ'
  board[69] = 'GP'
  board[92] = 'LP'
  board[102] = 'PS'
  board[117] = 'BB'

  # Adding shortcuts
  board[4] = 'BS60'
  board[29] = 'BS41'
  
  # Adding licorice
  board[45] = 'GL'
  board[76] = 'GL'
  
  # Remaining special spots
  board[92] = 'LP'
  board[102] = 'PS'
  board[117] = 'BB'
  
  # Final spot
  board[133] = 'MC'
  
  return board

# Take player's turn
def take_turn(player, board, deck):
  
  # Draw card
  card = deck.pop()
  print("Player " + player[0] + " drew a " + card[2] + ".")
  
  # Move player
  if card[0] == 1: 
    # Single move
    idx = None
    for i in range(player[1], len(board)):
      if board[i] == card[1]:
        idx = i
      break
  elif card[0] == 2:
    # Double move
    idx = None 
    for i in range(player[1] + 1, len(board)):
      if board[i] == card[1]:
        idx = i 
      break
  else:
    # Special card
    for i in range(len(board)):
      if board[i] == card[2]:
        idx = i
      break
  
  player = (player[0], idx)
  print("Player " + player[0] + " landed on " + board[idx] + ".")
  
  # Check for shortcuts
  if board[idx] == 'BS60':
    print("Player" +  player[0] +  "took a shortcut!")
    idx = 60
    player = (player[0], idx)
  
  # Check for licorice  
  if board[idx] == 'GL':
    print("Player" + player[0] + "lost a turn!")

  return player  

# Play full game
def play_game(num_players):
  # Create players
  deck = make_deck()
  players = []
  colors = ['R','Y','B','G']
  for i in range(num_players):
    players.append((colors[i], 0))
  # Create deck and board
  candy_land_card.shuffle(deck)
  board = create_board()
  
  # Play until someone wins
  winner = False
  while not winner:
    for player in players:
      player = take_turn(player, board, deck)
      if player[1] >= len(board)-1:
        winner = True
        break
    # Reshuffle deck if needed
    if len(deck) == 0:
      candy_land_card.shuffle(deck)
  print("Player" + player[0] + "wins!")

def main(): 
    num_players = int(input("How many players? "))
    play_game(num_players) 

if __name__ == "__main__":
    main()