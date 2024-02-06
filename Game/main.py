# MIT License
#
# Copyright (c) 2024 ThatOneGuy2664
# Copyright (c) 2024 Twaddler01
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# END LICENSE DESCRIPTION
# Python will have less updates but more eventual functionality. 

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

PlayerClass = None 
PlayerRace = None 
PlayerLevel = 1 
SneakAttack = False
CunningAction = False
Races = [ "Human", "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfing", "Half-Orc", "Tiefling" ] 
Classes = [ "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer", "Bloodhunter" ]
Spells = {
    "Cantrips": [
       "Acid Splash", "Blade Ward", "Booming Blade",
       "Chill Touch", "Control Flames", "Create Bonfire",
       "Dancing Lights", "Decompose", "Druidcraft", "Eldritch Blast",
       "Encode Thoughts", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade",
       "Guidance", "Gust", "Hand Of Radiance", "Infestation", "Light", "Lightning Lure",
       "Mage Hand", "Magic Stone", "Mending", "Message", "Mind Sliver", "Minor Illusion",
       "Mold Earth", "Poision Spray", "Prestidigitation", "Primal Savagery", "Produce Flame",
       "Ray Of Frost", "Resistance", "Sacred Flame", "Sapping Sting", "Shape Water", "Shillelagh",
       "Spare The Dying", "Shocking Grasp", "Sword Burst", "Thaumaturgy", "Thorn Whip", "Thunderclap",
       "Toll Of The Dead", "True Strike", "Vicious Mockery", "Virtue", "Word Of Radiance"
    ],
    "LevelOne": [
        "Absorb Elements", "Acid Stream", "Alarm", "Animal Friendship",
        "Arcane Weapon", "Armor of Agathys", "Arms of Hadar"
    ],
    "LevelTwo": [
        "Aid", "Alter Self", "Animal Messenger", "Arcane Lock", "Augury",
        "Barkskin", "Beast Sense", "Blindness/Deafness", "Blur", "Branding Smite",
        "Borrowed Knowledge", "Calm Emotions", "Cloud of Daggers", "Continual Flame", "Cordon of Arrows", "Crown of Madness",
        "Darkness", "Darkvision", "Detect Thoughts", "Enhance Ability", "Enlarge/Reduce", "Enthrall", "Find Traps", "Find Steed", "Flame Blade", 
        "Flaming Sphere", "Flock Of Familiars", "Fortune's Favor", "Gentle Repose", "Gust of Wind", "Heat Metal", "Hold Person", "Gift Of Gab",
        "Healing Spirit", "Icingdeath's Frost"
    ],
    "LevelThree": [],
    "LevelFour": [],
    "LevelFive": [],
    "LevelSix": [],
    "LevelSeven": [],
    "LevelEight": [],
    "LevelNine": []
}

if PlayerClass == "Rogue": 
    SneakAttack = True
