import sys

def CompareChoices(p1, p2):
    if p1==p2:
        return("Game ends in a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif p1 == "scissors":
        if p2 == "paper":
            return("Player 1 win!")
        else:
            return("Player 2 wins!")
    elif p1 == "paper":
        if p2 == "rock":
            return("Player 1 wins!")
        else:
            return("Player 2 win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again...")


player1 = input("Player #1.What's your name? :")
player2 = input("Player #2.And your name? :")
while True:
    player1Choice = str(input("%s, choose from rock, paper or scissors? :" %player1))
    if player1Choice == "rock" or "scissors" or "paper":
        player2Choice = str(input("%s, choose from rock, paper or scissors? :" %player2))
        if player2Choice == "rock" or "scissors" or "paper":
            print(CompareChoices(player1Choice, player2Choice))
            if str(input("Do you want to play another game, yes or no? :")) == "yes":
                continue
            else:
                print("game is over!!!!")
                break
        else:
            print("invalid input! Please try again...")
            continue
    else:
        print("invalid input! Please try again...")
        continue
        
