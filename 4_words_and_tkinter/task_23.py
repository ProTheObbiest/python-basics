sentence = input("Enter sentence: ")

length = len(sentence)
spaces = sentence.count(" ")
words = len(sentence.split())

vowels = "aeiouõäöü"

vows = sum(sentence.lower().count(vowel) for vowel in vowels)

numbers = "0123456789"

nums = sum(sentence.count(number) for number in numbers)

print("Characters: " + str(length))
print("Characters without spaces: " + str(length-spaces))
print("Words: " + str(words))
print("Vowels: " + str(vows))
print("Numbers: " + str(nums))