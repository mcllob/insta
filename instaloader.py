import instaloader

L = instaloader.Instaloader()
L.login('your_username', 'your_password')

profile = instaloader.Profile.from_username(L.context, 'your_username')

for post in profile.get_posts():
    L.download_post(post, target=profile.username)

import requests
from bs4 import BeautifulSoup

def get_user_info(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tag = soup.find('meta', property='og:description')
    content = meta_tag['content']
    return content

username = "instagram"
user_info = get_user_info(username)
print(user_info)