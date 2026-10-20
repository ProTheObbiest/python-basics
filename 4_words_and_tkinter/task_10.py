sentence = input("Enter a sentence: ")
find = input("Enter replaceable word: ")
replace_with = input("Enter word to put: ")

new_sentence = sentence.replace(find, replace_with)

print("New sentence is: " + new_sentence)