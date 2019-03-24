import tweepy
import time

print("this is my twitter bot")

CONSUMER_KEY = 'Xqpf3M4z5poRH6yp17lGXgUSU'
CONSUMER_SECRET = '2RVEN70Ti4QCl0kDMptrY4AnJF6kqEOBFdSEV1aZf3rBEN8AeL'
ACCESS_KEY = '732483098336595968-hH2jZVrpjKy0WxkM6dHzyZJ5kGgCrE9'
ACCESS_SECRET = '98B9BTk2toO3qLIppsMcsPThgOSoOf9GiGZ55OGFIypYE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def save_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print('Retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended'
    )

    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)
        last_seen_id = mention.id
        save_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('reponding back...')
            api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you!!', mention.id)


while True:
    reply_to_tweets()
    time.sleep(10)

