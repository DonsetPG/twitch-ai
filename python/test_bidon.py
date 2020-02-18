import twitch
import json 
# Username of your channel
username = 'Test_Bot_AI'
# oauth to get on twitch.com
password = 'oauth:x'
# channels to scrap
channels = 'solary'
# Name to give to the json file s
name_chat = channels +'_chat.json'

def open_live_tchat(number_of_message,chat_name):
    """Function that open the chat of a channel and saves the senders and messages.
    Arg:
        number_of_message: Number of message you want to save.
        chat_name: Name of the .json file where you want to save the messages
    """
    chat = {
        'Senders':[],
        'Messages':[]
    }

    def _add_to_chat(message):
        """Function that print a message, and save it inside a dict.
        """

        print('{} -> {}'.format(message.sender,message.text))
        chat['Senders'].append(message.sender)
        chat['Messages'].append(message.text)

        if len(chat['Messages']) > number_of_message:
            with open(name_chat, 'w') as fp:
                print('Saving chat...')
                json.dump(chat, fp)
                print('Chat saved in {}'.format(name_chat))
                return

    twitch.Chat(channel=channels, nickname=username, oauth=password).subscribe(
            lambda message: _add_to_chat(message))


open_live_tchat(number_of_message=100,chat_name=name_chat)


