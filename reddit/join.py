import praw

# Secondary Account Details
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

# Read from subs.txt
subslist = []
with open("subs.txt", "r") as f:
    for line in f:
        subslist.append(line.strip())

# Join one by one and write a log to joined.txt
with open("joinedlogs.txt", "w") as f:
    for sub in subslist:
        try:
            reddit.subreddit(sub).subscribe()
            f.write("Joined " + sub + "\n")
            print("Joined " + sub)
        except Exception as e:
            f.write("Failed to join " + sub + "\n")
            print("Failed to join " + sub + "due to the error :" + e)

print("Done")
