# import pyttsx3 
# #the script starts by importing the pyttsx3 library.

# def robo_spe():
#     engine = pyttsx3.init()   # pyttsx3.init function initializes the text-to-speech engine.
#     t_t_s = input("Enter a text: ")
#     engine.setProperty('rate', 150)
#     engine.setProperty('volume', 1.0)
#     engine.say(t_t_s)  # engine.say(t_t_s) function queues the enterd text to be spoken.
#     engine.runAndWait() # engine.runAndWait process the command and performs the speech synthesis.
# if __name__ == "__main__":
#     robo_spe() 



import pyttsx3


def set_voice(engine, voice_type="male"):
    voices = engine.getProperty('voices')
    if voice_type.lower() == "female":
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

def robo_spe():
    engine = pyttsx3.init()
    set_voice(engine, "female")  # Change to "male" for a male voice
    while True:
        t_t_s = input("Enter a text (or type 'exit' to quit): ")
        if t_t_s.lower() == "exit":
            break
        engine.say(t_t_s)
        engine.runAndWait()

if __name__ == "__main__":
    try:
        robo_spe()
    except Exception as e:
        print(f"An error occurred: {e}")