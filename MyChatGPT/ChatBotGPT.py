import configparser
import time

import openai
import panel as pn  # GUI
from openai.cli import display
import openai
from prompt_toolkit import prompt, print_formatted_text, HTML
from prompt_toolkit.history import InMemoryHistory

config = configparser.ConfigParser()
config.read('dev.config.ini')

if 'OPENAI' in config:
    OPENAI_API_KEY = config['OPENAI']['OPENAI_API_KEY']
else:
    raise 'Can''t fetch the api key'

openai.api_key = OPENAI_API_KEY
model = 'gpt-3.5-turbo'


def chat_with_bot():
    print("Welcome to the Chatbot! Type 'quit' to exit.")
    print("-----------------------------")

    conversation = ""
    while True:
        user_input = input("User: ")

        if user_input.lower() == 'quit':
            break

        conversation += "User: " + user_input + "\n"
        # response = openai.Completion.create(
        #     engine='text-davinci-003',
        #     prompt=conversation,
        #     temperature=0.6,
        #     max_tokens=100,
        #     n=1,
        #     stop=None,
        #     top_p=None,
        #     frequency_penalty=None,
        #     presence_penalty=None
        # )
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=conversation,
            temperature=0.6,
            max_tokens=100,
            n=1,
            stop=None,
            top_p=None
            # frequency_penalty=None
            # presence_penalty=1
        )
        bot_response = response.choices[0].text.strip()

        conversation += "Chatbot: " + bot_response + "\n"

        # Fancy chat display
        print("-----------------------------")
        print("Chatbot: " + bot_response)
        print("-----------------------------")

        time.sleep(1)  # Add a delay to simulate a more natural conversation flow


# Call the chatbot function
chat_with_bot()


###############################################
# def chat_with_bot(prompt):
#     response = openai.Completion.create(
#         engine='text-davinci-003',  # Choose the appropriate engine for your use case
#         prompt=prompt,
#         max_tokens=50,  # Adjust the number of tokens based on your desired response length
#         n=1,
#         stop=None,
#         temperature=0.7  # Adjust the temperature for more varied or conservative responses
#     )
#     return response.choices[0].text.strip()
#
#
# prompt = 'You: Hello\nBot:'
# while True:
#     user_input = input(prompt)
#     if user_input.lower() == 'bye':
#         print('Chatbot: Goodbye!')
#         break
#     prompt += user_input + '\nBot:'
#     bot_response = chat_with_bot(prompt)
#     prompt += bot_response + '\nYou:'
#     print('Chatbot:', bot_response)

############################################
#
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,  # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]
#
#
# def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.5):
#     responses = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=temperature,  # this is the degree of randomness of the model's output
#     )
#     # print(str(response.choices[0].message))
#     return responses.choices[0].message["content"]
#
#
# # messages = [
# #     {'role': 'system', 'content': 'You are an assistant that speaks like Shakespeare.'},
# #     {'role': 'user', 'content': 'tell me a joke'},
# #     {'role': 'assistant', 'content': 'Why did the chicken cross the road'},
# #     {'role': 'user', 'content': 'I don\'t know'}
# # ]
# #
# # response = get_completion_from_messages(messages, temperature=1)
# # print(response)
#
# messages = [
#     {'role': 'system', 'content': 'You are friendly chatbot.'},
#     {'role': 'user', 'content': 'Hi, my name is Isa'},
#     {'role': 'assistant', 'content': "Hi Isa! It's nice to meet you. \
#         Is there anything I can help you with today?"},
#     {'role': 'user', 'content': 'Yes, you can remind me, What is my name?'}]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)
#
#
# def collect_messages(_):
#     prompt = inp.value_input
#     inp.value = ''
#     context.append({'role': 'user', 'content': f"{prompt}"})
#     responses = get_completion_from_messages(context)
#     context.append({'role': 'assistant', 'content': f"{responses}"})
#     panels.append(
#         pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
#     panels.append(
#         pn.Row('Assistant:', pn.pane.Markdown(responses, width=600, styles={'background-color': '#F6F6F6'})))
#
#     return pn.Column(*panels)
#
#
# pn.extension()
#
# panels = []  # collect display
#
# context = [{'role': 'system', 'content': """
# You are OrderBot, an automated service to collect orders for a pizza restaurant. \
# You first greet the customer, then collects the order, \
# and then asks if it's a pickup or delivery. \
# You wait to collect the entire order, then summarize it and check for a final \
# time if the customer wants to add anything else. \
# If it's a delivery, you ask for an address. \
# Finally you collect the payment.\
# Make sure to clarify all options, extras and sizes to uniquely \
# identify the item from the menu.\
# You respond in a short, very conversational friendly style. \
# The menu includes \
# pepperoni pizza  12.95, 10.00, 7.00 \
# cheese pizza   10.95, 9.25, 6.50 \
# eggplant pizza   11.95, 9.75, 6.75 \
# fries 4.50, 3.50 \
# greek salad 7.25 \
# Toppings: \
# extra cheese 2.00, \
# mushrooms 1.50 \
# sausage 3.00 \
# canadian bacon 3.50 \
# AI sauce 1.50 \
# peppers 1.00 \
# Drinks: \
# coke 3.00, 2.00, 1.00 \
# sprite 3.00, 2.00, 1.00 \
# bottled water 5.00 \
# """}]  # accumulate messages
#
# inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
# button_conversation = pn.widgets.Button(name="Chat!")
#
# interactive_conversation = pn.bind(collect_messages, button_conversation)
#
# dashboard = pn.Column(
#     inp,
#     pn.Row(button_conversation),
#     pn.panel(interactive_conversation, loading_indicator=True, height=300),
# )
#
# display(dashboard)

# messages = context.copy()
# messages.append(
#     {'role': 'system', 'content': 'create a json summary of the previous food order. Itemize the price for each item\ '
#                                   'The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, '
#                                   'include size   4) list of sides include size  5)total price '},
# )

# The fields should be 1) pizza, price 2) list of toppings 3) list of drinks, include size include price  4) list of
# sides include size include price, 5)total price '},

# response = get_completion_from_messages(messages, temperature=0)
# print(response)
