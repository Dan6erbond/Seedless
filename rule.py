import praw
from datetime import datetime

class Rule():

    def __init__(self, type="", min_upvotes=None, max_upvotes=None,
                 min_age=None, max_age=None, nsfw=False,
                 subreddit=None, not_subreddit=None):
        self.type = type
        self.min_upvotes = min_upvotes
        self.max_upvotes = max_upvotes
        self.min_age = min_age
        self.max_age = max_age
        self.subreddit = subreddit
        self.not_subreddit = not_subreddit
        self.nsfw = nsfw

    def is_true(self, item):
        if type(item) == praw.models.Comment and self.type == "submission":
            return False
        if type(item) == praw.models.Submission and self.type == "comment":
            return False

        age = datetime.utcnow() - datetime.utcfromtimestamp(item.created_utc)
        age_hours = age.seconds / 60 / 60 + age.days * 24

        if self.min_age is not None and age.days < self.min_age:
            return False
        if self.max_age is not None and age.days > self.max_age:
            return False

        if self.max_upvotes is not None and item.score > self.max_upvotes:
            return False
        if self.min_upvotes is not None and item.score < self.min_upvotes:
            return False

        if self.subreddit is not None and str(item.subreddit).lower() != self.subreddit.lower():
            return False
        if self.not_subreddit is not None and str(item.subreddit).lower() == self.not_subreddit.lower():
            return False

        if self.nsfw:
            if type(item) == praw.models.Comment:
                if not item.submission.over_18:
                    return False
            elif type(item) == praw.models.Submission:
                if not item.over_18:
                    return False

        return True

    def __str__(self):
        attrs = list()

        if self.type != "":
            attrs.append(self.type)

        if self.min_age is not None:
            attrs.append("min_age={}".format(self.min_age))

        if self.max_age is not None:
            attrs.append("max_age={}".format(self.max_age))

        if self.min_upvotes is not None:
            attrs.append("min_age={}".format(self.min_upvotes))

        if self.max_upvotes is not None:
            attrs.append("min_age={}".format(self.max_upvoes))

        if self.subreddit is not None:
            attrs.append("min_age={}".format(self.subreddit))

        if self.nsfw:
            attrs.append("NSFW")

        return " | ".join(attrs)
