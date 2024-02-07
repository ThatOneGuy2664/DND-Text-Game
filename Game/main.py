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

# Imports
import random
import time

# Functions

# Function to get player choice
def get_choice(options):
    while True:
        print("Choose an option:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter your choice: "))  # Read input from the console
            if 1 <= choice <= len(options):  # Check if choice is within the range of valid indices
                return choice # returns numerical value of chosen option, starting with 1
            else:
                print("\nInvalid choice. Please enter a number within the range of options.\n")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")
# Example usage:
# options = ["Option 1", "Option 2", "Option 3"]
# player_choice = get_choice(options)
# print(f"Player chose option {player_choice}")

# round function
def round_number(number):
    return round(number)
 
# roll stats function
def roll_ability_score():
    # Roll 4d6 and drop the lowest value
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)
 
# Generate stats function using roll_ability_score()
def generate_ability_scores():
    # Generate ability scores for all stats
    ability_scores = {}
    stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    for stat in stats:
        ability_scores[stat] = roll_ability_score()
    return ability_scores
 
# pause for (seconds)
def wait(seconds):
    # Wait for (seconds) and resume
    time.sleep(seconds)
 
# rolls (number of dice, number of sides of dice)
def rollDice(num_dice, num_sides):
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, num_sides))
    return rolls # Example: (variable) = rollDice(2, 10) rolls 2 10 sided dice.
 
