import praw
import comment_clear as clearer
from rule import Rule

reddit = praw.Reddit(user_agent='Comment Cleaner',
                     client_id=CLIENTID, client_secret=CLIENTSECRET,
                     username=USERNAME, password=PASSWORD)

rules = [
Rule(max_upvotes=0) # anything with under 1 upvote
Rule(nsfw=True) # removes all NSFW
]

for item in clearer.clear(reddit, rules):
    if type(item) == praw.models.Submission:
        print("Submission in /r/{} with {} points: {}".format(item.subreddit, item.score, item.title))
    elif type(item) == praw.models.Comment:
        print("Comment in {} with {} points: {}".format(item.submission.title, item.score, item.body))
