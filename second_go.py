import oauth2 as oauth
import httplib2
import time, os, simplejson

from secrets import secret

# Fill the keys and secrets you retrieved after registering your app
consumer_key      =   secret['API_KEY']
consumer_secret  =   secret['Secret_Key']
user_token           =   secret['OAUT']
user_secret          =   secret['OAUS']

# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)

# Use the consumer object to initialize the client object
client = oauth.Client(consumer)

# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
                key=user_token,
                secret=user_secret)

client = oauth.Client(consumer, access_token)

# Make call to LinkedIn to retrieve your own profile
resp,content = client.request("http://api.linkedin.com/v1/people/~", "GET", "")

# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
# resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")
