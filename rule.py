import praw
from datetime import datetime

class Rule():

    def __init__(self, type="", min_upvotes=None, max_upvotes=None,
                 min_age=None, max_age=None, subreddit=None):
        self.type = type
        self.min_upvotes = min_upvotes
        self.max_upvotes = max_upvotes
        self.min_age = min_age
        self.max_age = max_age
        self.subreddit = subreddit

    def is_true(self, item):
        if type(item) == praw.models.Comment and self.type == "submission":
            return False
        if type(item) == praw.models.Submission and self.type == "comment":
            return False

        age = datetime.utcnow() - datetime.utcfromtimestamp(item.created_utc)
        age_hours = age.seconds / 60 / 60 + age.days * 24

        if self.min_age is not None and age.days > self.min_age:
            return False
        elif self.max_age is not None and age.days < self.max_age:
            return False

        if self.max_upvotes is not None and item.score > self.max_upvotes:
            return False
        elif self.min_upvotes is not None and item.score < self.min_upvotes:
            return False

        elif self.subreddit is not None and str(item.subreddit).lower() != self.subreddit.lower():
            return False

        return True