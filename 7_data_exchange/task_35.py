output_file = '7_data_exchange/text_analys.txt'

file_name = input("Enter the file name to analyze: ")
file_path = '7_data_exchange/' + file_name

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

words = len(text.split())
sentences = text.count(".") + text.count("!") + text.count("?")

longest = 0
longest_word = ""

word_list = text.lower().split()
clean_words = [w.strip("!.,?\"'():;") for w in word_list if w.strip("!.,?\"'():;")]

for word in clean_words:
    if len(word) > longest:
        longest = len(word)
        longest_word = word

unique_words = list(dict.fromkeys(clean_words))
top_5 = sorted(unique_words, key=clean_words.count, reverse=True)[:5]

print("Number of words:", words)
print("Number of sentences:", sentences)
print("Longest word:", longest_word)
print("Top 5 most common words:")
for word in top_5:
    print(word)

with open(output_file, "w", encoding="utf-8") as file:
    file.write("Number of words: " + str(words) + "\n")
    file.write("Number of sentences: " + str(sentences) + "\n")
    file.write("Longest word: " + longest_word + "\n")
    file.write("Top 5 most common words:\n")
    for word in top_5:
        file.write(word + "\n")