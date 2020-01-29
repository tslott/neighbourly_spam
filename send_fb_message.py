import os
import time
import getpass
from fbchat import Client
from fbchat.models import Message


def send_message(friend_uid: int = None):

    # Connect to FB client
    client = Client(
        email=os.environ['EMAIL_ADDRESS'],
        password=getpass.getpass(prompt='Password: ', stream=None)
    )

    if friend_uid is None:
        # Search for friend's uid
        persons = client.searchForUsers(input('What is the name of your friend: '))

        # Find friend's uid in list of persons
        for person in persons:
            if person.is_friend:
                friend_uid = person.uid
                break

    # Send message
    msg = 'Hejsa din klump'
    for i in range(3):
        client.send(message=Message(text=msg), thread_id=str(friend_uid))
        time.sleep(3)

    print('FB message sent')

    return True


if __name__ == '__main__':

    send_message(friend_uid=os.environ['TARGET_FB_UID'])
