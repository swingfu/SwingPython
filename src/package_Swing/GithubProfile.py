import requests
import json
from dataclasses import dataclass

@dataclass
class GitHubProfile:
    login: str
    name: str
    bio: str
    avatar_url: str
    html_url: str

def get_github_profile(username: str) -> GitHubProfile:
    url = 'https://api.github.com/users/{}'.format(username)
    page = requests.get(url)
    content = json.loads(page.text)
    print(content)

     # check if the username exists
    
    if 'login' in content:

     # get the specific key-value from the string
        login = content['login']
        name = content['name']
        bio = content['bio']
        avatar_url = content['avatar_url']
        html_url = content['html_url']

        profile = GitHubProfile(
            login,
            name,
            bio,
            avatar_url,
            html_url
            )

        return profile
    
    else:
        return None
