import openai
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def create_chat(messages):
    """

    Parameters
    ----------
    messages: list of message element
        [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Who won the world series in 2020?"},
          {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
          {"role": "user", "content": "Where was it played?"}
        ]
    """
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    return completion