# player Variables
inGameTime = 0 # seconds numerical value that increases by 6 as turns go by, one turn is 6 seconds.
PlayerGold = 0.0 # player's gold pieces, > 100 is the decimal of silver/copper, < 100 is platinum as per 5e rules.
PlayerStrength = None # soon-to-be STR stat number
PlayerDexterity = None # soon-to-be DEX stat number
PlayerConstitution = None # soon-to-be CON stat number
PlayerIntelligence = None # soon-to-be INT stat number
PlayerWisdom = None # soon-to-be WIS stat number
PlayerCharisma = None # soon-to-be CHA stat number
PlayerStrengthModifier = None # STR mod
PlayerDexterityModifier = None # DEX mod
PlayerConstitutionModifier = None # CON mod
PlayerIntelligenceModifier = None # INT mod
PlayerWisdomModifier = None # WIS mod
PlayerCharismaModifier = None # CHA mod
PlayerClass = None # soon-to-be player class
PlayerRace = None # soon-to-be player race
PlayerRessistances = None # any resistances the player has
PlayerLevel = 1 # Player level
PlayerLangs = ["Common"] # languages the player character knows
PlayerHasAction = True # action
PlayerHasBonusAction = True # bonus action
PlayerHasReaction = True # per round reaction
PlayerHasBreathWeapon = False # if PlayerRace is Dragonborn then player has a breath weapon attack
# end player variables
bonuslang = None # only relevant for Human race's extra language of choice
EnemyResistance = [ "" ] # resistance of current enemy(s)
rangeToEnemy = None # in feet
allLangs = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon", "Thieves Cant", "Drudic"]
SneakAttack = False # start Rogue only
CunningAction = False # Rogue only
UncannyDodge = False # Rogue only
Evasion = False # Rogue only
ReliableTalent = False # Rogue only
Elusive = False # Rogue only
StrokeOfLuck = 0 # end Rogue only. StrokeOfLuck is numerical value for uses per rest
Blindsight = 0 # in feet
Darkvision = 0 # in feet
Races = [ "Human", "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Tiefling" ] 
Classes = [ "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer", "Bloodhunter" ]
# http://dnd5e.wikidot.com/spells for spell list
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
    "LevelFour": [
       "Arcane Eye", "Aura Of Life", "Aura Of Purity", "Banishment", "Blight", "Charm Monster"
    ],
    "LevelFive": [],
    "LevelSix": [],
    "LevelSeven": [],
    "LevelEight": [],
    "LevelNine": []
}
WizardSpells = {
    # Cantrips
	"WizardCantrips": [
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
}

# spell functions
def acid_splash(): # Acid Splash cantrip
    if (rangeToEnemy <= 60): # in feet
        description = "You hurl a bubble of acid. Choose one creature you can see within range, or choose two creatures you can see within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage."
        duration = 0 # instant
        
        # action
        damage = rollDice(1, 6)
        if (PlayerLevel >= 5):
            damage += rollDice(1, 6)
        if (PlayerLevel >= 11):
            damage += rollDice(1, 6)
        if (PlayerLevel >=17):
            damage += rollDice(1, 6)
        # determine resistance
        if (EnemyResistance == "acid"):
            damage = damage / 2
    
        # end turn
        return damage
    # if out of range
    print("Enemy out of range...")

# create character functions
def load_racial_feats():
    global PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma, PlayerLangs
    match PlayerRace:
        case "Human":
            PlayerStrength += 1 
            PlayerDexterity += 1 
            PlayerConstitution += 1 
            PlayerIntelligence += 1 
            PlayerWisdom += 1 
            PlayerCharisma += 1 
            bonuslang = get_choice(allLangs) 
            if bonuslang is not None and bonuslang not in PlayerLangs: 
                PlayerLangs.append(bonuslang)
        case "Dragonborn":
	        PlayerHasBreathWeapon = True

def create_character():
    # Generate ability scores
    player_ability_scores = generate_ability_scores()
    print("\n**** Rolled stats...\n")
    # Print each ability score with its corresponding label
    for stat, score in player_ability_scores.items():
        print(f"{stat}: {score}")
        
    # select race
    print("\n**** Choose your race...\n")
    wait(1)
    race_choice = get_choice(Races) # show options
    
    # race option picked to playerrace variable
    match race_choice:
        case 1:
            PlayerRace = "Human" # these assign the playerrace variable
        case 2:
            PlayerRace = "Dragonborn"
        case 3:
            PlayerRace = "Dwarf"
        case 4:
            PlayerRace = "Elf"
        case 5:
            PlayerRace = "Gnome"
        case 6:
            PlayerRace = "Half-Elf"
        case 7:
            PlayerRace = "Halfling"
        case 8:
            PlayerRace = "Half-Orc"
        case 9:
            PlayerRace = "Tiefling"
    wait(1)
    print("\n**** You chose " + PlayerRace + " as your race.")
    
    # select class
    wait(1)
    print("\n**** Choose your class...\n")
    wait(1)
    
    class_choice = get_choice(Classes) # show options
    # Classes are: [ "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer", "Bloodhunter" ]
    match class_choice:
        case 1:
            PlayerClass = "Barbarian" # these assign the playerclass variable
        case 2:
            PlayerClass = "Bard"
        case 3:
            PlayerClass = "Cleric"
        case 4:
            PlayerClass = "Druid"
        case 5:
            PlayerClass = "Fighter"
        case 6:
            PlayerClass = "Monk"
        case 7:
            PlayerClass = "Paladin"
        case 8:
            PlayerClass = "Ranger"
        case 9:
            PlayerClass = "Rogue"
        case 10:
            PlayerClass = "Sorcerer"
        case 11:
            PlayerClass = "Warlock"
        case 12:
            PlayerClass = "Wizard"
        case 13:
            PlayerClass = "Artificer"
        case 14:
            PlayerClass = "Bloodhunter"
    wait(1)
    print("\n**** You chose " + PlayerClass + " as your class.")
    
    wait(1)
    PlayerName = input("\n**** What would you like to name your character? ")
    
    wait(1)
    print("\nYour character name is " + PlayerName + ".")
    
    wait(1)
    
    print("\n**** CHARACTER INFORMATION ****\n")
    for stat, score in player_ability_scores.items():
        print(f"{stat}: {score}")
    print("Race: " + PlayerRace)
    print("Class: " + PlayerClass)
    print("Character Name: " + PlayerName)
    ConfirmCharacter = input("\nConfirm this character? (y/n): ")
    if (ConfirmCharacter.upper() == "Y"):
        wait(1)
        print("\nCharacter creation complete!\n")
        # Assign ability scores to variables
        PlayerStrength = player_ability_scores['Strength']
        PlayerDexterity = player_ability_scores['Dexterity']
        PlayerConstitution = player_ability_scores['Constitution']
        PlayerIntelligence = player_ability_scores['Intelligence']
        PlayerWisdom = player_ability_scores['Wisdom']
        PlayerCharisma = player_ability_scores['Charisma']
	# Calculate ability score modifiers
        PlayerStrengthModifier = (PlayerStrength - 10) // 2
        PlayerDexterityModifier = (PlayerDexterity - 10) // 2 
        PlayerConstitutionModifier = (PlayerConstitution - 10) // 2 
        PlayerIntelligenceModifier = (PlayerIntelligence - 10) // 2
        PlayerWisdomModifier = (PlayerWisdom - 10) // 2 
        PlayerCharismaModifier = (PlayerCharisma - 10) // 2
        wait(1)
        load_racial_feats()

    else:
        wait(1)
        print("Starting over...\n")
        wait(1)

        # Generate ability scores
        player_ability_scores = generate_ability_scores()
        print("Your Stats:")
        # Print each ability score with its corresponding label
        for stat, score in player_ability_scores.items():
            print(f"{stat}: {score}")
        # Assign ability scores to variables
        PlayerStrength = player_ability_scores['Strength']
        PlayerDexterity = player_ability_scores['Dexterity']
        PlayerConstitution = player_ability_scores['Constitution']
        PlayerIntelligence = player_ability_scores['Intelligence']
        PlayerWisdom = player_ability_scores['Wisdom']
        PlayerCharisma = player_ability_scores['Charisma']
	# Calculate ability score modifiers 
        PlayerStrengthModifier = (PlayerStrength - 10) // 2
        PlayerDexterityModifier = (PlayerDexterity - 10) // 2 
        PlayerConstitutionModifier = (PlayerConstitution - 10) // 2 
        PlayerIntelligenceModifier = (PlayerIntelligence - 10) // 2
        PlayerWisdomModifier = (PlayerWisdom - 10) // 2 
        PlayerCharismaModifier = (PlayerCharisma - 10) // 2

        # Call create_character() again to reset Player(variables)
        create_character()

def load_character(): # load an existing character from character_info.txt
    char_data = {}
            
    with open("character_info.txt", "r") as file:
        for line in file.readlines():
            if not line.startswith('#'):
                key, value = map(str.strip, line.split(':', 1))
                char_data[key] = value
            
    print(char_data) # test
    # Assign each key to a separate variable
    for key, value in char_data.items():
        globals()[key] = value
    print("\n**** CHARACTER INFORMATION ****\n")
    print("Strength: " + PlayerStrength)
    print("Dexterity: " + PlayerDexterity)
    print("Constitution: " + PlayerConstitution)
    print("Intelligence: " + PlayerIntelligence)
    print("Wisdom: " + PlayerWisdom)
    print("Charisma: " + PlayerCharisma)
    print("Race: " + PlayerRace)
    print("Class: " + PlayerClass)
    print("Character Name: " + PlayerName)
        
    ConfirmCharacter = input("\nLoad this character data? (y/n): ")
    if (ConfirmCharacter.upper() == "Y"):
        wait(1)
        print("\nCharacter data loaded!\n")
        # next function to start game
    else:
        wait(1)
        print("Starting over...\n")
        wait(1)

        # Call create_character() again to reset Player(variables)
        create_character()

# create character or load existing
def read_or_write():
    print("\n**** Would you like to create a new character or load an existing character?\n")
    wait(1)
    neworload_char = [ "Create new character", "Load existing character" ]
    char_choices = get_choice(neworload_char)
    match char_choices:
        case 1:
            create_character()
        case 2:
            load_character()

# actual game code
print("**** Welcome to DND-Text-Game! ****")

# start function calls
# create new character or load existing
read_or_write()

# randomized adventure code
