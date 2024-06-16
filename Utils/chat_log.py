def log_to_file(message):
    words = message.split()
    
    result = ''
    

    for i in range(0, len(words), 20):
        chunk = ' '.join(words[i:i+20])
        result += chunk + '\n'
    

    with open('chat_log.txt', 'a') as f:
        f.write(result + '\n')
