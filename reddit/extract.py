import praw

# Primary Account Details
client_id = ""
client_secret = ""
user_agent = ""
username = ""
password = ""

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

subslist = []

for subreddit in reddit.user.subreddits(limit=None):
    # print(str(subreddit))
    subslist.append(str(subreddit))

with open("subs.txt", "w") as f:
    for item in subslist:
        f.write(item + "\n")
