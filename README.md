# Like Searcher - For Twitter

Can't be bothered to use the UI to search tweets from last year let alone 10 years ago...

This little command-line tool will search as far back as your twitter likes go for a given query (beware of rate limiting!)

## Requirements
For this you're going to need some twitter api credentials, head [here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and get your api tokens/secrets (Sometimes called consumer keys in twitter api land) and your auth tokens/secrets. These are slurped up as environment variables by the script, so be sure that they're exported in your shell. I keep a file like the one below and then `source ./env.sh` when I need to use this. Yeah I know about autoenv, no im too lazy.

``` shell
#!/bin/bash

export TWITTER_API_TOKEN="your api token"
export TWITTER_API_SECRET="your api secret"
export TWITTER_AUTH_TOKEN="your auth token"
export TWITTER_AUTH_SECRET="your auth secret"
```

After that, clone this repo and run `make install` to install the likesearch package! This also installs a command for running `likesearch <query>` from whereever you have it installed.

## Usage

``` shell
~/dev/shane/likesearcher
❯ likesearch --help
    likesearch --help
usage: likesearch "what you want to search"

pass a search string as an argument to this file to search your twitter likes

positional arguments:
  query                 substring to query

optional arguments:
  -h, --help            show this help message and exit
  --first {True,False}  Stop after the first hit(s)

```

By default this will exit after it finds a match (or matches, it searches in bunches, read the api if you care), but if you want it to find all the tweets that match your search query, pass the flag `--first False` and it will go all the way back.
