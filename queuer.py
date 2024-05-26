# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from random import randrange
from openai import OpenAI
import os
# Written in Python 3.11.2


def chatGPT(prompt, max_zdania_context = ""):
    response = OpenAI().chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
             "role": "system",
             "content": max_zdania_context + os.getenv('CONTEXT')
            },

            {
             "role": "user",
             "content": prompt
            }
        ],
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    load_dotenv()

    PYTANIA = open('questions.txt', 'r').readlines()
    i = 1;
    
    for linia in PYTANIA:
        pytanie = linia.strip()

        if pytanie == "":
            continue

        max_zdania = randrange(int(os.getenv('MIN_QUESTIONS')), int(os.getenv('MAX_QUESTIONS')) + 1)
        odpowiedz = chatGPT(pytanie, f"Odpowiedz w {max_zdania} zdaniach. ")

        print(pytanie + "\n" + odpowiedz + "\n")
        with open(f"./answers/{i} {pytanie[:40]}.txt", 'w') as answer:
            answer.write(odpowiedz)
        
        i += 1