import random
import time

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

def wait(seconds):
    # Wait for (seconds) and resume
    time.sleep(seconds)

# Generate ability scores
player_ability_scores = generate_ability_scores()

# Print each ability score with its corresponding label
for stat, score in player_ability_scores.items():
    print(f"{stat}: {score}")
print(f"{stat}: {score}")

PlayerClass = None 
PlayerRace = None 
PlayerLevel = 1 
Races = [ "Human", "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfing", "Half-Orc", "Tiefling" ] 
Classes = [ "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer", "Bloodhunter" ]
