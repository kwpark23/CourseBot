import random
import time

' ' 'This bot responds based on whether user asked a question or made a statement ' ' '

bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = {"question": ["you tell me!", "I don't know :("], 
             "statement": [":)", "oh wow!", "I find that extremely interesting", "why do you think that?"]}

def respond(message):
    if message.endswith("?"):
        return random.choice(responses["question"])
    return random.choice(responses["statement"])


def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    time.sleep(1.0)
    print(bot_template.format(response))



send_message("what's today's weather?")
time.sleep(1.0)
send_message("Do you need something?")
time.sleep(1.0)
send_message("I love building chatbots")
time.sleep(1.0)
send_message("I like Python!")
