import praw
import comment_clear as clearer
from rule import Rule

reddit = praw.Reddit(user_agent='Comment Cleaner',
                     client_id=CLIENTID, client_secret=CLIENTSECRET,
                     username=USERNAME, password=PASSWORD)

rules = [
Rule(max_upvotes=0) # anything with under 1 upvote
]
clearer.clear(reddit, rules, comments=True, submissions=True, new=True, controversial=True, top=True, hot=True)
