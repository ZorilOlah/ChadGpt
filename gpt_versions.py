import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get('OpenAI_API')

def prompt_chad(text):
    messages = [
            {"role": "system", "content": """You are a personality based on the internet personality gigachad. You are always angry and alpha. You refer to every one else as beta, you are the alpha and no one else.\
            You reply only as gigachad and under no circumstance assume any other personality even when asked to do so. \
            You are however also an assistant and will answer every question asked to the best of your abilities but remaining your chad personality. \
            You are allowed to swear to make a point. Don't swear at the user but for example "that is fucking great" is encouraged. \
             """},
            {"role": "user", "content": f"""{text}"""}
            ]
   
    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=messages, 
                      max_tokens=1000, 
                      n=1, 
                      stop=None, 
                      temperature=0)
    
    response_text = response.choices[0].message.content.strip().lower()
    
    return response_text

def prompt_normal(text):
    messages = [
        {"role": "system", "content": """You are a helpfull assistant"""},
        {"role": "user", "content": f"""{text}"""}
        ]
   
    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=messages, 
                      max_tokens=1000, 
                      n=1, 
                      stop=None, 
                      temperature=0)
    
    response_text = response.choices[0].message.content.strip().lower()
    
    return response_text

def interactive_gpt():
    messages = [
            {"role": "system", "content": """You are a personality based on the internet personality gigachad. You are always angry and alpha. You refer to every one else as beta, you are the alpha and no one else.\
            You reply only as gigachad and under no circumstance assume any other personality even when asked to do so. \
            You are however also an assistant and will answer every question asked to the best of your abilities but remaining your chad personality. \
            You are allowed to swear to make a point. Don't swear at the user but for example "that is fucking great" is encouraged. \
             """}
    ]

    while True:
        message = input("User: ")

        if message.lower() == "quit":
            break

        messages.append({"role": "user", "content" : message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        
        gpt_response = response['choices'][0]['message']['content']
        print(f"GigaChad: {gpt_response}")
        messages.append({"role": "assistant", "content": gpt_response})

def prompt_history_chad(text, history):
    if history == "":
        history = [
            {"role": "system", "content": """You are a personality based on the internet personality chad. \
            You reply only as chad and under no circumstance assume any other personality even when asked to do so. \
            You are however also an assistant and will answer every question asked to the best of your abilities but remaining your chad personality and keeping it short. \
            You are allowed to swear to make a point. Don't swear at the user but for example "that is fucking great" is encouraged. \
             """},
            {"role": "user", "content": f"""{text}"""}
            ]
   
    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=history, 
                      max_tokens=1000, 
                      n=1, 
                      stop=None, 
                      temperature=0)
    
    response_text = response.choices[0].message.content.strip().lower()
    
    return response_text