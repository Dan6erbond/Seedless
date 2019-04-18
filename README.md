# Seedless
A simple script to remove Reddit submissions/comments that meet given criteria.

Unlike similar setups, Seedless not only removes a post, but also edits the contents to "[removed by user]" as well as allows to setup rules which means not all posts will be removed if you don't need that.

## Usage
Fork the latest version of this repository to your local system and follow the [example.py](example.py) file to have your posts removed from Reddit:

```python
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
clearer.clear(reddit, rules, comments=True, submissions=True, new=True, controversial=True, top=True, hot=True)
```

The file's default rules removes all NSFW content (submissions as well as comments in NSFW submissions) but rules can be heavily configured. To get your ClientID as well as Client-Secret, you will need to visit the [preference page](https://www.reddit.com/prefs/apps) on Reddit and create a script. The redirect URL can be set to https://127.0.0.1.

Calling `clear()` will have the script clear all the posts meeting the given criteria and log the actions as it goes.

### Rules
The rule-class allows for very customizable critera that a comment/submission (or both) need to meet before they're removed. Setting up a new rule acts as a or-statement and the criteria within a rule as an and-statement as a post will only removed if it meets **all** the given criteria of a ***singular*** rule. Rules have the following fields which can be setup: `type`, `min_upvotes`, `max_upvotes`, `min_age`, `max_age`, `subreddit` and `nsfw`.

The `type` field is represented by a string and can be left empty if both comments and submissions should be removed, otherwise it can be set to either "comment" or "submission".

Instantiating an empty rule (`Rule()`) would remove all posts made by the user.
