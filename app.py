import os
from openai import AzureOpenAI
import json
import tiktoken
import gradio as gr
import time


# streaming chat
# run in local or docker
# Load config values
with open('config.json') as config_file:
    config_details = json.load(config_file)

# init in config.json
model_name = config_details['CHATGPT_MODEL_HIGH']

client = AzureOpenAI(
  api_key = config_details['OPENAI_API_KEY'],
  api_version = "2023-05-15",
  azure_endpoint = config_details['OPENAI_API_BASE']
)


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    response = client.chat.completions.create(
        model=model_name,
        messages= history_openai_format,
        temperature=1.0,
        stream=True)
    
    partial_message = ""
    for chunk in response:
        print(chunk)
        print("--------------")
        print(chunk.choices[0])
        print("--------------")
        try:
            if chunk.choices[0].delta.content is not None:
                partial_message = partial_message + chunk.choices[0].delta.content
                yield partial_message
        except:
            continue

gr.ChatInterface(predict).launch()