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

        # Defects twice after being defected against, otherwise cooperates.
        elif self.strategy.lower() == "2tft":
            if len(opponent.history) < 2:
                return "cooperate"
            # defect only if opponent defected in the last 2 rounds
            if opponent.history[-1] == "defect" and opponent.history[-2] == "defect":
                return "defect"
            else:
                return "cooperate"

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
        elif self.strategy.lower() == "suspicious tit for tat":
            if not opponent.history:
                return "defect"
            return opponent.history[-1]
        
        # Random moves
        elif self.strategy.lower() == "random":
            # Randomly pick "cooperate" or "defect"
            return random.choice(["cooperate", "defect"])
            
        elif self.strategy.lower() == "gradual":
            # Count how many defections opponent has made
            opponent_defections = opponent.history.count("defect")

            # If opponent never defected, cooperate
            if opponent_defections == 0:
                return "cooperate"
    
            # Retaliate: defect once for each new defection
            # We can keep track using self.retaliation_counter
            if not hasattr(self, "retaliation_counter"):
                self.retaliation_counter = 0

            # If retaliation counter is active, keep defecting
            if self.retaliation_counter > 0:
                self.retaliation_counter -= 1
                return "defect"

            # Check if opponent defected this round
            if opponent.history and opponent.history[-1] == "defect":
                # Start retaliation: defect once + gradually return to cooperate
                self.retaliation_counter = 1  # you can increase this if you want more gradualness
                return "defect"

            # Otherwise, cooperate
            return "cooperate"

        else:
            # Safety net
            print("ERROR")
            raise ValueError(f"Unknown strategy: {self.strategy}")

        return self.strategy
