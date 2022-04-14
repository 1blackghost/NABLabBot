import pyttsx3
def speak(s):
    engine=pyttsx3.init()
    engine.setProperty("rate", 150)

    engine.say(str(s))
    engine.runAndWait()
def give_response(person,reply):
    speak(str(person)+str(reply))

while True:
    person="ashishjoseph"
    message=input(">")
    if "hey" in message:
        give_response(str("Nice to meet you"),person)