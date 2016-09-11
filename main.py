import time
import praw
pr = praw.Reddit(user_agent='Birmingham apartment hunter notifier by /u/NotFlameRetardant')
pr.login()
keywords = ['apartment', 'apartments', 'hunting', 'looking for apartment', 'searching', 'rent', 'lease', '2br', '1br', '3br', '4br', '1ba', '2ba', 'studio']
sub = pr.get_subreddit('Birmingham')
already_done = []

while True:
    for submission in sub.get_hot(limit=10):
        title = submission.title.lower()
        body = submission.selftext.lower()
        positive_title = any(string in title for string in keywords)
        positive_body = any(string in body for string in keywords)

        if submission.id not in already_done and (positive_title or positive_body):
            msg = '[Potential apartment lead found here](%s)' % submission.short_link
            pr.send_message('USERNAME', 'Apartment lead', msg) # Replace with username to send to
            already_done.append(submission.id)

    time.sleep(300)
