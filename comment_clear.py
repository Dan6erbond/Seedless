import praw
import login
from datetime import datetime
from rule import Rule

reddit = praw.Reddit(user_agent='Comment Cleaner',
                     client_id=CLIENTID, client_secret=CLIENTSECRET,
                     username=USERNAME, password=PASSWORD)

rules = [
    Rule(max_upvotes=0)$
]

items = set()

items.update(reddit.user.me().comments.new(limit=None))
items.update(reddit.user.me().comments.controversial(limit=None))
items.update(reddit.user.me().submissions.new(limit=None))
items.update(reddit.user.me().submissions.controversial(limit=None))

print("{} items found.".format(len(items)))

count = 0
time_started = datetime.now()

for item in items:
    for rule in rules:
        if rule.is_true(item):
            try:
                item.edit("[removed by user]")
            except:
                pass # image/link submission
            item.delete()
            count+=1
            print(item)
            break

print("{} items removed in {}!".format(count, datetime.now() - time_started))
