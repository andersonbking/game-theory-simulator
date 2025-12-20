# Define the Game class which handles interactions between two agents
class Game:
    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2

    def play_round(self):
        move1 = self.agent1.choose_move(self.agent2)
        move2 = self.agent2.choose_move(self.agent1)

        # Payoff matrix (example: Prisoner's Dilemma)
        if move1 == "cooperate" and move2 == "cooperate":
            self.agent1.score += 3
            self.agent2.score += 3
        elif move1 == "cooperate" and move2 == "defect":
            self.agent1.score += 0
            self.agent2.score += 5
        elif move1 == "defect" and move2 == "cooperate":
            self.agent1.score += 5
            self.agent2.score += 0
        else:
            self.agent1.score += 1
            self.agent2.score += 1

        # Record history AFTER the round
        self.agent1.history.append(move1)
        self.agent2.history.append(move2)

        return move1, move2, self.agent1.score, self.agent2.score
