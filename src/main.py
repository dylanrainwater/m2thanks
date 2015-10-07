import praw
import time
from random import randint

user_agent = "Me too thanks account for r/me_irl v1.0 (by u/Chemical_Studios)"

site_name = "m2thanks"

r = praw.Reddit(user_agent=user_agent, site_name=site_name)

r.login()

user = r.get_redditor('m2thanks')

already_done = []

subreddit = r.get_subreddit('me_irl')

motto = "me too thanks"

count = 0

while True:
    print "I'm awake! ", motto
    # get top 10 from r/me_irl
    for submission in subreddit.get_hot(limit=10):
        # make sure i haven't posted there yet
        if not (submission in already_done):
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            if (randint(0, 9) <= 2) or (len(flat_comments) == 0): # add parent comment
                submission.add_comment(motto)
                # wait 10 minutes in between comments
                time.sleep(600)
            else:
                comment_to_reply_to = flat_comments[randint(0, len(flat_comments) - 1)]
                comment_to_reply_to.reply(motto)
                # wait 10 minutes in between comments
                time.sleep(600)
            already_done.append(submission)
            count = count + 1

    print "Finished cycle... going to sleep."
    r.send_message('Chemical_Studios', 'Write-Up', count)
    # sleep for 8 hours 
    time.sleep(28800)
