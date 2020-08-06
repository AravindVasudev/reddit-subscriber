import json
import sys

from praw import Reddit


_REDDIT_USER_AGENT = 'reddit subscriber agent'


def create_agent(credentials_file='credentials.json'):
  with open(credentials_file) as f:
    credentials = json.load(f)

  credentials['user_agent'] = _REDDIT_USER_AGENT
  return Reddit(**credentials)


def main(args):
  if len(args) != 2:
    raise Exception('Illegal Usage. Format: python subscriber.py <subreddit_list_file_path>')

  reddit = create_agent()

  with open(args[1]) as f:
    for subreddit in f:
      reddit.subreddit(subreddit).subscribe()


if __name__ == '__main__':
  main(sys.argv)