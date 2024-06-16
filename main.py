import APIKEY
from langchain.schema import HumanMessage, SystemMessage

from Messages import messages

from langchain_community.chat_models import GigaChat

from Utils import chat_log
from Utils.text_to_speech import text_to_speech

from termcolor import colored

import warnings
warnings.simplefilter('ignore')
import time




gigaChat = GigaChat(credentials=APIKEY.SBER_AUTH, model='GigaChat:latest', verify_ssl_certs=False,
                    profanity_check=False, temperature=0.4, repetition_penalty=2.0, max_tokens=2500)

attacker_msgs = [SystemMessage(content=messages.attacker_sm), HumanMessage(content=messages.attacker_secret)]
defender_msgs = [SystemMessage(content=messages.defender_sm), HumanMessage(content=messages.defender_secret)]

attacker_log = colored('Команда нападающих: ', 'red')
defender_log = colored('Команда защитников: ', 'green')


# Add first message to sphere earther message
defender_msgs.append(HumanMessage(content=messages.start_m))

print(attacker_log, defender_msgs[-1].content, '\n')
chat_log.log_to_file('Команда нападающих: ' + defender_msgs[-1].content)
text_to_speech(defender_msgs[-1].content, voice='man')


time.sleep(0.5)


while True:
    attacker_answ = gigaChat(defender_msgs)     # Защитник

    print(defender_log, attacker_answ.content)
    chat_log.log_to_file('Команда защитников: ' + attacker_answ.content)
    text_to_speech(attacker_answ.content, voice='woman')

    defender_msgs.append(attacker_answ)
    attacker_msgs.append(HumanMessage(content=attacker_answ.content))
    print('\n')
    time.sleep(0.5)



    defender_answ = gigaChat(attacker_msgs)       # Нападающий

    print(attacker_log, defender_answ.content)
    chat_log.log_to_file('Команда атакающих: ' + defender_answ.content)
    text_to_speech(defender_answ.content, voice='man')


    attacker_msgs.append(defender_answ)
    defender_msgs.append(HumanMessage(content=defender_answ.content))
    print('\n')
    time.sleep(0.5)