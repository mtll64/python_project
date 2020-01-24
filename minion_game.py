# Minion Game Program

string = input('Enter word in Uppercase: ')
vowels = "AEIOU"
stuart_points = 0
kevin_points = 0
index = 0
string_length = len(string)
while index < string_length:
    if string[index] not in vowels:
        h = string_length - index
        stuart_points += h
    if string[index] in vowels:
        h = string_length - index
        kevin_points += h
    index += 1
print(stuart_points, kevin_points)
if stuart_points > kevin_points:
    print("Stuart", stuart_points)
elif stuart_points < kevin_points:
    print("Kevin", kevin_points)
else:
    print("Draw")
