# Seedless
A simple script to remove Reddit submissions/comments that meet given criteria.

Unlike similar setups, Seedless not only removes a post, but also edits the contents to "[removed by user]" as well as allows to setup rules which means not all posts will be removed if you don't need that.

## Usage
The [seedless.py](seedless.py) is the main file which contains the `clear()` function. Calling `clear()` will have the script clear all the posts meeting the given criteria and log the actions as it goes. It takes the arguments `reddit`, `rules`, `submissions`, `comments`, `new`, `controversial`, `hot`, `top` and `remove`. The key ones are...

`reddit`: This is where you feed your Reddit instance with which it will find your posts and remove them.
`submissions`: If you only want to have comments removed, this can be set to `False` to improve performance.
`comments`: Just like with the submissions this can be set to `False` to improve performance if comments do not need to be scanned.
`remove`: If you only want the posts returned, not removed, set this to `False`.

The examples' default rules remove all NSFW content (submissions as well as comments in NSFW submissions) but rules can be heavily configured. To get your ClientID as well as Client-Secret, you will need to visit the [preference page](https://www.reddit.com/prefs/apps) on Reddit and create a script. The redirect URL can be set to https://127.0.0.1.

### Direct removal
Clone the latest version of this repository to your local system and follow the [example.py](example.py) file to have your posts removed directly from Reddit:

```python
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
```

### Removal after confirmation
Unlike the previous example, this example sets `remove` to `False` and asks the user if a post should be removed. Entering anything containing an "n" will not remove it, otherwise it will be removed.

```python
### Author: Dan6erbond ###
###  Date: 10.04.2019  ###
###    Version: 1.2    ###
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

for item in seedless.clear(reddit, rules, remove=False):
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
```

### Rules
The rule class allows for very customizable critera that a comment/submission (or both) need to meet before they're removed. Setting up a new rule acts as a or-statement and the criteria within a rule as an and-statement as a post will only removed if it meets **all** the given criteria of a ***singular*** rule. Rules have the following fields which can be setup:

`type`: [string] Can be left empty and represents whether a submission or comment should be removed. If empty it removes all and otherwise should be set to "comment" or "submission".
`min_upvotes`: [int] The minimum amount of upvotes a post should have before it's removed.
`max_upvotes`: [int] The maxiumum amount of upvotes a post should have before it's removed.
`min_age`: [int] How old in days it should be at least for removal.
`max_age`: [int] How old a post should be in days at most for it to be removed.
`nsfw`: [boolean] If set to true, all posts that are NSFW or in an NSFW submission/subreddit are removed.
`subreddits`: [list-string] The subreddits in which the post needs to be present in.
`not_subreddits`: [list-string] The subreddits in which a post should not be present in for removal.

Instantiating an empty rule (`Rule()`) would remove all posts made by the user.
