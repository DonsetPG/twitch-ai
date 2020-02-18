import twitch
import json
from datetime import datetime
# Username of your channel
username = 'Test_Bot_AI'
# oauth to get on twitch.com
password = 'oauth:7dzsorwdktwht4ks6bhdbcehy1r20l'
# channels to scrap
channels = 'domingo'
# Name to response 
to_answser = ''


chat_live = twitch.Chat(channel=channels, nickname=username, oauth=password)

def send_response(message):
    if message.sender == to_answser:
        chat_live.irc.send_message(message='Salut Theops', channel=chat_live.channel)

chat_live.subscribe(
            lambda message: send_response(message)
            )

