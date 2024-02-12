#!/bin/bash

# Run Lua script to generate cantrips.txt
lua FeatsList.lua

# Run Python script to read from cantrips.txt
python main.py
