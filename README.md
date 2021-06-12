# Like Searcher - For Twitter

Can't be bothered to use the UI to search tweets from last year let alone 10 years ago...

This little script will search as far back as your twitter likes go for a given query (beware of rate limiting!)

## Requirements
For this you're going to need some twitter api credentials, head [here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and get your api tokens/secrets (Sometimes called consumer keys in twitter api land) and your auth tokens/secrets. These are slurped up as environment variables by the script, so be sure that they're exported in your shell. I keep a file like the one below and then `source ./env.sh` when I need to use this. Yeah I know about autoenv, no im too lazy.

``` shell
#!/bin/bash

export TWITTER_API_TOKEN="your api token"
export TWITTER_API_SECRET="your api secret"
export TWITTER_AUTH_TOKEN="your auth token"
export TWITTER_AUTH_SECRET="your auth secret"
```

After that, set up a python virtualenv and make sure it's active. Once it is, install the requirements `pip install -r requirements.txt` and you're ready to go!

## Usage

``` shell
~/dev/shane/likesearcher
❯ python main.py --help
    python main.py --help
usage: python main.py "what you want to search"

pass a search string as an argument to this file to search your twitter likes

positional arguments:
  query                 substring to query

optional arguments:
  -h, --help            show this help message and exit
  --first {True,False}  Stop after the first hit(s)

```

By default this script will exit after it finds a match (or matches, it searches in bunches, read the api if you care), but if you want it to find all the tweets that match your search query, pass the flag `--first False` and it will go all the way back.
