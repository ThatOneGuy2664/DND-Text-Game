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

# this includes UA, Tasha's Cauldron of Everything, and other optional spells

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
  "LevelOne": ["Absorb Elements", "Alarm", "Animal Friendship", "Beast Bond", "Cure Wounds"],
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
  "LevelTwo": ["Aid", "Branding Smite"],
  "LevelThree": ["Aura of Vitality", "Blinding Smite"],
  "LevelFour": ["Aura of Life", "Aura of Purity", "Banishment"],
  "LevelFive": ["Banishing Smite", "Circle Of Power"]
  # Paladin spells stop at level 5
}

# Bloodhunters use Warlock spells, Arcane Trickster Rogues use Wizard spells

# schools
EnchantmentSpells = {
  "EnchantmentCantrips": ["Encode Thoughts", "Friends", "Mind Sliver", "Vicious Mockery"]
  "EnchantmentLevelOne": ["Animal Friendship", "Bane", "Bless"]
}
AbjurationSpells = {}
ConjurationSpells = {}
NecromancySpells = {}
EvocationSpells = {}
DivinationSpells = {}
IllusionSpells = {}
TransmutationSpells = {}
