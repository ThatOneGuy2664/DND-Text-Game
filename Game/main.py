# MIT License   
#   
# Copyright (c) 2024 ThatOneGuy2664 from Github
# Copyright (c) 2024 Twaddler01 from Github
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

# Eventually, I am planning to use Kivy/KivyMD for play outside console, for now however it's console only.

# Imports
import random # random numerical values
import time # to prevent walls of text with wait()
import os

# Spells
from SpellLists import BardSpells # import spell dictionaries for classes
from SpellLists import WizardSpells
from SpellLists import WarlockSpells
from SpellLists import RangerSpells
from SpellLists import EvocationSpells # schools of magic and their spells
from SpellLists import NecromancySpells
from SpellLists import AbjurationSpells
from SpellLists import ConjurationSpells
from SpellLists import DivinationSpells
from SpellLists import EnchantmentSpells

# Functions

# pause for (seconds)
def wait(seconds):
    # Wait for (seconds) and resume
    time.sleep(seconds)

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
                wait(1)
                print("\nInvalid choice. Please enter a number within the range of options.\n")
        except ValueError:
            wait(1)
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
PlayerHP = 0 # to be assigned
PlayerHPMax = 0 # to be assigned
PlayerClass = None # Player class
PlayerRace = None # Player race
PlayerRessistances = [] # any resistances the player has
PlayerName = None # Player's soon-to-be name
PlayerBackground = None # soon-to-be player background
PlayerSize = None # soon-to-be player character size
PlayerLevel = 1 # Player level
PlayerBlindsight = 0 # in feet
PlayerDarkvision = 0 # in feet
PlayerSpeed = 0 # in feet
PlayerHasBreathWeapon = False # Dragonborn only
DragonbornSubRaceType = None # Dragonborn only
PlayerSpells = None # Spells player knows
PlayerHasAction = True # action
PlayerHasBonusAction = True # bonus action
PlayerHasReaction = True # per round reaction
PlayerStarterGear = None # soon-to-be player starting gear defined by background and class to add to inventory (see below)
PlayerInv = [] # soon-to-be player inventory
PlayerLangs = ["Common"] # soon-to-be languages the player knows
AllLangs = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"] # all languages
EnemyResistance = [] # resistance(s) of current enemy(s)
RangeFromPlayerToEnemy = None # in feet
Races = [ "Human", "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Tiefling" ] # self-explanatory
Classes = [ "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer", "Bloodhunter" ] # self-explanatory
Backgrounds = ["Acolyte", "Criminal / Spy", "Folk Hero", "Noble", "Sage", "Soldier", "Charlatan", "Haunted One"] # self-explanatory

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

def refresh_stat_mods():
        global PlayerSTRMod, PlayerDEXMod, PlayerCONMod, PlayerINTMod, PlayerWISMod, PlayerCHAMod, PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma
        PlayerSTRMod = (PlayerStrength - 10) // 2
        PlayerDEXMod = (PlayerDexterity - 10) // 2
        PlayerCONMod = (PlayerConstitution - 10) // 2
        PlayerINTMod = (PlayerIntelligence - 10) // 2
        PlayerWISMod = (PlayerWisdom - 10) // 2
        PlayerCHAMod = (PlayerCharisma - 10) // 2

def print_player_stats():
        refresh_stat_mods()
        print("\n**** CHARACTER INFORMATION ****\n")
        print("Strength:", PlayerStrength, " +", PlayerSTRMod)
        print("Dexterity:", PlayerDexterity, " +", PlayerDEXMod)
        print("Constitution:", PlayerConstitution, " +", PlayerCONMod)
        print("Intelligence: ", PlayerIntelligence, " +", PlayerINTMod)
        print("Wisdom: ", PlayerWisdom, " +", PlayerWISMod)
        print("Charisma: ", PlayerCharisma, " +", PlayerCHAMod)
        print("Race:", PlayerRace)
        print("Class:", PlayerClass)
        print("Background:", PlayerBackground)
        print("Character Name:", PlayerName)
        print("Languages:", PlayerLangs)
        if PlayerDarkvision > 0:
            print("Darkvision: ", (PlayerDarkvision), "feet")
        if PlayerBlindsight > 0:
            print("Blindsight: ", (PlayerBlindsight), "feet")
        if PlayerRessistances not []:
            print("Resistances: ", (PlayerRessistances))

