import tweepy
import time

auth = tweepy.OAuthHandler('8jDwJZkvlpWWUUt1EOxzcZafo',
                           'iK14IzBz0LMb6ImsOurkgJufqnO1LuAZ18Zfsupc22JdKlQfPS')
auth.set_access_token('1145579421853597696-0eevf4fmLjaixp9k5qdu0IOMPN03m7',
                      'OAuRVJeeUGnQreVk5eN1Ym9TybcONSEgmoAyQp04OwZBJ')

api = tweepy.API(auth)
user = api.me()

# user info
print(f"User Name : {user.name}")
print(f"Screen Name : {user.screen_name}")
print(f"Followers : {user.followers_count}")


def limit_handler(cursor):
    print("Follower Names :")
    try:
        while True:
            yield cursor.next()
    except:
        time.sleep(2)


def print_followers():
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        print(f"{follower.name},  {follower.screen_name}")


def like_tweets():
    key = str(input("Enter the key to search: "))
    num = int(input("Enter the number of tweets to like: "))

    for tweet in tweepy.Cursor(api.search, key).items(num):
        try:
            tweet.favorite()
            print('i liked a tweet')
        except tweepy.TweepError as e:
            print(f"An error occured {e}")
        except StopIteration:
            break


print_followers()
like_tweets()
