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
import os

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
                return choice # returns numerical value of chosen option, starting at 1 for first option
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
# Example usage:
# round_number(2.3) (will return 2)
 
# roll stats function
def roll_ability_score():
    # Roll 4d6 and drop the lowest value
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)
 
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
 
# Variables
PlayerHasInspiration = False # whether or not Player has inspiration, boolean to limit to one use.
PlayerProfBonus = 0 # Proficiency bonus
PlayerInGameTime = 0 # seconds numerical value that increases by 6 as turns go by, one turn is 6 seconds.
PlayerGold = 0.0 # player's gold pieces, < 1 is the decimal of silver/copper (tenths or hundredths respectively), >/= 100 is 1 (+1 per hundred) platinum as per 5e rules.
PlayerStrength = None # STR stat number
PlayerDexterity = None # DEX stat number
PlayerConstitution = None # CON stat number
PlayerIntelligence = None # INT stat number
PlayerWisdom = None # WIS stat number
PlayerCharisma = None # CHA stat number
PlayerSTRMod = None # STR mod to be assigned 
PlayerDEXMod = None # DEX mod to be assigned 
PlayerCONMod = None # CON mod to be assigned 
PlayerINTMod = None # INT mod to be assigned 
PlayerWISMod = None # WIS mod to be assigned
PlayerCHAMod = None # CHA mod to be assigned
PlayerClass = None # Player class
PlayerRace = None # Player race
PlayerRessistances = [""] # any resistances the player has
PlayerName = None # Player's soon-to-be name
PlayerBackground = None # soon-to-be player background
PlayerSize = None # soon-to-be player character size
PlayerLevel = 1 # Player level
PlayerBlindsight = 0 # in feet
PlayerDarkvision = 0 # in feet
PlayerSpeed = 0 # in feet
PlayerHasBreathWeapon = False
DragonbornSubRaceType = None
PlayerHasAction = True # action
PlayerHasBonusAction = True # bonus action
PlayerHasReaction = True # per round reaction
PlayerStarterGear = [""] # soon-to-be player starting gear defined by background and class to add to inventory (see below)
PlayerInv = [""] # soon-to-be player inventory
PlayerLangs = ["Common"] # soon-to-be languages the player knows
AllLangs = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"] # all languages
EnemyResistance = [ "" ] # resistance(s) of current enemy(s)
RangeFromPlayerToEnemy = None # in feet
Races = [ "Human", "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Tiefling" ] # self-explanatory
Classes = [ "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer", "Bloodhunter" ] # self-explanatory
Backgrounds = ["Acolyte", "Criminal / Spy", "Folk Hero", "Noble", "Sage", "Soldier", "Charlatan", "Haunted One"] # self-explanatory
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

# Generate and print stats using roll_ability_score()
def generate_ability_scores():
    global PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma
    
    player_stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    player_vars = [PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma]
    for i in range(len(player_stats)):
        player_vars[i] = roll_ability_score()
        print(player_stats[i], ":" ,player_vars[i])

    # assign stats to global variables
    PlayerStrength = player_vars[0]
    PlayerDexterity = player_vars[1]
    PlayerConstitution = player_vars[2]
    PlayerIntelligence = player_vars[3]
    PlayerWisdom = player_vars[4]
    PlayerCharisma = player_vars[5]

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
    else:
     print("Enemy out of range...")

