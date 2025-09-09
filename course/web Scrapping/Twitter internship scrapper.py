import requests
import pandas as pd

BEARER_TOKEN = 'YOUR_TWITTER_BEARER_TOKEN'  # Replace this with your token

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Keywords that usually show up in academic opportunities
query = (
    '(phd OR "phd position" OR "master position" OR "fully funded") '
    '("apply now" OR "open position" OR "graduate position") '
    '-is:retweet lang:en'
)

params = {
    'query': query,
    'max_results': 10,  # Max is 100 for recent search
    'tweet.fields': 'author_id,created_at,text',
    'expansions': 'author_id',
    'user.fields': 'username,name',
}

def get_tweets():
    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}, {response.text}")
    return response.json()

def extract_tweet_info(data):
    users = {u['id']: u for u in data.get('includes', {}).get('users', [])}
    tweets_info = []

    for tweet in data.get('data', []):
        user = users.get(tweet['author_id'], {})
        tweet_url = f"https://twitter.com/{user.get('username')}/status/{tweet['id']}"

        tweets_info.append({
            'Date': tweet['created_at'],
            'Username': user.get('username'),
            'Name': user.get('name'),
            'Text': tweet['text'],
            'Tweet_URL': tweet_url
        })

    return pd.DataFrame(tweets_info)

if __name__ == "__main__":
    data = get_tweets()
    df = extract_tweet_info(data)
    print(df[['Date', 'Username', 'Text', 'Tweet_URL']].head())
    df.to_csv('phd_masters_positions_twitter.csv', index=False)