words = ["arvuti", "programmeerimine", "hiir", "klaviatuur", "monitor"]

length = 0
longest_word = ""
length2 = 999
shortest_word = ""
for word in words:
    if len(word) > length:
        length = len(word)
        longest_word = word
    if len(word) < length2:
        length2 = len(word)
        shortest_word = word

print(longest_word + ' - Longest Word')
print(shortest_word + ' - Shortest Word')