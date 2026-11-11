word = input("Enter word: ")
if word.lower() == word[::-1].lower():
    print('this word is palindrome')
else:
    print("this word isnt palidrome")