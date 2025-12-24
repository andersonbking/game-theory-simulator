from agent import Agent
from game import Game     
import random

print("Game Theory Simulation Demo by Anderson")
print("Iterated Prisoner's Dilemma Edition")
print()

def main():
    """
    Main function to run a simple simulation.
    """
    choice1 = input("What strategy would you like John to perform? ")
    choice2 = input("What strategy would you like Bob to perform? ")
    choices = [choice1, choice2]

    
    # Create two agents with fixed strategies
    agent1 = Agent("John", strategy=choice1)
    agent2 = Agent("Bob", strategy=choice2)

    # Initialize the game with the two agents
    game = Game(agent1, agent2)

    print()
    times = int(input("How many rounds? "))
    print()
    
    count = 0
    
    while count < times:
        move1, move2, score1, score2 = game.play_round()

        print(f"{agent1.name} chose {move1}, {agent2.name} chose {move2}")
        print(f"Scores -> {agent1.name}: {agent1.score}, {agent2.name}: {agent2.score}")
        print()
        count += 1
      
    print()  
    print(f"Total Score: {agent1.name} has {agent1.score} and {agent2.name} has {agent2.score}.")

# Standard Python boilerplate to ensure main() runs
if __name__ == "__main__":
    main()
