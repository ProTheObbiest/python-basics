import requests

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
file_path = '7_data_exchange/url_content.txt'

response = requests.get(url)
byte_data = response.content

with open(file_path, "w", encoding="utf-8") as file:
    file.write(byte_data.decode('utf-8'))

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
