import random
from collections import defaultdict

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_history = []
        self.ai_history = []
        self.results = []
        self.score = {'player': 0, 'ai': 0, 'tie': 0}
        
    def determine_winner(self, player_choice, ai_choice):
        """Determine the winner of a round"""
        if player_choice == ai_choice:
            return 'tie'
        
        winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_combinations[player_choice] == ai_choice:
            return 'player'
        else:
            return 'ai'
    
    def get_ai_choice_basic(self):
        """Basic AI strategy - completely random"""
        return random.choice(self.choices)
    
    def get_ai_choice_intermediate(self):
        """Intermediate AI strategy - reacts to player patterns"""
        if not self.player_history:
            return random.choice(self.choices)
        
        # Count player's most frequent choice
        freq = defaultdict(int)
        for choice in self.player_history:
            freq[choice] += 1
        most_common = max(freq.items(), key=lambda x: x[1])[0]
        
        # Choose what beats the player's most common choice
        beating_choices = {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
        }
        return beating_choices[most_common]
    
    def get_ai_choice_advanced(self):
        """Advanced AI strategy - predicts based on last move"""
        if not self.player_history:
            return random.choice(self.choices)
        
        last_player_choice = self.player_history[-1]
        
        # Players often switch to what would have beaten their last choice
        likely_next = {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
        }
        predicted_player_choice = likely_next.get(last_player_choice, 'rock')
        
        # Choose what beats the predicted choice
        beating_choices = {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
        }
        return beating_choices[predicted_player_choice]
    
    def play_round(self, player_choice):
        """Play a single round of the game"""
        player_choice = player_choice.lower()
        if player_choice not in self.choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return None
        
        # AI selects strategy based on game progress
        if len(self.player_history) < 3:
            ai_choice = self.get_ai_choice_basic()
        elif len(self.player_history) < 10:
            ai_choice = self.get_ai_choice_intermediate()
        else:
            ai_choice = self.get_ai_choice_advanced()
        
        # Determine winner
        result = self.determine_winner(player_choice, ai_choice)
        
        # Update game state
        self.player_history.append(player_choice)
        self.ai_history.append(ai_choice)
        self.results.append(result)
        self.score[result] += 1
        
        return {
            'player_choice': player_choice,
            'ai_choice': ai_choice,
            'result': result
        }
    
    def display_result(self, round_result):
        """Display the result of a round"""
        print(f"\nYou chose: {round_result['player_choice']}")
        print(f"AI chose: {round_result['ai_choice']}")
        
        if round_result['result'] == 'tie':
            print("It's a tie!")
        elif round_result['result'] == 'player':
            print("You win this round!")
        else:
            print("AI wins this round!")
        
        print(f"\nCurrent score - You: {self.score['player']} | AI: {self.score['ai']} | Ties: {self.score['tie']}")
    
    def play_game(self):
        """Main game loop"""
        print("Welcome to Rock Paper Scissors!")
        print("Enter 'quit' to end the game at any time.")
        
        while True:
            print("\nChoose rock, paper, or scissors:")
            player_input = input().lower()
            
            if player_input == 'quit':
                print("\nFinal Score:")
                print(f"You: {self.score['player']} | AI: {self.score['ai']} | Ties: {self.score['tie']}")
                if self.score['player'] > self.score['ai']:
                    print("Congratulations! You won the game!")
                elif self.score['ai'] > self.score['player']:
                    print("The AI won this time. Better luck next time!")
                else:
                    print("The game ended in a tie!")
                break
            
            round_result = self.play_round(player_input)
            if round_result:
                self.display_result(round_result)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()