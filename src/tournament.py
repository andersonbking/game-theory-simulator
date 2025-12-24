# tournament.py
from agent import Agent
from game import Game
import itertools

# List of strategies to include
strategies = [
    "always cooperate",
    "always defect",
    "cooperate for defect",
    "2tft",
    "grim",
    "tit for tat",
    "suspicious tit for tat",
    "gradual",
    "random"
]

# Initialize cumulative scores
scores = {strategy: 0 for strategy in strategies}

# Number of rounds per match
NUM_ROUNDS = int(input("Number of rounds: "))
print()

# Round-robin tournament (no self-play; change itertools.combinations to itertools.product for self-play)
for strat_a, strat_b in itertools.product(strategies, repeat=2):
    # Instantiate agents
    agent_a = Agent(name=strat_a, strategy=strat_a)
    agent_b = Agent(name=strat_b, strategy=strat_b)

    # Create a game instance
    game = Game(agent_a, agent_b)

    # Play NUM_ROUNDS rounds
    for _ in range(NUM_ROUNDS):
        game.play_round()

    # Update cumulative scores
    scores[strat_a] += agent_a.score
    scores[strat_b] += agent_b.score

# Sort and print tournament results
ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print("Tournament Results:")
for rank, (strategy, total_score) in enumerate(ranked, start=1):
    print(f"{rank}. {strategy}: {total_score}")
