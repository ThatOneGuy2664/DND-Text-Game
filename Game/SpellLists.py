# MIT License   
#    
# Copyright (c) 2024 ThatOneGuy2664 from Github
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

BardSpells = {
  "Cantrips": [
    "Blade Ward", "Dancing Lights", "Friends", "Light",
    "Mage Hand", "Mending", "Message", "Minor Illusion",
    "Prestidigitation", "Thunderclap", "True Strike", "Vicious Mockery" ],
  "LevelOne": [
    "Animal Friendship", "Bane", "Charm Person", "Color Spray",
    "Command", "Comprehend Languages", "Cure Wounds", "Detect Magic",
    "Disguise Self", "Dissonant Whispers", "Distort Value", "Earth Tremor",
    "Faerie Fire", "Feather Fall", "Guiding Hand", "Healing Word", "Heroism",
    "Identify", "Illusory Script", "Longstrider", "Puppet", "Sense Emotion",
    "Silent Image", "Silvery Barbs", "Sleep", "Speak with Animals", "Sudden Awakening",
    "Tasha's Hideous Laughter", "Thunderwave", "Unearthly Chorus", "Unseen Servant" ],
  "LevelTwo": [
    "Aid", "Animal Messenger", "Blindness/Deafness", "Borrowed Knowledge", "Calm Emotions",
    "Cloud Of Daggers", "Crown Of Madness", "Detect Thoughts", "Enhance Ability" ],
  "LevelThree": [],
  "LevelFour": [],
  "LevelFive": [],
  "LevelSix": [],
  "LevelSeven": [],
  "LevelEight": [],
  "LevelNine": []
}
RangerSpells = {
  # Rangers don't have Cantrips
  "LevelOne": ["Absorb Elements", "Alarm", "Animal Friendship", "Beast Bond", "Cure Wounds", "Detect Magic",
               "Detect Poison And Disease", "Ensnaring Strike", "Entangle", "Fog Cloud", "Goodberry",
               "Hail Of Thorns", "Hunter's Mark", "Jump", "Longstrider", "Searing Smite", "Snare",
               "Speak With Animals", "Sudden Awakening", "Wild Cunning", "Zephyr Strike"],
  "LevelTwo": [],
  "LevelThree": [],
  "LevelFour": [],
  "LevelFive": []
  # Ranger spells stop at level 5
}
WizardSpells = {
  "Cantrips": [],
  "LevelOne": [],
  "LevelTwo": [],
  "LevelThree": [],
  "LevelFour": [],
  "LevelFive": [],
  "LevelSix": [],
  "LevelSeven": [],
  "LevelEight": [],
  "LevelNine": []
}
WarlockSpells = {
  "Cantrips": [],
  "LevelOne": [],
  "LevelTwo": [],
  "LevelThree": [],
  "LevelFour": [],
  "LevelFive": [],
  "LevelSix": [],
  "LevelSeven": [],
  "LevelEight": [],
  "LevelNine": []
}
SorcererSpells = {
  "Cantrips": ["Acid Splash", "Blade Ward", "Booming Blade"],
  "LevelOne": [],
  "LevelTwo": [],
  "LevelThree": [],
  "LevelFour": [],
  "LevelFive": [],
  "LevelSix": [],
  "LevelSeven": [],
  "LevelEight": [],
  "LevelNine": []
}
PaladinSpells = {
  # Paladins don't havs Cantrips
  "LevelOne": ["Bless", "Ceremony", "Command", "Compelled Duel", "Cure Wounds", "Detect Evil And Good",
               "Detect Magic"],
  "LevelTwo": ["Aid", "Branding Smite", "Find Steed"],
  "LevelThree": ["Aura of Vitality", "Blinding Smite"],
  "LevelFour": ["Aura of Life", "Aura of Purity", "Banishment"],
  "LevelFive": ["Banishing Smite", "Circle Of Power"]
  # Paladin spells stop at level 5
}
ClericSpells = {
  "Cantrips": [],
  "LevelOne": [],
  "LevelTwo": [],
  "LevelThree": [],
  "LevelFour": [],
  "LevelFive": [],
  "LevelSix": [],
  "LevelSeven": [],
  "LevelEight": [],
  "LevelNine": []
}

# Bloodhunters use Warlock spells, Arcane Trickster Rogues use Wizard spells

