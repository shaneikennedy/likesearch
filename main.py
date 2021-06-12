import os
import sys
import argparse
from typing import Sequence
from twitter import Twitter, OAuth
from functools import reduce

class Like:
    def __init__(self, id: int, text: str, user_handle: str):
        self.id = id
        self.text = text
        self.user_handle = user_handle

    @property
    def url(self):
        return f'https://twitter.com/{self.user_handle}/status/{self.id}'

    def __str__(self):
        return f'"{self.text}" by {self.user_handle} at {self.url}"'

    def __repr__(self):
        return str(self)

def fetch_likes(client: Twitter, count: int, *args, **kwargs):
    return client.favorites.list(count=count, *args, **kwargs)

def search_likes(likes: Sequence[Like], q: str) -> Sequence[Like]:
    return [
        l for l in likes
        if l.text.lower().find(q) >= 0
    ]

def get_oldest_like(likes: Sequence[Like]) -> Like:
   return reduce(
        lambda l, oldest: l if l.id < oldest.id else oldest,
        likes,
        likes[0],
    )

def get_client() -> Twitter:
    # Sometimes called consumer keys in twitter api land
    api_token = os.getenv('TWITTER_API_TOKEN')
    api_secret = os.getenv('TWITTER_API_SECRET')

    auth_token = os.getenv('TWITTER_AUTH_TOKEN')
    auth_secret = os.getenv('TWITTER_AUTH_SECRET')

    # These are needed for the twitter client
    assert api_token
    assert api_secret
    assert auth_token
    assert auth_secret

    return Twitter(
        auth=OAuth(
            consumer_key=api_token,
            consumer_secret=api_secret,
            token=auth_token,
            token_secret=auth_secret
        )
    )

def get_cli_args():
    cli_parser = argparse.ArgumentParser(
        usage='python main.py "what you want to search"',
        description='pass a search string as an argument to this file to search your twitter likes',
    )
    cli_parser.add_argument('query', type=str, help='substring to query')
    cli_parser.add_argument('--first', default=True, help='Stop after the first hit(s)', choices=[True, False])
    args = cli_parser.parse_args()
    return args.query, args.first


if __name__ == '__main__':

    query, only_first = get_cli_args()
    twitter_client = get_client()
    search_hits = []

    # Make initial call to twitter to get latest likes
    likes = [
        Like(l['id'], l['text'], l['user']['screen_name'])
        for l in fetch_likes(twitter_client, 200)
    ]
    target_likes = search_likes(likes, query)
    search_hits += target_likes
    oldest_like = get_oldest_like(likes)

    # Poll while we still have older likes to search
    prev_oldest_like_id = 0
    while prev_oldest_like_id != oldest_like.id:

        if len(search_hits) > 0 and only_first:
            break

        try:
            likes = [
                Like(l['id'], l['text'], l['user']['screen_name'])
                for l in fetch_likes(twitter_client, 200, max_id=oldest_like.id)
            ]
        except ConnectionResetError:
            # Is this for my shit internet ...
            # or Twitter trying to get me to use their streaming api?
            continue

        print(f'Parsing {len(likes)} tweets...')
        target_likes = search_likes(likes, query)
        search_hits += target_likes
        prev_oldest_like_id = oldest_like.id
        oldest_like = get_oldest_like(likes)


    # Report
    num_found = len(search_hits)
    if num_found > 0:
        print(f'Found {num_found} likes matching {query}:')
        print([t for t in search_hits])
        sys.exit()

    print(f'No tweets matching {query} found.')
