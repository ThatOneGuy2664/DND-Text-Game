local str = "apple,banana,orange"
local result = {}
for word in string.gmatch(str, "([^,]+)") do
    table.insert(result, word)
end
-- result is now an array containing {"apple", "banana", "orange"}
-- this is an example