# create character functions
def create_character():
    global PlayerRace, PlayerClass, PlayerBackground, PlayerName, PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma, PlayerLangs, DragonbornSubRaceType, PlayerHasBreathWeapon, PlayerRessistances, PlayerSpeed
  
    print("\n**** Rolled stats...\n")
    # Generate and print player ability scores
    generate_ability_scores()
        
    # select race
    print("\n**** Choose your race...\n")
    wait(1)
    race_choice = get_choice(Races) # show options
    
    # race option picked to playerrace variable
    match race_choice:
        case 1:
             PlayerRace = "Human" # these assign the playerrace variable
             PlayerStrength += 1 # + 1 all stats
             PlayerDexterity += 1 # + 1 all stats
             PlayerConstitution += 1 # + 1 all stats
             PlayerIntelligence += 1 # + 1 all stats
             PlayerWisdom += 1 # + 1 all stats
             PlayerCharisma += 1 # + 1 all stats
             PlayerSpeed = 30 # feet
             PlayerSize = "Medium" # size
             print("\nChoose your extra language:\n")
             wait(1)
             ExtraLang = get_choice(AllLangs)
             wait(1)
             match ExtraLang:
              case 1:
                        print("You already know Common.")
              case 2:
                 ExtraLang = "Dwarvish"
              case 3:
                 ExtraLang = "Elvish"
              case 4:
                 ExtraLang = "Giant"
              case 5:
                 ExtraLang = "Gnomish"
              case 6:
                 ExtraLang = "Goblin"
              case 7:
                 ExtraLang = "Halfling"
              case 8:
                 ExtraLang = "Orc"
              case 9:
                 ExtraLang = "Abyssal"
              case 10:
                 ExtraLang = "Celestial"
              case 11:
                 ExtraLang = "Draconic"
              case 12:
                 ExtraLang = "Deep Speech"
              case 13:
                 ExtraLang = "Infernal"
              case 14:
                 ExtraLang = "Primordial"
              case 15:
                 ExtraLang = "Sylvan"
              case 16:
                 ExtraLang = "Undercommon"
             PlayerLangs.append(ExtraLang)
             wait(1)
             print("\nYou know the languages...")
             print(PlayerLangs)
        case 2:
            PlayerStrength += 2
            PlayerCharisma += 1
            PlayerSpeed = 30 # feet
            PlayerSize = "Medium"
            PlayerRace = "Dragonborn"
            PlayerHasBreathWeapon = True
            wait(1)
            print("\nPick your Draconic Ancestry:\n")
            wait(1)
            DragonbornSubCategory = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"] # Dragonborn Ancestry types
            DragonbornSubRaceType = get_choice(DragonbornSubCategory)
            wait(1)
            print("\nYou know the languages...")
            PlayerLangs = ["Common", "Draconic"]
            print(PlayerLangs)
            match DragonbornSubRaceType:
                case 1:
                        DragonbornSubRaceType = "Acid"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 2:
                        DragonbornSubRaceType = "Lightning"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 3:
                        DragonbornSubRaceType = "Fire"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 4:
                        DragonbornSubRaceType = "Lightning"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 5:
                        DragonbornSubRaceType = "Acid"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 6:
                        DragonbornSubRaceType = "Fire"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 7:
                        DragonbornSubRaceType = "Poison"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 8:
                        DragonbornSubRaceType = "Fire"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 9:
                        DragonbornSubRaceType = "Cold"
                        PlayerRessistances.append(DragonbornSubRaceType)
                case 10:
                        DragonbornSubRaceType = "Cold"
                        PlayerRessistances.append(DragonbornSubRaceType)
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
    print("\n**** Choose your background...\n")
    wait(1)
    Backgroundchoice = get_choice(Backgrounds)
    # Backgrounds = ["Acolyte", "Criminal / Spy", "Folk Hero", "Noble", "Sage", "Soldier", "Charlatan", "Haunted One"]
    match Backgroundchoice:
     case 1:
        PlayerBackground = "Acolyte"
     case 2:
        PlayerBackground = "Criminal"
     case 3:
         PlayerBackground = "Folk Hero"
     case 4:
        PlayerBackground = "Noble"
     case 5:
        PlayerBackground = "Sage"
     case 6:
        PlayerBackground = "Soldier"
     case 7:
        PlayerBackground = "Charlatan"
     case 8:
        PlayerBackground = "Haunted One"
    wait(1)
    print("\n**** You chose " + PlayerBackground + " as your background.")
	
    wait(1)
    PlayerName = input("\n**** What would you like to name your character? ")
    
    wait(1)
    print("\nYour character name is " + PlayerName + ".")
    
    wait(1)
    
    print("\n**** CHARACTER INFORMATION ****\n")
    print("Strength:", PlayerStrength)
    print("Dexterity:", PlayerDexterity)
    print("Constitution:", PlayerConstitution)
    print("Intelligence: ", PlayerIntelligence)
    print("Wisdom: ", PlayerWisdom)
    print("Charisma: ", PlayerCharisma)
    print("Race:", PlayerRace)
    print("Class:", PlayerClass)
    print("Background:", PlayerBackground)
    print("Character Name:", PlayerName)

    print("\n**** Choose this character or start over? ")
    choice = ["Choose this character.", "Start over."]
    PickedCharCreateOption = get_choice(choice)
    if PickedCharCreateOption == 1:
            wait(1)
            print("\nCharacter creation complete!\n")
            # next function to start game
    else:
        wait(1)
        print("Starting over...\n")
        wait(1)

        create_character()

def load_character(): # load an existing character from character_info.txt
    global PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma, PlayerRace, PlayerClass, PlayerBackground, PlayerName
    char_data = {}

    # Get the current directory
    current_directory = os.getcwd()

    # Get list of files in the current directory with a .txt extension and sort them by name
    txt_files = sorted([file for file in os.listdir(current_directory) if file.endswith(".txt")])

    # Load the list of .txt files
    print("\n**** Which save file would you like to load?\n")
    wait(1)
    selected_index = get_choice(txt_files) # show options
    selected_file = txt_files[selected_index - 1]


    with open(selected_file, "r") as file:
        for line in file.readlines():
            if not line.startswith('#'):
                key, value = map(str.strip, line.split(':', 1))
                char_data[key] = value

    print(char_data) # test
    # Assign each key to a separate variable
    for key, value in char_data.items():
        globals()[key] = value

    try:
        wait(1)
        print("\n**** CHARACTER INFORMATION ****\n")
        print("Strength:", PlayerStrength)
        print("Dexterity:", PlayerDexterity)
        print("Constitution:", PlayerConstitution)
        print("Intelligence: ", PlayerIntelligence)
        print("Wisdom: ", PlayerWisdom)
        print("Charisma: ", PlayerCharisma)
        print("Race:", PlayerRace)
        print("Class:", PlayerClass)
        print("Background:", PlayerBackground)
        print("Character Name:", PlayerName)
    except ValueError:
        wait(1)
        print("\nERROR: Unable to load character information...")
        wait(1)
        read_or_write()

    wait(1)
    print("\n**** Load this character data? ")
    Yesno = ["Yes", "No"]
    PickedCharCreateOption = get_choice(Yesno)
    if PickedCharCreateOption == 1:
            wait(1)
            print("\nCharacter data loaded!\n")
            # next function to start game
    else:
        wait(1)
        # Call create_character() again to reset Player(variables)
        read_or_write()

