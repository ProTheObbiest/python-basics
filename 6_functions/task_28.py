def vowels(text):
    symbols = 0
    i = 0
    
    while i < len(text):
        if text[i].lower() in "aeiouõäöü":
            symbols += 1
        i += 1

    return symbols

text = input("Enter text: ")
print("This text contains: " + str(vowels(text)) + " vowels")