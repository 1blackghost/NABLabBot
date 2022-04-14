#ashdev

import pytchat
import pyttsx3
#passing the video id: https://youtube.con/v=<id> %&* are all excluded.
VIDEO_ID="nm5kz7tuH4s"

#initialising pychat
chat = pytchat.create(video_id=VIDEO_ID)

#text-speech engine pyttsx3
def speak(s):
    engine=pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(str(s))
    engine.runAndWait()
#response function
def give_response(person,reply):
    speak(str(person)+str(message))

#main-loop
while chat.is_alive():
    for c in chat.get().sync_items():
        #getting-values
        message=str(c.message)
        person=str(c.author.name)
        #displays the live comments
        print(f"{c.datetime} [{person}]- {message}")
        for i in message:
            if "hey" in message:
                give_response(person,"Nice to Meet you!")
            if "fuck" in message:
                give_response(str("dont use those kind of words, respect our community guidelines"),str(p))
            if "how are you" in message:
                give_response(str("fine thank you"),str(p))    