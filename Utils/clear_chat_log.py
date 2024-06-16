import os

os.remove('chat_log.txt')

with open('chat_log.txt', 'x') as f:
    pass