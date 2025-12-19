# Define the Game class which handles interactions between two agents
class Game:
    def __init__(self, agent1, agent2):
        """
        Initialize a new game with two agents.
        :param agent1: Agent object
        :param agent2: Agent object
        """
        self.agent1 = agent1          # Store the first agent
        self.agent2 = agent2          # Store the second agent

        # Payoff matrix: maps each pair of moves to points for each agent
        # Format: (agent1_move, agent2_move) : (agent1_points, agent2_points)
        self.payoffs = {
            ("cooperate", "cooperate"): (3, 3),
            ("cooperate", "defect"):    (0, 5),
            ("defect", "cooperate"):    (5, 0),
            ("defect", "defect"):       (1, 1)
        }

    def play_round(self):
        """
        Play a single round of the game.
        1. Ask each agent for their move.
        2. Look up the points in the payoff matrix.
        3. Update each agent's score and history.
        4. Return the moves and scores for reporting.
        """
        # Get moves from agents
        move1 = self.agent1.choose_move()
        move2 = self.agent2.choose_move()

        # Lookup the resulting scores in the payoff matrix
        score1, score2 = self.payoffs[(move1, move2)]

        # Update agent scores
        self.agent1.score += score1
        self.agent2.score += score2

        # Record moves in each agent's history
        self.agent1.history.append(move1)
        self.agent2.history.append(move2)

        # Return results so main.py can display them
        return move1, move2, score1, score2