# function to create a character or load an existing one
def read_or_write():
    wait(1)
    print("\n**** Would you like to create a new character or load an existing character?\n")
    wait(1)
    neworload_char = [ "Create new character", "Load existing character" ]
    char_choices = get_choice(neworload_char)
    match char_choices:
        case 1:
            wait(1)
            create_character()
            save_character()
        case 2:
            wait(1)
            load_character()

# finish character functions
print("**** Welcome to DND-Text-Game! ****")

# save character data to new file
def save_character():
    global PlayerRace, PlayerClass, PlayerName, PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma
    char_data = {
    "PlayerStrength":PlayerStrength,
    "PlayerDexterity":PlayerDexterity,
    "PlayerConstitution":PlayerConstitution,
    "PlayerIntelligence":PlayerIntelligence,
    "PlayerWisdom":PlayerWisdom,
    "PlayerCharisma":PlayerCharisma,
    "PlayerRace":PlayerRace,
    "PlayerClass":PlayerClass,
    "PlayerBackground":PlayerBackground,
    "PlayerName":PlayerName
    }

    # write data to a new file
    with open("new_info.txt", "w") as new_file:
        new_file.write("# character sheet\n")
        for key, value in char_data.items():
            new_file.write(f"{key}: {value}\n")

# create a new character or load an existing one
read_or_write()

# end character creation
# start applying and/or changing globals relating to chosen race and class

def refresh_stat_mods():
        global PlayerSTRMod, PlayerDEXMod, PlayerCONMod, PlayerINTMod, PlayerWISMod, PlayerCHAMod, PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma
        PlayerSTRMod = (PlayerStrength - 10) // 2
        PlayerDEXMod = (PlayerDexterity - 10) // 2
        PlayerCONMod = (PlayerConstitution - 10) // 2
        PlayerINTMod = (PlayerIntelligence - 10) // 2
        PlayerWISMod = (PlayerWisdom - 10) // 2
        PlayerCHAMod = (PlayerCharisma - 10) // 2

# define ASI (ability score increase) function for ASI on level-up, all classes use ASIs
def ability_score_increase():
    print("Pick an ability score to increase.")
    global PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma
    AbilIncOpts = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    PickedInc = get_choice(AbilIncOpts)
    match AbilIncOpts:
     case 1:
         PlayerStrength += 2
     case 2:
         PlayerDexterity += 2
     case 3:
         PlayerConstitution += 2
     case 4:
         PlayerIntelligence += 2
     case 5:
         PlayerWisdom += 2
     case 6:
         PlayerCharisma += 2
         refresh_stat_mods()

# PlayerClass abilities/passives for all classes
# Barbarian
BarbarianRage = False
BarbarianUnarmoredDef = False
BarbarianRecklessAtk = False
BarbarianDangerSense = False
BarbarianFastMove = False
BarbarianFeral = False
BarbarianBrutalCrit = 0 # extra di(c)e rolled
BarbarianRelentlessRage = False
BarbarianBetterRage = False
BarbarianMight = False
BarbarianPrimalChamp = False
# Bard
BardicInspirationAbility = 0 # uses
JackOfAllTrades = False
CounterCharmAbility = False # passively grants new active action, basically a toggle
BetterInspiration = False
# Cleric
ChannelDivinity = 0 # non-boolean for more than once per rest at higher levels
DestroyUndead = False # passive = boolean
DestroyUndeadCR = 0 # variable related to DestroyUndead
DivineIntervention = False # boolean for one time, on/off use
# Druid
Druidic = False
# General features (more than one class uses these)
ExtraAtk = 0
SpellcastingAbil = None

# matching the null variables to the chosen class and make them not = null for that class's variables
match PlayerClass:
 case "Barbarian":
	 BarbarianRage = True
	 BarbarianUnarmoredDef = True
 case "Bard":
	 SpellcastingAbil = PlayerCharisma
	 BardicInspirationAbility = (PlayerCharisma - 10) // 2 # CHA mod
 case "Cleric":
	 SpellcastingAbil = PlayerWisdom
 case "Druid":
	 SpellcastingAbil = PlayerWisdom
	 Drudic = True

# Refresh player stats after bonuses are applied
refresh_stat_mods()
