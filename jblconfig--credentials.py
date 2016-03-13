
'''USER CONFIGURATION'''

#Used to store all the proper credentials.  Remove the --credentials from filename to use.

import praw

#Fill in values as per https://www.reddit.com/comments/3cm1p8/how_to_make_your_bot_use_oauth2/

APP_ID = ""
#App Id below Reddit App username

APP_SECRET = ""
#Secret Key below App ID

APP_URI = ""
#Probably a local link 

APP_REFRESH = ""
#App Refresh Token

APP_SCOPES = "account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread"
#Just gave you everything

USERAGENT = ""
#This is a short description of what the bot does. For example "/u/GoldenSights' Newsletter bot"

APP_ACCOUNT_CODE = ""
#App Account Code

def login():
    r = praw.Reddit(USERAGENT)
    r.set_oauth_app_info(APP_ID,APP_SECRET,APP_URI)
    r.refresh_access_information(APP_REFRESH)
    return r
#allows for easy import of credentials into the main bot file
