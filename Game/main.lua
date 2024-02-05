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

lume = require "lume"

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
    "Dancing Lights"
    -- Too many more
  },
  LevelOne = {
    "Absorb Elements", "Acid Stream", "Alarm", "Animal Friendship",
    "Arcane Weapon"
  },
  LevelTwo = {
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

if PlayerClass == "Rogue" then
  SneakAttack = true
end
