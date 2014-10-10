__author__ = 'yiqiwang'
# This program simulate a classical game named "Rock,Paper,Scissors".
# The user and computer choose a weapon from "Rock,Paper,Scissors" and fight. And then output the result of "fight"
import random

def main():
    print "Let's play Rock, Paper, Scissors!"
    Tie_count = 0
    User_win_count = 0
    Computer_win_count = 0
    R_count = 0
    S_count = 0
    P_count = 0
    # Call get_user_input() function to get the user's weapon
    user_weapon = get_user_input()
    while user_weapon != 'Quit':
        # Call choose_weapon() function to get the computer's weapon
        computer_weapon = choose_weapon()
        # Call determine_winner() function to decide which side wins
        result = determine_winner(user_weapon,computer_weapon)
        print "You have chosen %s and the computer chose %s. %s" % (user_weapon,computer_weapon,result)
        # To record the user's choice
        if user_weapon == "Rock":
            R_count += 1
        elif user_weapon == "Paper":
            P_count += 1
        elif user_weapon == "Scissor":
            S_count += 1
        user_weapon = get_user_input()
        # To record the result of game
        if result == "It's a tie!":
            Tie_count += 1
        elif result == "The computer has won this round!":
            Computer_win_count += 1
        else:
            User_win_count += 1

    print "I'm sorry to see you go! You've proven to be a worthy adversary."

    # Print the result and the times user choose each weapon
    print "User Win: %d , Computer Win: %d , Ties: %d ." % (User_win_count,Computer_win_count,Tie_count)
    print "User has chosen Rock: %d;  Paper: %d;  Scissor: %d." % (R_count,P_count,S_count)

# To get the user's decision(weapon)
def get_user_input():
    user_input = raw_input("Please select your weapon: (R) for rock, (P) for paper, (S) for scissors, or (Q) to quit: ")
    if user_input == 'R' or user_input == 'r':
        user_weapon = "Rock"
    elif user_input == 'P' or user_input == 'p':
        user_weapon = "Paper"
    elif user_input == 'S' or user_input == 's':
        user_weapon = "Scissor"
    else:
        user_weapon = "Quit"
    return user_weapon

# To get the computer's decision(weapon)
def choose_weapon():
    computer_output = random.randint(1,3)
    if computer_output == 1:
        computer_weapon = "Rock"
    elif computer_output == 2:
        computer_weapon = "Paper"
    elif computer_output == 3:
        computer_weapon = "Scissor"
    return computer_weapon

# To get the game result
def determine_winner(user_weapon,computer_weapon):

    if computer_weapon == "Rock":
        if user_weapon == "Rock":
            result = "It's a tie!"
        elif user_weapon == "Scissor":
            result = "The computer has won this round!"
        else:
            result = "You win!"
    elif computer_weapon == "Scissor":
        if user_weapon == "Scissor":
            result = "It's a tie!"
        elif user_weapon == "Rock":
            result = "You win!"
        else:
            result = "The computer has won this round!"
    else:
        if user_weapon == "Scissor":
            result = "You win!"
        elif user_weapon == "Rock":
            result = "The computer has won this round!"
        else:
            result = "It's a tie!"

    return result

# To call main() function
main()
