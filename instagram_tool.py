import requests
import pandas as pd

ACCESS_TOKEN = 'your_access_token'
USER_ID = 'your_user_id'  # Instagram User ID

def get_user_profile(user_id, access_token):
    url = f'https://graph.instagram.com/{user_id}'
    params = {
        'fields': 'id,username,account_type,media_count',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()

def get_user_media(user_id, access_token):
    url = f'https://graph.instagram.com/{user_id}/media'
    params = {
        'fields': 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == '__main__':
    user_profile = get_user_profile(USER_ID, ACCESS_TOKEN)
    print('User Profile:', user_profile)

    user_media = get_user_media(USER_ID, ACCESS_TOKEN)
    media_data = user_media.get('data', [])
    df = pd.DataFrame(media_data)
    print('User Media:', df)
