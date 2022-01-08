import random

MAX_PLAYERS = 3
ROCK = "\U0000270A"
PAPER = "\U0000270B"
SCISSORS = "\U0000270C"

N_GAMES = 3


def main():

    print_welcome()

    players = []
    players.append(Player("human"))

    ai_opponents = input("How many AI opponents do you want to play against? ")
    for i in range(int(ai_opponents)):
        players.append(Player("ai"))

    print()
    print("Let's begin! Our players are: ")
    for p in players:
        print(f" > \33[1m{p.name}\33[0m")
    print()


    for round in range(N_GAMES):   
        hround = round + 1
        print(f"\33[1mRound {hround}!\33[0m")
        print()
        pmoves = []

        # check for player moves
        for p in players:
            print(f"{p.name}'s turn!")
            move = p.rps()
            print(f"{p.name} plays {move}!")
            pmoves.append([p, move])
            print()

        print()

        ties = []
        for cp in pmoves:
            current_player = cp[0]
            current_move = cp[1]
            for op in pmoves:
                opponent_player = op[0]
                opponent_move = op[1]
                if current_player != opponent_player:
                    if current_player.beats(current_move, opponent_move):
                        print(f"{current_player.name} beats {opponent_player.name}! One point to {current_player.name}!")
                        current_player.award(1)
                    elif current_move == opponent_move:
                        ties.append(set([current_player, opponent_player]))
        while ties:
            t = ties.pop()
            tied_string = ", ".join([x.name for x in t])
            for t2 in ties:
                if t == t2:
                    ties.remove(t2)
            print(f"We had a tie between {tied_string}!")
        print()


    # we'll need to sort the list by high score to low score    
    players.sort(key=lambda x: x.score, reverse=True)

    #add rankings based on scores
    prev = None
    for i, p in enumerate(players):
        if p.score!=prev:
            place,prev = i+1,p.score
        p.rank = place
    

    # resort by rank numbers
    players.sort(key=lambda x: x.rank)

    print()
    print("\33[1mGame over!\33[0m")
    print()

    for p in players:
        print(f"Rank #{p.rank}: {p.name} (score: {p.score})")

    
class Player:
    def __init__(self, ai_or_human):
        self._name = ""
        self._score = 0
        self._rank = 0

        if ai_or_human == "human":
            self._classification = "human"
        elif ai_or_human == "ai":
            self._classification = "ai"
        else:
            # assume human with no params
            self._classification = "human"

        self.prompt_name()

    def __str__(self):
        return f"{self._name} (score: {self._score})"
    
    def __repr__(self):
        return f"{self._name} (score: {self._score})"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def classification(self):
        return self._classification
    
    @classification.setter
    def classification(self, classification):
        self._classification = classification
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score + score

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, rank):
        self._rank = rank

    def award(self, points):
        self._score = self._score + points
        return self._score
    
    def beats(self, m1, m2):
        if m1 == ROCK and m2 == SCISSORS:
            return True
        elif m1 == PAPER and m2 == ROCK:
            return True
        elif m1 == SCISSORS and m2 == PAPER:
            return True
        elif m1 == m2:
            return False
        else:
            return False

    def prompt_name(self):
        ai_names = ["T1000", "T800", "HAL9000", "Colossus", "R2D2", "Skynet", 
        "C-3PO", "Mother", "Cyberman", "Dalek", "Chappie", "MCP", "VIKI", 
        "Ava", "Ultron", "Gunslinger"]

        if self.classification == "ai":
            self.name = random.choice(ai_names)
        else:
            self.name = input("Please enter your name: ")
    
    def rps(self):
        rps_string = {
            "r": ROCK,
            "p": PAPER,
            "s": SCISSORS
        }

        if self.classification == "ai":
            rand = random.random()
            if rand >= 0 and rand <= 0.333:
                return ROCK
            elif rand > 0.333 and rand <= 0.666:
                return PAPER
            elif rand > 0.666 and rand <= 1:
                return SCISSORS
        elif self.classification == "human":

            rps_input = input("Enter your choice - [p]aper, [r]ock, [s]cissors: ")
            while rps_input != "r" and rps_input != "p" and rps_input != "s":
                print("Invalid choice, enter r, p, or s!")
                rps_input = input("Enter your choice - [p]aper, [r]ock, [s]cissors: ")

            return rps_string[rps_input]

            


def print_welcome():
    """
    prints a welcome message
    """
    print('\33[1mWelcome to Rock Paper Scissors!\33[0m')
    print(f"You will play {N_GAMES} games against the AI.")
    print(f"{ROCK} beats {SCISSORS}, {SCISSORS} beats {PAPER}, {PAPER} beats {ROCK}")

    print('')
    print('')

if __name__ == '__main__':
    main()