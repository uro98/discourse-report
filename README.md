# discourse-report

This Twitter bot collects the 100 most recent tweets mentioning a politician for 6 UK politicians every minute. Every 6 hours it tweets a report showing what percentage of the tweets were negative for each politician and whether the number increased or decreased.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Python 2.7

Download Python 2.7.

#### Tweepy

See the installation details on [Tweepy's Github](https://github.com/tweepy/tweepy/tree/v3.6.0).

#### TextBlob

See the installation details on [TextBlob's website](https://textblob.readthedocs.io/en/dev/#get-it-now).

#### Keys and Access Tokens

For a copy of the config.py file containing the Keys and Access Tokens of the Twitter app, contact one of the contributors.

## Running

Type 'python text_blob_test.py' in the terminal and press enter. A log should start appearing within a minute. If you get an error make sure you are running Python 2. If you leave the program running in the background it will start posting on Twitter within 6 hours. You can use a Screen for this.

## Built With

* [Python 2.7](https://www.python.org/downloads/release/python-2715/)
* [Tweepy](http://www.tweepy.org/) - The Python library used to access Twitter's API
* [TextBlob](https://textblob.readthedocs.io/en/dev/) - The Python library used for sentiment analysis
* [Twitter Apps](https://apps.twitter.com/) - Bot registration and configuration

## Authors

Team Power-Hardcore (Jane Ditchfield, Angus Shaw, Yiping Sun and Yu-Jo Tseng)
