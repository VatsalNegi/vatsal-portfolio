import urllib.request
import json
url = "https://api.github.com/users/VatsalNegi/repos?per_page=100"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
with open("repos.txt", "w", encoding="utf-8") as f:
    for r in data:
        name = r.get("name", "")
        html_url = r.get("html_url", "")
        description = r.get("description", "No description")
        topics = r.get("topics", [])
        f.write(f"{name}: {html_url} - {description} - {topics}\n")