# schools of magic
EnchantmentSpells = {
  "EnchantmentCantrips": ["Encode Thoughts", "Friends", "Mind Sliver", "Vicious Mockery"],
  "EnchantmentLevelOne": ["Animal Friendship", "Bane", "Bless", "Charm Person", "Command", "Compelled Duel",
                          "Dissonant Whispers", "Heroism", "Hex", "Id Insinuation", "Puppet", "Silvery Barbs",
                          "Sleep", "Sudden Awakening", "Tasha's Hideous Laughter"],
  "EnchantmentLevelTwo": [],
  "EnchantmentLevelThree": [],
  "EnchantmentLevelFour": [],
  "EnchantmentLevelFive": [],
  "EnchantmentLevelSix": [],
  "EnchantmentLevelSeven": [],
  "EnchantmentLevelEight": [],
  "EnchantmentLevelNine": []
}
AbjurationSpells = {
  "AbjurationCantrips": ["Blade Ward", "Resistance", "Virtue"],
  "AbjurationLevelOne": [],
  "AbjurationLevelTwo": [],
  "AbjurationLevelThree": [],
  "AbjurationLevelFour": [],
  "AbjurationLevelFive": [],
  "AbjurationLevelSix": [],
  "AbjurationLevelSeven": [],
  "AbjurationLevelEight": [],
  "AbjurationLevelNine": []
}
ConjurationSpells = {
  "ConjurationCantrips": ["Acid Splash", "Create Bonfire", "Infestation", "Mage Hand", "Poison Spray", "Produce Flame", "Sword Burst"],
  "ConjurationLevelOne": [],
  "ConjurationLevelTwo": [],
  "ConjurationLevelThree": [],
  "ConjurationLevelFour": [],
  "ConjurationLevelFive": [],
  "ConjurationLevelSix": [],
  "ConjurationLevelSeven": [],
  "ConjurationLevelEight": [],
  "ConjurationLevelNine": []
}
NecromancySpells = {
  "NecromancyCantrips": ["Chill Touch", "Decompose", "Sapping Sting", "Spare The Dying", "Toll The Dead"],
  "NecromancyLevelOne": ["Cause Fear", "False Life", "Inflict Wounds", "Ray Of Sickness"],
  "NecromancyLevelTwo": ["Blindness/Deafness", "Gentle Repose", "Ray of Enfeeblement", "Wither And Bloom"],
  "NecromancyLevelThree": ["Animate Dead", "Bestow Curse", "Feign Death", "Life Transference", "Revivify", "Speak with Dead",
                           "Spirit Shroud", "Summon Undead", "Vampric Touch"],
  "NecromancyLevelFour": ["Blight", "Shadow Of Moil", "Spirit Of Death"],
  "NecromancyLevelFive": ["Contagion", "Danse Macabre", "Enervation", "Negative Energy Flood", "Raise Dead"],
  "NecromancyLevelSix": ["Circle of Death", "Create Undead", "Eyebite", "Harm", "Magic Jar", "Soul Cage"],
  "NecromancyLevelSeven": ["Finger of Death", "Resurrection", "Tether Essence"],
  "NecromancyLevelEight": ["Abi-Dalzim's Horrid Wilting", "Clone"],
  "NecromancyLevelNine": ["Astral Projection", "Time Ravage", "True Resurrection"]
}
EvocationSpells = {
  "EvocationCantrips": [],
  "EvocationLevelOne": [],
  "EvocationLevelTwo": [],
  "EvocationLevelThree": [],
  "EvocationLevelFour": [],
  "EvocationLevelFive": [],
  "EvocationLevelSix": [],
  "EvocationLevelSeven": [],
  "EvocationLevelEight": [],
  "EvocationLevelNine": []
}
DivinationSpells = {
  "DivinationCantrips": ["Guidance", "True Strike"],
  "DivinationLevelOne": [],
  "DivinationLevelTwo": ["Augury", "Beast Sense", "Borrowed Knowledge", "Detect Thoughts", "Find Traps", "Fortune's Favor", "Locate Animals or Plants", "Locate Object", "Mind Spike", "See Invisibility", "Warp Sense"],
  "DivinationLevelThree": ["Clairvoyance", "Tongues"],
  "DivinationLevelFour": ["Arcane Eye", "Divination", "Locate Creature"],
  "DivinationLevelFive": ["Commune", "Commune with City", "Commune with Nature", "Contact Other Plane", "Legend Lore", "Rary's Telepathic Bond", "Scrying"],
  "DivinationLevelSix": ["Find the Path", "True Seeing"],
  "DivinationLevelSeven": [], # none
  "DivinationLevelEight": [], # none
  "DivinationLevelNine": ["Foresight"]
}
IllusionSpells = {}
TransmutationSpells = {}
