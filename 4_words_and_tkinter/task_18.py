sentence = input("Enter sentences: ")

symbols = 0
i = 0

while i < len(sentence):
    if sentence[i].lower() in "aeiouõäöü":
        symbols += 1
    i += 1

print('Total vowels: ' + str(symbols))