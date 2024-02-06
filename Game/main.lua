-- MIT License
--
-- Copyright (c) 2024 ThatOneGuy2664
-- Copyright (c) 2024 Twaddler01
--
-- Permission is hereby granted, free of charge, to any person obtaining a copy
-- of this software and associated documentation files (the "Software"), to deal
-- in the Software without restriction, including without limitation the rights
-- to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-- copies of the Software, and to permit persons to whom the Software is
-- furnished to do so, subject to the following conditions:
--
-- The above copyright notice and this permission notice shall be included in all
-- copies or substantial portions of the Software.
--
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-- IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-- FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-- AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-- LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-- OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-- SOFTWARE.
-- END LICENSE DESCRIPTION
-- LUA allows for quicker updates, it will likely be done first.
-- must be played in console.

local PlayerClass = nil
local PlayerRace = nil
local PlayerLevel = 1
local Races = {
  "Human", "Dragonborn", "Dwarf",
  "Elf", "Gnome", "Half-Elf", "Halfing",
  "Half-Orc", "Tiefling"
}
local Classes = {
  "Barbarian", "Bard", "Cleric", "Druid",
  "Fighter", "Monk", "Paladin", "Ranger", "Rogue",
  "Sorcerer", "Warlock", "Wizard", "Artificer", "Bloodhunter"
}
local SneakAttack = false
local CunningAction = false

-- Roll 4d6 and drop the lowest value
function roll_ability_score()
    local rolls = {}
    for i = 1, 4 do
        table.insert(rolls, math.random(1, 6))
    end
    table.sort(rolls)
    table.remove(rolls, 1)
    local total = 0
    for _, roll in ipairs(rolls) do
        total = total + roll
    end
    return total
end

-- Generate ability scores for all stats
function generate_ability_scores()
    local ability_scores = {}
    local stats = {'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'}
    for _, stat in ipairs(stats) do
        ability_scores[stat] = roll_ability_score()
    end
    return ability_scores
end

-- Wait for (seconds) and resume
function wait(seconds)
    os.execute("sleep " .. seconds)
end

-- Generate ability scores
player_ability_scores = generate_ability_scores()

-- Print each ability score with its corresponding label
for stat, score in pairs(player_ability_scores) do
    print(stat .. ": " .. score)
end

local Spells = {
  Cantrips = {
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
  },
  LevelOne = {
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
  },
  LevelTwo = {
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
  },
  LevelThree = {
  },
  LevelFour = {
  },
  LevelFive = {
  },
  LevelSix = {
  },
  LevelSeven = {
  },
  LevelEight = {
  },
  LevelNine = {
  }
}
-- Define the WizardSpells table
WizardSpells = {
  -- Cantrips
  Spells["Cantrips"][1], -- First Cantrip
  Spells["Cantrips"][2],
  Spells["Cantrips"][3],
  Spells["Cantrips"][4],
  Spells["Cantrips"][5],
  Spells["Cantrips"][6],
  Spells["Cantrips"][7],
  Spells["Cantrips"][11], -- jump to Encode Thoughts
  Spells["Cantrips"][12],
  Spells["Cantrips"][13],
  Spells["Cantrips"][14],
  Spells["Cantrips"][15],
  Spells["Cantrips"][17], -- jump to Gust
  Spells["Cantrips"][19], -- jump to Infestation
  Spells["Cantrips"][20],
  Spells["Cantrips"][21],
  Spells["Cantrips"][22],
  Spells["Cantrips"][24], -- jump to Mending
  Spells["Cantrips"][25],
  Spells["Cantrips"][26],
  Spells["Cantrips"][27],
  Spells["Cantrips"][28],
  Spells["Cantrips"][29],
  Spells["Cantrips"][30],
  Spells["Cantrips"][33],
  Spells["Cantrips"][36],
  Spells["Cantrips"][37],
  Spells["Cantrips"][40], -- jump to Shocking Grasp
  Spells["Cantrips"][41],
  Spells["Cantrips"][44], -- jump to Thunderclap
  Spells["Cantrips"][45],
  Spells["Cantrips"][46]
}
function rollDice(num_dice, num_sides)
  local rolls = {}
  for i = 1, num_dice do
    table.insert(rolls, math.random(num_sides))
  end
  return rolls
end -- (variable) = rollDice(2, 10) rolls 2 10 sided dice.


if PlayerClass == "Rogue" then
  SneakAttack = true
end