# create character functions
def create_character():
    global PlayerRace, PlayerClass, PlayerBackground, PlayerName, PlayerStrength, PlayerDexterity, PlayerConstitution, PlayerIntelligence, PlayerWisdom, PlayerCharisma, PlayerLangs, DragonbornSubRaceType, PlayerHasBreathWeapon, PlayerRessistances, PlayerSpeed, PlayerDarkvision
  
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
             wait(1) # wait a second
             ExtraLang = get_choice(AllLangs) # Humans get an extra language
             wait(1) # wait a second
             match ExtraLang:
              case 1:
                 wait(1)
                 print("You already know Common.")
                 ExtraLang = ""
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
            print("\nPick your Draconic Ancestry:\n") # determines added resistance and breath weapon damage type
            wait(1)
            DragonbornSubCategory = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"] # Dragonborn Ancestry types
            DragonbornSubRaceType = get_choice(DragonbornSubCategory) # get player choice of DragonbornSubCategory(s)
            wait(1)
            print("\nYou know the languages...")
            PlayerLangs = ["Common", "Draconic"]
            print(PlayerLangs)
            match DragonbornSubRaceType:
                case 1:
                        DragonbornSubRaceType = "Acid" # breath weapon type
                        PlayerRessistances.append(DragonbornSubRaceType) # add corresponding player ressistance
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
            PlayerSpeed = 30 # feet
            PlayerSize = "Medium"
            PlayerDarkvision = 60 # feet
            PlayerRessistances.append("Poison")
            PlayerLangs = ["Common", "Dwarvish"] # Dwarf's languages
            wait(1)
            print("What type of Dwarf are you?") # sub-race selection
            DwarfSubRaces = ["Hill Dwarf", "Mountain Dwarf"] # sub-race choices
            DwarfSubRacePicked = get_choice(DwarfSubRaces) # read player choice with numerical value chosen (1-2)
            wait(1)
            print("\nYou know the languages...") # print PlayerLangs array
            print(PlayerLangs)
            match DwarfSubRacePicked:
                case 1:
                        PlayerWisdom += 1 # +1 WIS
                        PlayerHPMax += PlayerLevel # +1 HPMax per level
                case 2:
                        PlayerStrength += 2
        case 4:
            PlayerRace = "Elf"
            PlayerDarkvision = 60 # feet
            PlayerDexterity += 2 # +2 Dex
            PlayerSize = "Medium" # player size
            PlayerSpeed = 30 # feet
            PlayerLangs = ["Common", "Elvish"] # Elf's languages
            wait(1)
            print("What type of Elf are you?")
            ElfSubRaces = ["Wood Elf", "High Elf", "Eladrin"]
            ElfSubRacePicked = get_choice(ElfSubRaces)
            match ElfSubRacePicked:
                case 1:
                        PlayerWisdom += 1
                        PlayerSpeed += 5 # 35 feet
                case 2:
                        PlayerIntelligence += 1
                        wait(1)
                        print("\nPick your extra language:\n")
                        ExtraLang = get_choice(AllLangs)
                        match ExtraLang:
                           case 1:
                                  wait(1)
                                  print("You already know Common.")
                                  ExtraLang = ""
                           case 2:
                                  ExtraLang = "Dwarvish"
                           case 3:
                                  wait(1)
                                  print("You already know Elvish")
                                  ExtraLang = ""
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
                        wait(1)
                        print("\nPick your Wizard Cantrip:\n")
                        wait(1)
                        #PlayerSpellPicked = get_choice(SpellList["Cantrips"])
                        # Make Wizard Cantrip only (eventually)
                        # Add to PlayerSpells array (eventually)
                case 3:
                        PlayerIntelligence += 1
                        # free Misty Step spell per rest
        case 5:
            PlayerRace = "Gnome"
            PlayerIntelligence += 2 # +2 INT
            PlayerSize = "Small" # Size
            PlayerSpeed = 25 # feet
            PlayerDarkvision = 60 # feet
            PlayerLangs = ["Common", "Gnomish"]
            GnomeSubRaces = ["Forest Gnome", "Rock Gnome"]
            wait(1)
            print("What kind of Gnome are you?") # subrace select prompt
            wait(1)
            GnomeSubRacePicked = get_choice(GnomeSubRaces) # select subrace
            match GnomeSubRacePicked:
                case 1:
                        PlayerDexterity += 1
                        # minor illusion at will
                case 2:
                        PlayerConstitution += 1
                        # tinker
        case 6:
            PlayerRace = "Half-Elf"
            PlayerCharisma += 1
            AbilIncOptsForHalfElf = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom"]
            PlayerDarkvision = 60 # feet
            PlayerSize = "Medium" # Size
            PlayerSpeed = 30 # feet
            PlayerLangs = ["Common", "Elvish"]
            wait(1)
            print("Choose a stat to increase by one:")
            wait(1)
            AbilIncOptPicked = get_choice(AbilIncOptsForHalfElf)
            match AbilIncOptPicked:
                case 1:
                        PlayerStrength += 1
                case 2:
                        PlayerDexterity += 1
                case 3:
                        PlayerConstitution += 1
                case 4:
                        PlayerIntelligence += 1
                case 5:
                        PlayerWisdom += 1
        case 7:
            PlayerRace = "Halfling"
            PlayerDexterity += 2
            PlayerSpeed = 25 # feet
            PlayerSize = "Small" # Size
            PlayerLangs = ["Common", "Halfling"]
            HalflingSubRaces = ["Lightfoot", "Stout"]
            wait(1)
            print("What kind of Halfling ard you?")
            wait(1)
            HalflingSubRacePicked = get_choice(HalflingSubRaces)
            match HalflingSubRacePicked:
                case 1:
                        PlayerCharisma += 1
                case 2:
                        PlayerConstitution += 1
        case 8:
            PlayerRace = "Half-Orc"
            PlayerStrength += 2
            PlayerConstitution += 1
            PlayerSize = "Medium"
            PlayerSpeed = 30 # feet
            PlayerDarkvision = 60 # feet
            PlayerLangs = ["Common", "Orc"]
            # no base sub-races
        case 9:
            PlayerRace = "Tiefling"
            PlayerIntelligence += 1
            PlayerCharisma += 2
            PlayerSize = "Medium"
            PlayerSpeed = 30 # feet
            PlayerDarkvision = 60 # feet
            PlayerRessistances.append("Fire")
            PlayerLangs = ["Common", "Infernal"]
            # no base sub-races
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
    print("\n**** Choose your background...\n") # assign a background
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
    PlayerName = input("\n**** What would you like to name your character? ") # naming the player character
    
    wait(1)
    print("\nYour character name is " + PlayerName + ".")
    
    wait(1)
    
    print_player_stats()

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
        print_player_stats()
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
            # start game (Game() is called later)
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

# Refresh player stats after bonuses are applied and before game start
refresh_stat_mods()

wait(1)

def Game():
    wait(1)
    print("What would you like to do?")
    GameOpts = ["View Stats"]
    GameOptPicked = get_choice(GameOpts)
    match GameOptPicked:
        case 1:
                print("\n")
                wait(1)
                print_player_stats()
                print("\n")
    # repeat function after other calls are completed
    Game()
                
Game()
