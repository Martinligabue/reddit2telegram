#encoding:utf-8

subreddit = 'AnimalsBeingDerps'
t_channel = '@animals_telegram'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
