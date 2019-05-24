### Author: Dan6erbond ###
###  Date: 24.05.2019  ###
###    Version: 1.1    ###
import praw
import seedless
from rule import Rule

reddit = praw.Reddit(user_agent='Seedless',
                     client_id=CLIENTID, client_secret=CLIENTSECRET,
                     username=USERNAME, password=PASSWORD)

rules = [
Rule(max_upvotes=0) # anything with under 1 upvote
Rule(nsfw=True) # removes all NSFW
]

for item in seedless.clear(reddit, rules):
    if type(item) == praw.models.Submission:
        print("Submission in /r/{} with {} points: {}".format(item.subreddit, item.score, item.title))
    elif type(item) == praw.models.Comment:
        print("Comment in {} with {} points: {}".format(item.submission.title, item.score, item.body))
