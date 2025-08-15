import random
import time

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.symbols = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        self.rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        
        # Game state
        self.user_score = self.computer_score = self.rounds = 0
        self.user_name = ""
        self.bot_name = "Rocky"
        self.bot_streak = 0
        
        # Personality responses
        self.reactions = {
            'win': ["YES! I'm on fire! 🔥", "Boom! Got you! 😎", "That felt amazing! 🎉"],
            'lose': ["Nice one! You got me! 👏", "Ouch! Well played! 😅", "You're good at this! 🤔"],
            'tie': ["Great minds think alike! 🤝", "Jinx! We're in sync! ✨", "Spooky mind-reading! 👻"]
        }

    def print_slow(self, text, delay=0.02):
      
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def setup_game(self):
        
        print(f"🎮 Hey there! I'm {self.bot_name}, ready to play Rock-Paper-Scissors! 😊")
        self.user_name = input("What's your name, challenger? ").strip() or "Player"
        self.print_slow(f"\nNice to meet you, {self.user_name}! Let's see what you've got! 💪")

    def display_status(self):
        
        print(f"\n{'='*40}")
        print(f"🏆 {self.user_name}: {self.user_score} | {self.bot_name}: {self.computer_score} | Rounds: {self.rounds}")
        if self.bot_streak > 1:
            print(f"🔥 {self.bot_name} is on a {self.bot_streak} win streak!")
        print(f"{'='*40}")

    def get_user_choice(self):
        
        while True:
            print(f"\n{self.user_name}, choose your weapon:")
            print("1. Rock 🪨  2. Paper 📄  3. Scissors ✂️  4. Quit 👋")
            
            choice = input("Your choice (1-4): ").strip()
            choices_map = {'1': 'rock', '2': 'paper', '3': 'scissors', '4': 'quit'}
            
            if choice in choices_map:
                return choices_map[choice]
            print(f"{self.bot_name}: Pick 1, 2, 3, or 4! 😊")

    def bot_thinking(self):
        
        print(f"\n{self.bot_name}: ", end='')
        for _ in range(3):
            print(".", end='', flush=True)
            time.sleep(0.3)
        print(" 🤔 Choosing!")

    def get_computer_choice(self):
        
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        
        if user_choice == computer_choice:
            return 'tie', random.choice(self.reactions['tie'])
        elif self.rules[user_choice] == computer_choice:
            self.bot_streak = 0
            return 'user', random.choice(self.reactions['lose'])
        else:
            self.bot_streak += 1
            return 'computer', random.choice(self.reactions['win'])

    def show_result(self, user_choice, computer_choice, winner, bot_reaction):
        
        print(f"\n⚔️ BATTLE RESULTS ⚔️")
        print(f"{self.user_name}: {user_choice.upper()} {self.symbols[user_choice]}")
        print(f"{self.bot_name}: {computer_choice.upper()} {self.symbols[computer_choice]}")
        
        time.sleep(1)
        if winner == 'tie':
            print("🤝 IT'S A TIE!")
        elif winner == 'user':
            print(f"🎉 {self.user_name.upper()} WINS!")
        else:
            print(f"💻 {self.bot_name.upper()} WINS!")
        
        print(f"\n{self.bot_name}: {bot_reaction}")

    def update_score(self, winner):
        
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1
        self.rounds += 1

    def play_again(self):
       
        prompts = ["Another round? 😊", "Keep playing? 💪", "One more battle? ⚔️"]
        while True:
            choice = input(f"\n{self.bot_name}: {random.choice(prompts)} (y/n): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            print("Just y or n! 😄")

    def final_stats(self):
        
        print(f"\n{'='*50}")
        print("📊 FINAL RESULTS 📊")
        print(f"Battles: {self.rounds} | {self.user_name}: {self.user_score} | {self.bot_name}: {self.computer_score}")
        
        if self.user_score > self.computer_score:
            print(f"🏆 {self.user_name} WINS! You're amazing! 🎉")
        elif self.computer_score > self.user_score:
            print(f"🤖 I won, but you were awesome! Great game! 👏")
        else:
            print("🤝 Perfect tie! We're equally matched! ⚖️")
        
        if self.rounds > 0:
            win_rate = (self.user_score / self.rounds) * 100
            print(f"📈 {self.user_name}'s win rate: {win_rate:.1f}%")
        print(f"{'='*50}")

    def run_game(self):
        
        self.setup_game()
        input("\nPress Enter to start the battle...")
        
        while True:
            self.display_status()
            
            # Pre-game chatter
            chatter = ["Let's do this! 🚀", "Ready for battle! ⚔️", "Bring it on! 💪"]
            print(f"\n{self.bot_name}: {random.choice(chatter)}")
            
           
            user_choice = self.get_user_choice()
            if user_choice == 'quit':
                print(f"\n{self.bot_name}: Thanks for playing, {self.user_name}! 👋")
                break
            
            self.bot_thinking()
            computer_choice = self.get_computer_choice()
            
           
            winner, bot_reaction = self.determine_winner(user_choice, computer_choice)
            self.update_score(winner)
            self.show_result(user_choice, computer_choice, winner, bot_reaction)
            
           
            if not self.play_again():
                break
        
        # Final stats
        if self.rounds > 0:
            self.final_stats()
            print(f"\n{self.bot_name}: You're awesome, {self.user_name}! Come back anytime! ✨")

def main():
    """Start the game."""
    game = RockPaperScissorsGame()
    game.run_game()

if __name__ == "__main__":
    main()