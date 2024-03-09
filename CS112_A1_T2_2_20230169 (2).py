# File: CS112_A1_T2_2_20230169.py.
# Purpose: Number scrabble is played with the list of numbers between 1 and 9. Each player takes
# turns picking a number from the list. Once a number has been picked, it cannot be picked
# again. If a player has picked three numbers that add up to 15, that player wins the game.
# However, if all the numbers are used and no player gets exactly 15, the game is a draw.
# Author: Samya Mostafa
# ID: 20230169

# set the array of numbers and the players arrayrr
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
score1 = []
score2 = []

#this function checks the first 3 indexies if they are equal 15 or not for both players 
def determine():
    if sum(score1[:3]) == 15 and sum(score2[:3]) != 15:
        print("Player 1 wins")
    elif sum(score2[:3]) == 15 and sum(score1[:3]) != 15:
        print("Player 2 wins")
    elif sum(score2[:3]) == 15 and sum(score1[:3]) == 15:
        print("*****Draw!!!*****")
    elif sum(score2[:3]) != 15 and sum(score1[:3]) != 15:
        print("No player has reached a sum equal to 15 continue to choose one more number")
        game(3)

#this function checks the remaining indexies after a forth iteration if they are equal 15 or not for both players 
def determine2():
    if (sum(score1[1:4]) == 15 or sum(score1[:2]) + score1[3] == 15 or sum(score1[2:4]) + score1[0] == 15) and (sum(score2[1:4]) != 15 or sum(score2[:2]) + score2[3] != 15 and sum(score2[2:4]) + score2[0] == 15):
        print("*****Player 1 wins*****")
    elif (sum(score2[1:4]) == 15 or sum(score2[:2]) + score2[3] == 15 or sum(score2[2:4]) + score2[0] == 15) and (sum(score1[1:4]) != 15 or sum(score1[:2]) + score1[3] != 15 or sum(score1[2:4]) + score1[0] == 15):
        print("*****Player 2 wins*****")
    else:
        print("*****Draw!!!*****")

#this function operates the game
def game(counter):
    while counter < 4:
        print("player 1, your number is " + str(score1))
        choice = int(input("Player 1, enter your choice from " + str(numbers)+":"))
        while choice not in numbers:
            choice = int(input("invalid. please enter a valid choice, player 1:"))
        #remove the selected number by user from the set of the numbers and add it to the desierd player array 
        numbers.remove(choice)
        score1.append(choice)
        print("player 1, your number is " + str(score1))
        print("player 2, your number is " + str(score2))
        choice = int(input("Player 2, enter your choice from " + str(numbers)+":"))
        while choice not in numbers:
            choice = int(input("invalid. please enter a valid choice, player 2:"))
        numbers.remove(choice)
        score2.append(choice)
        print("player 2, your number is " + str(score2))
        counter += 1
        if counter == 3:
            determine()
            break
        if counter == 4:
            determine2()
            break


def main_menu():
    main_menu = """
                |**Main Menu**|
        WELCOME TO NUMBER SCRABBLE GAME
    ---------------------------------------
    A) Start
    B) End
    """
    while True:
        print(main_menu)
        choice_menu = input("Enter your choice: ").upper()
        if choice_menu == "A":
            print("\nGame started\n")
            game(0)
            break
        elif choice_menu == "B":
            print("\nGood Bye\n")
            break
        else:
            print("Please enter a valid choice")


main_menu()


