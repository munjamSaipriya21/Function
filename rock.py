def rock_paper_scissor(player1_choice,player2_choice):
    if player1_choice == player2_choice:
        print("tie the game")
    elif player1_choice =="rock" or player2_choice=="scissor":
        print("winner the rock")
        print("lose the scissor")
    elif player1_choice=="scissor" or  player2_choice=="paper":
        print("winner the scissor")
        print("lose the paper")
    elif  player1_choice=="paper" or  player2_choice=="rock":
        print("winner the paper")
        print("lose the rock")
print("rock","paper","scissor")
print("welcome play the game")
player1=input("enter the player:")
player2=input("enter the player:")
rock_paper_scissor(player1,player2)
