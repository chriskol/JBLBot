#!/usr/bin/python
import praw
import pdb
import re
import os
from jblconfig import *

# Check that the file that contains our username exists
if not os.path.isfile("jblconfig.py"):
    print "Username and pass is wrong or config file is missing"
    exit(1)

# Create the Reddit instance
user_agent = ("JBLBot 0.1")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("post_replies.txt"):
    post_replies = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("post_replies.txt", "r") as f:
        post_replies = f.read()
        post_replies = post_replies.split("\n")
        post_replies = filter(None, post_replies)

# Get the top 5 values from our subreddit
subreddit = r.get_subreddit('pythonforengineers')
for submission in subreddit.get_hot(limit=3):
    # print submission.title

    # If we haven't replied to this post before
    if submission.id not in post_replies:

        # Do a case insensitive search
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.add_comment("I LOVE IT!")
            print "Bot replying to : ", submission.title

            # Store the current id into our list
            post_replies.append(submission.id)

# Write our updated list back to the file
with open("post_replies.txt", "w") as f:
    for post_id in post_replies:
        f.write(post_id + "\n")