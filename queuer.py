# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from random import randrange
from openai import OpenAI
import json
import os
# Written in Python 3.11.2


def chatGPT(prompt, randSentance_context = ""):
    response = OpenAI().chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {
             "role": "system",
             "content": randSentance_context + CONFIG['context']
            },

            {
             "role": "user",
             "content": prompt
            }
        ],
        temperature = 0,
        max_tokens = 1000,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    load_dotenv()
    CONFIG = json.load(open('config.json', 'r'))
    QUESTIONS = open('questions.txt', 'r').readlines()
    i = 1;


    for linia in QUESTIONS:
        question = linia.strip()

        if question == "":
            continue

        randSentance = randrange(int( CONFIG['min_questions'] ), int( CONFIG['max_questions'] ) + 1)
        response = chatGPT(question, f"Response in {randSentance} sentences. ")

        print(question + "\n" + response + "\n")
        with open(f"./answers/{i} {question[:40]}.txt", 'w') as answer:
            answer.write(response)
        
        i += 1