# Hello Startup Institute Team
# Thanks for checking out my code!


# Use tweepy module to access Twitter API from Python
import tweepy


# Save OAth Information
CONSUMER_KEY = 'CSwQx9t9IEhgxM84jUyfzA'
CONSUMER_SECRET = 'yVYvZaBJIuerH5nipG1zipMJDd0fNNQT4UU28v7QeM'
ACCESS_TOKEN = '2318037230-XVVmvoPLPGGeEs9P1PmxN4rlrlB1AV1xgpsPcp8'
ACCESS_TOKEN_SECRET = '1m2ezcAvxrfBuOepD24y5m8Vj77E8h294o1sT0EqP73N1'


# Create an OAuthHandler instance
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# Create API instance
api = tweepy.API(auth)

# Search for tweets that contain "monkey" and "banana"
results = api.search(q="monkey banana")


# Print resulting tweets
for result in results:
    print result.text
