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

for item in clearer.clear(login.get_praw(), rules, remove=False):
    if type(item) == praw.models.Submission:
        i = input("Submission in /r/{} with {} points: {}\nShould it be removed? (y/n) ".format(item.subreddit, item.score, item.title))
    elif type(item) == praw.models.Comment:
        i = input("Comment in {} with {} points: {}\nShould it be removed? (y/n) ".format(item.submission.title, item.score, item.body))

    if "n" not in i:
        print("Deleting...")
        try:
            item.edit("[removed by user]")
        except:
            pass # image/link submission
        item.delete()
