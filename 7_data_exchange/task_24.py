import requests

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
file_path = '7_data_exchange/url_content.txt'

response = requests.get(url)
text_data = response.text

lines = 0
words = 0
symbols = 0
empty_lines = 0

with open(file_path, "w", encoding="utf-8") as file:
    file.write(text_data)

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        lines += 1
        words += len(line.split(" "))
        symbols += len(line)
        if line == "":
            empty_lines += 1

print("Web text stats")
print("--------------")
print("Lines:",lines)
print("Words:",words)
print("Symbols:",symbols)
print("Empty lines:",empty_lines)
