string1 = "Hello"
string2 = "World"
result = ""
i, j = 0, 0
while i < len(string1) and j < len(string2):
    result += string1[i] + string2[j]
    i += 1
    j += 1
result += string1[i:] + string2[j:]
print("-".join(result))
