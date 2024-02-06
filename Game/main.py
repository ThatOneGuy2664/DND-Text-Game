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
       "Arcane Weapon", "Armor of Agathys", "Arms of Hadar", "Bane", "Beast Bond", "Bless", "Burning Hands",
       "Catapult", "Cause Fear", "Ceremony", "Chaos Bolt", "Charm Person", "Chromatic Orb", "Color Spray",
       "Command", "Compelled Duel", "Comprehend Languages", "Create Or Destroy Water", "Cure Wounds", "Detect Evil And Good",
       "Detect Magic", "Detect Poison And Disease", "Disguise Self", "Dissonant Whispers", "Distort Value", "Divine Favor",
       "Earth Tremor", "Ensnaring Strike", "Entangle", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall",
       "Find Familiar", "Fog Cloud", "Frost Fingers", "Gift Of Alacrity", "Goodberry", "Grease", "Guiding Bolt", "Guiding Hand",
       "Hail Of Thorns", "Healing Elixir", "Healing Word", "Hellish Rebuke", "Heroism", "Hex", "Hunter's Mark", "Ice Knife",
       "Id Insinuation", "Identify", "Illusory Script", "Infallible Relay", "Inflict Wounds", "Jim's Magic Missile", "Jump", "Longstrider",
       "Mage Armor", "Magic Missile", "Magnify Gravity", "Protection From Evil And Good", "Puppet", "Purify Food And Drink", "Ray Of Sickness",
       "Sanctuary", "Searing Smite", "Sense Emotion", "Shield", "Shield Of Faith", "Silent Image", "Silvery Barbs", "Sleep", "Snare", "Speak With Animals",
       "Sudden Awakening", "Tasha's Caustic Brew", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderous Smite", "Thunderwave", "Unearthly Chorus",
       "Unseen Servant", "Wild Cunning", "Witch Bolt", "Wrathful Smite", "Zephyr Strike"
    ],
    "LevelTwo": [
       "Aganazzar's Scorcher", "Aid", "Air Bubble", "Alter Self", "Animal Messenger", "Arcane Lock", "Augury",
       "Barkskin", "Beast Sense", "Blindness/Deafness", "Blur", "Branding Smite",
       "Borrowed Knowledge", "Calm Emotions", "Cloud of Daggers", "Continual Flame", "Cordon of Arrows", "Crown of Madness",
       "Darkness", "Darkvision", "Detect Thoughts", "Dragon's Breath", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Enthrall", 
       "Find Traps", "Find Steed", "Flame Blade", "Flaming Sphere", "Flock Of Familiars", "Fortune's Favor", "Gentle Repose", "Gust of Wind", "Heat Metal",
       "Hold Person", "Gift Of Gab", "Healing Spirit", "Icingdeath's Frost", "Immovable Object", "Invisibility", "Jim's Glowing Coin", "Kinetic Jaunt", "Knock",
       "Lesser Restoration", "Levitate", "Locate Animals Or Plants", "Locate Object", "Magic Mouth", "Magic Weapon", "Maximmillian's Earthen Grasp", "Melf's Acid Arrow",
       "Mental Barrier", "Mind Spike", "Mind Thrust", "Mirror Image", "Misty Step", "Moonbeam", "Nathair's Mischief", "Nystul's Magical Aura", "Pass Without Trace",
       "Phantasmal Force", "Prayer Of Healing", "Protection From Poison", "Pyrotechnics", "Ray Of Enfeeblement", "Rime's Binding Ice", "Rope Trick", "Scorching Ray",
       "See Invisibility", "Shadow Blade", "Shatter", "Silence", "Skywrite", "Snilloc's Snowball Storm", "Spider Climb", "Spike Growth", "Spiritual Weapon", "Spray Of Cards",
       "Suggestion", "Summon Beast", "Tasha's Mind Whip", "Thought Shield", "Vortex Warp", "Warding Bond", "Warding Wind", "Warp Sense", "Web", "Wither And Bloom", "Wristpocket",
       "Zone Of Truth"
    ],
    "LevelThree": [
       "Animate Dead", "Antagonize", "Ashardalon's Stride", "Aura Of Vitality", "Beacon Of Hope", "Bestow Curse", "Blinding Smite", "Blink", "Call Lightning", "Catnap", "Clairvoyance",
       "Conjure Animals", "Conjure Barrage", "Conjure Lesser Demon", "Counterspell", "Create Food And Water", "Crusader's Mantle", "Daylight", "Dispel Magic", "Elemental Weapon",
       "Enemies Abound", "Erupting Earth", "Fast Friends", "Fear", "Feign Death", "Fireball", "Flame Arrows", "Flame Stride", "Fly", "Freedom Of The Waves", "Galder's Tower", "Gaseous Form",
       "Glyph Of Warding", "Haste", "House Of Cards", "Hunger Of Hadar", "Hypnotic Pattern", "Incite Greed", "Intellect Fortress", "Leomund's Tiny Hut", "Life Transference", "Lightning Arrow",
       "Lightning Bolt", "Magic Circle", "Major Image", "Mass Healing Word", "Meld Into Stone", "Melf's Minute Meteors", "Motivational Speech", "Nondetection", "Phantom Seed", "Plant Growth",
       "Protection From Energy", "Psionic Blast", "Pulse Wave", "Remove Curse", "Revivify", "Sending", "Sleet Storm", "Slow", "Speak With Dead", "Speak With Plants", "Spirit Guardians", "Spirit Shroud",
       "Stinking Cloud", "Summon Fey", "Summon Lesser Demons", "Summon Shadowspawn", "Summon Undead", "Summon Warrior Spirit", "Thunder Step", "Tidal Wave", "Tiny Servant", "Tongues",
       "Vampiric Touch", "Wall Of Sand", "Wall Of Water", "Water Breathing", "Water Walk", "Wind Wall"
    ],
    "LevelFour": [],
    "LevelFive": [],
    "LevelSix": [],
    "LevelSeven": [],
    "LevelEight": [],
    "LevelNine": []
}
WizardSpells = [
    # Cantrips
    Spells["Cantrips"][0], # First Cantrip
    Spells["Cantrips"][1],
    Spells["Cantrips"][2],
    Spells["Cantrips"][3],
    Spells["Cantrips"][4],
    Spells["Cantrips"][5],
    Spells["Cantrips"][6],
    Spells["Cantrips"][10], # jump to Encode Thoughts
    Spells["Cantrips"][11],
    Spells["Cantrips"][12],
    Spells["Cantrips"][13],
    Spells["Cantrips"][14],
    Spells["Cantrips"][16], # jump to Gust
    Spells["Cantrips"][18], # jump to Infestation
    Spells["Cantrips"][19],
    Spells["Cantrips"][20],
    Spells["Cantrips"][21],
    Spells["Cantrips"][23], # jump to Mending
    Spells["Cantrips"][24],
    Spells["Cantrips"][25],
    Spells["Cantrips"][26],
    Spells["Cantrips"][27],
    Spells["Cantrips"][28],
    Spells["Cantrips"][29],
    Spells["Cantrips"][32],
    Spells["Cantrips"][35],
    Spells["Cantrips"][36],
    Spells["Cantrips"][39], # jump to Shocking Grasp
    Spells["Cantrips"][40],
    Spells["Cantrips"][43], # jump to Thunderclap
    Spells["Cantrips"][44],
    Spells["Cantrips"][45]
]

def rollDice(num_dice, num_sides):
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, num_sides))
    return rolls # Example: (variable) = rollDice(2, 10) rolls 2 10 sided dice.

if PlayerClass == "Rogue": 
    SneakAttack = True
