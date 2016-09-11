import praw
pr = praw.Reddit(user_agent='Birmingham apartment hunter notifier by /u/NotFlameRetardant')
pr.login = ('username', 'password') # Replace these with creds of account to send from
keywords = ['apartment', 'apartments', 'hunting', 'looking for apartment', 'searching', 'rent', 'lease']
sub = pr.get_subreddit('birmingham')
already_done = []

while True:
    for submission in sub.get_hot(limit=10)
        title = submission.title.lower()
        body = submission.text.lower()
        positive_title = any(string in title for string in keywords)
        positive_body = any(string in body for string in keywords)

        if submission.id not in already_done and (positive_title or positive_body)
            msg = '[Potential apartment lead found here](%s) % submission.short_link
            pr.send_message('user_to_notify', 'Apartment lead', msg) # Replace with username to send to
            already_done.append(submission.id)

    sleep(900)
