from pprint import pprint
import praw

reddit = praw.Reddit('bot')

pprint(reddit.get('/r/allthingsprotoss/wiki/config/automoderator'))
