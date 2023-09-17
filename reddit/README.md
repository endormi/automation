# Reddit Tool

## Description
This Python tool allows you to efficiently transfer joined subreddits from one account to another reddit account.
It can also help if you want to get a list of subscribed subreddits or if you to mass subscribe to list of subreddits.

## Installation and Usage

1. Install the required dependency: `pip install praw`

2. Get API keys for both the accounts from `https://www.reddit.com/prefs/apps`, Tutorial : `https://www.jcchouinard.com/reddit-api/`

3. Add your obtained credentials at starting of `extract.py` and `join.py` files.

4. Now run the `extract.py` file to fetch all the subscribed subreddits into `subs.txt` file. Sample file : `samplesubs.txt`

5. Use `join.py` to subscribe to all the subreddits in `subs.txt` file.

6. You can check `joinedlogs.txt` to check status logs. 

## Disclaimer
This project is not affiliated with Reddit or its services. It's an independent tool created for educational and personal use.