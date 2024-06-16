def log_to_file(message):
    with open('chat_log.txt', 'w') as f:
        f.write(message + '\n')