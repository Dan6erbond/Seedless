import praw
from datetime import datetime

class Rule():

    def __init__(self, type="", min_upvotes=None, max_upvotes=None,
                 min_age=None, max_age=None, nsfw=False,
                 subreddits=None, not_subreddits=None):
        self.type = type
        self.min_upvotes = min_upvotes
        self.max_upvotes = max_upvotes
        self.min_age = min_age
        self.max_age = max_age
        self.subreddits = [sub.lower() for sub in subreddits] if subreddits is not None else None
        self.not_subreddits = [sub.lower() for sub in not_subreddits] if not_subreddits is not None else None
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

        if self.subreddits is not None and str(item.subreddit).lower() not in self.subreddits:
            return False
        if self.not_subreddits is not None and str(item.subreddit).lower() in self.not_subreddits:
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
            attrs.append("min_upvotes={}".format(self.min_upvotes))

        if self.max_upvotes is not None:
            attrs.append("max_upvotes={}".format(self.max_upvotes))

        if self.subreddits is not None:
            attrs.append("subreddits={}".format(self.subreddits))

        if self.not_subreddits is not None:
            attrs.append("not_subreddits={}".format(self.not_subreddits))

        if self.nsfw:
            attrs.append("NSFW")

        return " | ".join(attrs)
