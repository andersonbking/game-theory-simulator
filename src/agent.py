# Agent class with properties like strategy, score, and history

# Methods for choosing moves based on strategy

# Define the Agent class which represents a player in the simulation
# Define the Agent class which represents a player in the simulation
import random 

class Agent:
    def __init__(self, name, strategy="cooperate"):
        """
        Initialize a new agent.
        :param name: string, the name of the agent
        :param strategy: string, initial fixed strategy ("cooperate" or "defect")
        """
        self.name = name              # Save the agent's name
        self.strategy = strategy      # Save the agent's chosen strategy
        self.score = 0                # Initialize the agent's score to 0
        self.history = []             # Keep track of the agent's moves over rounds
        
    def choose_move(self, opponent):
    
        # Always cooperate
        if self.strategy == "always_cooperate":
            return "cooperate"

        # Always defect
        elif self.strategy == "always_defect":
            return "defect"
            
        # Cooperates first, then permanently defects if opponent defects
        elif self.strategy == "grim":
            if "defect" in opponent.history:
                return "defect"
            else:
                return "cooperate"

        # Tit-for-Tat strategy
        elif self.strategy == "tit_for_tat":
            # First move: cooperate
            if not opponent.history:
                return "cooperate"
            # Copy opponent's last move
            return opponent.history[-1]
            
        # Suspicious Tit-for-Tat strategy
        elif self.strategy == "stft":
            if not opponent.history:
                return "defect"
            return opponent.history[-1]
        
        # Random moves
        elif self.strategy == "random":
            # Randomly pick "cooperate" or "defect"
            return random.choice(["cooperate", "defect"])
            
        else:
            # Safety net
            print("ERROR")
            raise ValueError(f"Unknown strategy: {self.strategy}")

        return self.strategy
