import requests
import os

# Replace YOUR_TOKEN with your Personal Access Token
token = os.environ["PERSONAL_ACCESS_TOKEN"]
headers = {"Authorization": f"token {token}"}

# Replace USERNAME with the GitHub username you want to fetch information about
username = os.environ["GITHUB_USERNAME"]
url = f"https://api.github.com/users/{username}"

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    user_data = response.json()
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public Repos: {user_data['public_repos']}")
else:
    print(f"Request failed with status code {response.status_code}")
