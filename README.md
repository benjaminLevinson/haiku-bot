# haiku-bot
Twitter bot that generates and tweets haikus

## Installation
Run:
```
make init
source venv/bin/activate
make install
```

Add a `keys.env` file with your Twitter developer access keys:
```
export HAIKU_CONSUMER_KEY=[key here]
export HAIKU_CONSUMER_SECRET=[key here]
export HAIKU_ACCESS_TOKEN_KEY=[key here]
export HAIKU_ACCESS_TOKEN_SECRET=[key here]
export WORDBANK_PATH=[path here]
```

[Download the word bank](http://www.ashley-bovan.co.uk/words/partsofspeech.html)
and add the path to the WORDBANK_PATH variable.

Run `./tweet.sh` and the bot will generate and post a Tweet.