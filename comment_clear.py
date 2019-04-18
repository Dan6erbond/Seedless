import praw
from datetime import datetime

def clear(reddit, rules, submissions=False, comments=False, new=False, controversial=False, hot=False, top=False):
    items = set()

    if comments:
        if new:
            items.update(reddit.user.me().comments.new(limit=None))
        if controversial:
            items.update(reddit.user.me().comments.controversial(limit=None))
        if hot:
            items.update(reddit.user.me().comments.hot(limit=None))
        if top:
            items.update(reddit.user.me().comments.top(limit=None))

    if submissions:
        if new:
            items.update(reddit.user.me().submissions.new(limit=None))
        if controversial:
            items.update(reddit.user.me().submissions.controversial(limit=None))
        if hot:
            items.update(reddit.user.me().submissions.hot(limit=None))
        if top:
            items.update(reddit.user.me().submissions.top(limit=None))

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
