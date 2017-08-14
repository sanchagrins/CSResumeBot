import praw
import config
import datetime

from mongoengine import *
from resume import Resume

class Bot():
    def __init__(self):
        self.count=0

    def bot_login(self):
        r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent)
        return r

    def run_bot(self, r):
        subreddit = r.subreddit('cscareerquestions')
        for submission in subreddit.search("author:AutoModerator Resume"):
            print("Processing: " + submission.title)
            self.process_submission(submission)

    def process_submission(self, submission):
        connect('resume_test', host='localhost', port=27017)
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments:
            s = top_level_comment.body
            if "(http" in s:
                date = datetime.datetime.fromtimestamp(submission.created_utc).isoformat()
                author = top_level_comment.author
                img_url = s[s.find("(http")+1:s.find(")")]

                if author != None and img_url.startswith('http'):
                    #img_url = s[s.find("(http")+1:s.find(")")]
                    print("Writing: " + author.name + " " + img_url + " to database..."),
                    post = Resume(
                        author=author.name,
                        url=img_url,
                        post_date=date
                        )
                    post.save()
                    self.count += 1
                    print("Done!")
                    print(post.author)
                    break

resume_bot = Bot()
print(resume_bot.count)
r = resume_bot.bot_login()
resume_bot.run_bot(r)

print(str(resume_bot.count) + " records written.")
