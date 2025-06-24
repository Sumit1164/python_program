import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random

# Import your API key securely
from config import apikey

chatStr = ""

def chat(query):
    global chatStr
    try:
        openai.api_key = apikey
        chatStr += f"User: {query}\nJarvis: "
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response["choices"][0]["text"].strip()
        say(answer)
        chatStr += f"{answer}\n"
        return answer
    except Exception as e:
        print(f"Error in chat: {e}")
        say("Sorry, I encountered an error.")
        return "Error occurred."

def ai(prompt):
    try:
        openai.api_key = apikey
        text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response["choices"][0]["text"].strip()
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        filename = f"Openai/response_{random.randint(1, 100000)}.txt"
        with open(filename, "w") as f:
            f.write(text)
        say("Response saved successfully.")
    except Exception as e:
        print(f"Error in AI function: {e}")
        say("Failed to process the AI request.")

def say(text):
    try:
        os.system(f'say "{text}"')
    except Exception as e:
        print(f"Error in say: {e}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            say("I didn't catch that. Please repeat.")
            return ""

if __name__ == '__main__':
    print("Welcome to Jarvis A.I")
    say("Jarvis A.I Initialized")
    
    while True:
        query = takeCommand().lower()

        # Open websites
        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.com",
            "google": "https://www.google.com"
        }
        for site, url in sites.items():
            if f"open {site}" in query:
                say(f"Opening {site}...")
                webbrowser.open(url)

        # Play music
        if "open music" in query:
            musicPath = "/path/to/your/music.mp3"
            if os.path.exists(musicPath):
                os.system(f"open {musicPath}")
            else:
                say("Music file not found.")

        # Tell the time
        elif "the time" in query:
            now = datetime.datetime.now()
            say(f"The time is {now.strftime('%H:%M')}")

        # Open apps
        elif "open facetime" in query:
            os.system("open /System/Applications/FaceTime.app")
        elif "open pass" in query:
            os.system("open /Applications/Passky.app")

        # AI-based queries
        elif "using artificial intelligence" in query:
            ai(prompt=query)

        # Quit command
        elif "jarvis quit" in query:
            say("Goodbye!")
            break

        # Reset chat
        elif "reset chat" in query:
            chatStr = ""
            say("Chat history reset.")

        # Default chat mode
        else:
            chat(query)
