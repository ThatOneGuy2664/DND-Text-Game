import random

def roll_ability_score():
    # Roll 4d6 and drop the lowest value
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def generate_ability_scores():
    # Generate ability scores for all stats
    ability_scores = {}
    stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    for stat in stats:
        ability_scores[stat] = roll_ability_score()
    return ability_scores

# Example usage:
player_ability_scores = generate_ability_scores()
print("Player Ability Scores:")
for stat, score in player_ability_scores.items():
    print(f"{stat}: {score}")
