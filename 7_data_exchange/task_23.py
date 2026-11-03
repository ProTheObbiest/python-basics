import requests

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
file_path = '7_data_exchange/url_content.txt'

response = requests.get(url)
text_data = response.text

with open(file_path, "w", encoding="utf-8") as file:
    i = 0
    lines = text_data.splitlines()
    while i < 10:
        file.write(lines[i]+"\n")
        i += 1

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
