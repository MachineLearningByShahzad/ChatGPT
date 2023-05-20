import configparser
import openai

config = configparser.ConfigParser()
config.read('dev.config.ini')

if 'OPENAI' in config:
    OPENAI_API_KEY = config['OPENAI']['OPENAI_API_KEY']
else:
    raise 'Can''t fetch the api key'

openai.api_key = OPENAI_API_KEY


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


text = """My Query fot GPT"""

print(get_completion(text))
