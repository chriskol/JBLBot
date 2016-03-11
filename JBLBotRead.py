#!/usr/bin/python
import praw

user_agent = ("JBLBot 0.1")

r = praw.Reddit(user_agent = JBLBot 0.1)

subreddit = r.get_subreddit("squaredcircle")

for submission in subreddit.get_hot(limit = 5):
    print "Title: ", submission.title
    print "Text: ", submission.selftext
    print "Score: ", submission.score
    print "---------------------------------\n"
    print "Comment: ", submission.Comment
    print "---------------------------------\n"
