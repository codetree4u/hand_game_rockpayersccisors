import random

# Step 1: Creating a Class
class Game:
    def __init__(self):
        # get the computer's pick 
        self.computer_pick = self.get_computer_pick()
        
        # get the user's pick
        self.user_pick = self.get_user_pick()

        # get the result of the game
        self.result = self.get_result()     
# Step 2: Get Computer's Pick 
    def get_computer_pick(self):
        # get random number among 1, 2 and 3
        random_number = random.randint(1, 3)
        
        # possible options 
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        
        # return the value present at random_number
        return options[random_number]
# Step 3: Get user's Pick		
# -- If the user enters any other strings other than 'rock', 'paper' or 'scissors', we cannot compare it properly with the computer's pick.
    def get_user_pick(self):
        #user_pick = input('Enter rock/paper/scissors: ')
		#return user_pick.lower()
# Step 4: Make User Input a Valid String
# -- To solve the prior issue, let's modify the get_user_pick()	
        # infinite while loop 
        while True:
            user_pick = input('Enter rock/paper/scissors: ')

            # convert to lowercase
            user_pick = user_pick.lower()

            # if user_pick is either rock or paper or scissors,
            # terminate the loop
            if user_pick in ('rock', 'paper', 'scissors'):
                  break
            else:
                print('Wrong input!')

        return user_pick
# Step 5: Decide win, lose and draw
    def get_result(self):
        # condition for draw
        if self.computer_pick == self.user_pick:
            return 'draw'
        
        # condition for the user to win
        elif self.user_pick == 'paper' and self.computer_pick == 'rock':
            return 'win'
        elif self.user_pick == 'rock' and self.computer_pick == 'scissors':
            return 'win'
        elif self.user_pick == 'scissors' and self.computer_pick == 'paper':
            return 'win'
        
        # in all other conditions, users lose    
        else:
            return 'lose'
# Step 6: Add a Method to Print the result
    def print_result(self):
        print(f"Computer's pick: {self.computer_pick}")
        print(f'Your pick: {self.user_pick}')
        print(f'You {self.result}')


# create an object of the Game class inside a while loop.
while True:
    game = Game()
    game.print_result()
    
    play_again = input('Do you want to play again? (y/n)')
    
    if play_again != 'y':
        break
