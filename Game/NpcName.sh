#!/bin/bash

# Arrays of possible name components
first_names=("Grim" "Thorn" "Sable" "Vex" "Fenrir" "Raven" "Silas" "Luna" "Astrid" "Rowan")
last_names=("Darkblade" "Shadowhunter" "Blackthorn" "Nightshade" "Bloodfang" "Duskwalker" "Ravensong" "Moonshadow" "Deathwhisper" "Gloomreaper")

# Generate a random index for each array
first_index=$(( RANDOM % ${#first_names[@]} ))
last_index=$(( RANDOM % ${#last_names[@]} ))

# Concatenate the random first and last name
npc_name="${first_names[$first_index]} ${last_names[$last_index]}"

# Output the generated NPC name
echo "Generated NPC name: $npc_name"
