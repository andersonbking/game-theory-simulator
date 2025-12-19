# Agent class with properties like strategy, score, and history

# Methods for choosing moves based on strategy

# Define the Agent class which represents a player in the simulation
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

    def choose_move(self):
        """
        Determine the agent's move for the round.
        Currently returns the fixed strategy.
        Later, can implement adaptive or AI strategies here.
        """
        return self.strategy
