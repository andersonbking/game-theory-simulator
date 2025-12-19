from agent import Agent
from game import Game     

def main():
    """
    Main function to run a simple simulation.
    """
    # Create two agents with fixed strategies
    agent_a = Agent("Alice", strategy="cooperate")
    agent_b = Agent("Bob", strategy="defect")

    # Initialize the game with the two agents
    game = Game(agent_a, agent_b)

    # Play one round of the game
    move1, move2, score1, score2 = game.play_round()

    # Print the moves and updated scores
    print(f"{agent_a.name} chose {move1}, {agent_b.name} chose {move2}")
    print(f"Scores -> {agent_a.name}: {agent_a.score}, {agent_b.name}: {agent_b.score}")

# Standard Python boilerplate to ensure main() runs
if __name__ == "__main__":
    main()
