# Define the Agent class which represents a player in the simulation
import random 

class Agent:
    def __init__(self, name, strategy="cooperate"):
        # Initialize a new agent
        self.name = name              # Save the agent's name
        self.strategy = strategy      # Save the agent's chosen strategy
        self.score = 0                # Initialize the agent's score to 0
        self.history = []             # Keep track of the agent's moves over rounds
        
    def choose_move(self, opponent):
    
        # Always cooperate
        if self.strategy.lower() == "always cooperate":
            return "cooperate"

        # Always defect
        elif self.strategy.lower() == "always defect":
            return "defect"
        
        # Defect unless both agents defect
        elif self.strategy.lower() == "cooperate for defect":
            if "defect" in opponent.history:
                return "cooperate"
            else:
                return "defect"
            
        # Cooperates first, then permanently defects if opponent defects
        elif self.strategy.lower() == "grim":
            if "defect" in opponent.history:
                return "defect"
            else:
                return "cooperate"

        # Tit-for-Tat strategy
        elif self.strategy.lower() == "tit for tat":
            # First move: cooperate
            if not opponent.history:
                return "cooperate"
            # Copy opponent's last move
            return opponent.history[-1]
            
        # Suspicious Tit-for-Tat strategy
        elif self.strategy.lower() == "stft":
            if not opponent.history:
                return "defect"
            return opponent.history[-1]
        
        # Random moves
        elif self.strategy.lower() == "random":
            # Randomly pick "cooperate" or "defect"
            return random.choice(["cooperate", "defect"])
            
        else:
            # Safety net
            print("ERROR")
            raise ValueError(f"Unknown strategy: {self.strategy}")

        return self.strategy

