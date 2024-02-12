-- Lua script to save the array to a file named "cantrips.txt"
local str = "Actor,Alert,Artificer Initiate,Athlete"
local result = {}
for word in string.gmatch(str, "([^,]+)") do
    table.insert(result, word)
end

local file = io.open("feats.txt", "w")
for _, v in ipairs(result) do
    file:write(v .. "\n")
end
file:close()
