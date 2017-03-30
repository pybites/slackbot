import sys

from starterbot import parse_slack_output

from commands.mood import get_mood
from commands.special import celebration
from commands.articles import get_num_posts
from commands.challenge import create_tweet
from commands.weather import get_weather

names = ('dog?', 'is_special', '#posts', '100days')
methods = (get_mood, celebration, get_num_posts, create_tweet)
COMMANDS = zip(names, methods)
print(get_weather())
sys.exit()
print(get_mood())
print(celebration())
print(get_num_posts())
print(create_tweet())
def handle_command(cmd, channel):
    if cmd in commands:
        response = commands[cmd]
    else:
        response = 'Not sure what you mean. I can answer these: {}'.format(commands)

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
