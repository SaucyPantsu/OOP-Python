# Lab Test 1
# Ryan McLoughlin
# C21431604
# Number guessing game. User tries to guess the numbers in one of the four slots in the number list, and once done,
# the game completes.

# breaking a string into a list
def convert_to_list(string):
    list_split = []
    list_split[:0] = string
    return list_split


number_list = ["456", "987", "693", "275"]  # list of possible targets

# User target selection
user_selection = int(input("please choose a number between 0 and 3 to start the game"))
# ensuring selected target is valid
while user_selection < 0 or user_selection > 3:  # checking number chosen is in range
    print("Error, number outside of range, please try again")
    user_selection = int(input("please choose a number between 0 and 3 to start the game"))
# setting target number as the selected number
target_num = number_list[user_selection]
# variable list
target_list = convert_to_list(target_num)
guess_amount = 0
number_correct_guess = 0
previous_guess = []
state = False
while state is False:
    win = 0
    index = 0
    index_two = 0
    guess_test = 0
    # if user has won, end game
    if number_correct_guess == 3:
        state = True
    else:
        # if user has not won, run this else
        input_check = str(input("Please guess a number between 0 and 9"))
        user_guess_num = int(input_check)  # converting string to int for checking if number is in range
        while user_guess_num < 0 or user_guess_num > 9:  # checking number chosen is in range
            print("Error, number outside of range, please try again")
            input_check = str(input("Please guess a number between 0 and 9"))
        for user_guess in previous_guess:  # Checking if number has been previously guessed
            if input_check == previous_guess[index]:
                print("you have already guessed", user_guess, "please try again")
                input_check = str(input("Please guess a number between 0 and 9"))
                user_guess_num = int(input_check)
                while user_guess_num < 0 or user_guess_num > 9:  # checking number chosen is in range
                    print("Error, number outside of range, please try again")
                    input_check = str(input("Please guess a number between 0 and 9"))
                index = index+1
            else:
                index = index+1
        # adding the guessed number into the guessed number array
        previous_guess.append(input_check)
        # checking id the number is in the target array
        for user_guess in target_list:
            if input_check != target_list[index_two]:
                index_two = index_two+1
                guess_test = guess_test + 1
            # if number matches a number in the array
            else:
                number_correct_guess = number_correct_guess + 1
                print("you guessed the number at position ", index_two+1, " correctly!")
                index_two = index_two + 1
                guess_test = guess_test + 1
                win = 1
            # if the number you guessed isn't in the array
            if guess_test == 3 and number_correct_guess != 3 and win == 0:
                print("You didn't guess correct, please try again")
                break
print("congratulations, you have won!")  # ending line
