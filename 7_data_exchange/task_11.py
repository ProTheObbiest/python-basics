import string

file_path = '7_data_exchange/text.txt'

longest_length = 0
longest_word = ""

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            word = word.strip(string.punctuation)
            if len(word) > longest_length:
                longest_length = len(word)
                longest_word = word

print("Longest word is " + str(longest_length) + " characters long (" + str(longest_word) + ")")