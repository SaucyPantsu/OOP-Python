from abc import ABC, abstractmethod


class MathsGame(ABC):   # Maths game abstract class

    @abstractmethod
    def __init__(self): # init
        pass

    def play_game(self):    # where the game goes
        pass

    def game_logic(self):   # where game math goes
        pass

    def score(self):    # score tracking per game
        pass


class Fibonacci(MathsGame, ABC):    # fibonacci game

    def __init__(self):     # game variables
        self.fibonacci_amount = 0   # number of fib iterations
        self.loop = 0   # loop tracking
        self.temp = 0   # fib number tracking
        self.userscore = 0  # score tracking

    def play_game(self):
        userguess = 0   # user guess for next number
        userplay = 1    # is the user going to retry?
        while userplay != 2:    # while user play != 2, play game
            self.fibonacci_amount = int(input("How many Fibonacci numbers would you like?"))
            while self.fibonacci_amount < 3:    # ensures there are atleast 3 numbers in the sequesnce to guess from
                print("Number is too small, please choose a number larger than 3")
                self.fibonacci_amount = int(input("How many Fibonacci numbers would you like?"))    # input checking
            self.game_logic()   # run the game math
            while userguess != self.temp:   # checking guesses
                userguess = int(input("Please guess a number:"))
                if userguess == self.temp:
                    print("congratulations, you are right!")
                    self.userscore = self.userscore+1   # iterating score
                else:
                    pass
            userplay = int(input("Press 1 to play again, 2 to quit"))   # checking is user still wants to play

    def game_logic(self):   # game math
        n1 = 0
        n2 = 1
        temp = 0
        self.loop = 0
        print("The first ", self.fibonacci_amount, "numbers are:")
        print("0")
        while self.loop < self.fibonacci_amount-1:  # fibonacci sequence
            temp = n1 + n2
            n1 = n2
            n2 = temp
            self.loop = self.loop + 1
            print(temp)
        self.temp = n1 + n2
        print("What is the next number in the sequence?")

    def score(self):    # score tracking
        print("Your score in the Fibonacci game is:")
        print(self.userscore)

test = Fibonacci()
useroption = 1000

while useroption != 3:  # while user option is not 3, stay in program
    print("What Game would you like to play?")
    print("Available games : 1) Fibonacci, 2) See Scores, 3) Exit Program")
    while useroption != 1 | useroption != 3 | useroption != 2:  # stay in while while user input is invalid
        useroption = int(input("Which option do you choose? "))

    if useroption == 1: # play game
        test.play_game()
        useroption = 1000

    elif useroption == 2:   # see score
        test.score()
        useroption = 1000




