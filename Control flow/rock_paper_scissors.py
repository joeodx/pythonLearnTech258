import getpass

print("Welcome to Joe's version of Rock-Paper-Scissors!")

player1 = input("Player 1, enter your choice (rock, paper, or scissors): ")
player2 = input("Player 2, enter your choice (rock, paper, or scissors): ")

if player1 == player2:
    print("It's a tie!")
elif (player1 == 'rock' and player2 == 'scissors') or \
     (player1 == 'scissors' and player2 == 'paper') or \
     (player1 == 'paper' and player2 == 'rock'):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")



