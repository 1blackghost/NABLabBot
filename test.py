#ashdev
import wikipedia
import pytchat
import pyttsx3
#passing the video id: https://youtube.con/v=<id> %&* are all excluded.
VIDEO_ID="zPO_P51jcK8"

#initialising pychat
chat = pytchat.create(video_id=VIDEO_ID)

#text-speech engine pyttsx3
def speak(s):
    engine=pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(str(s))
    engine.runAndWait()
#response function
def give_response(person,reply):
    speak(str(person)+str(reply))

#main-loop
while chat.is_alive():
    for c in chat.get().sync_items():
        #getting-values
        message=str(c.message)
        person=str(c.author.name)
        #displays the live comments
        print(f"{c.datetime} [{person}]- {message}")
        replied=False
        for i in message:
            if "hey" in message:
                give_response(person,"Nice to Meet you!")
                replied=True
            if "fuck" in message:
                give_response(str("dont use those kind of words, respect our community guidelines"),str(person))
                replied=True
            if "how are you" in message:
                give_response(str("fine thank you"),str(person))  
                replied=True  
            if ("creator" or "creation" or "purpose") in message:
                give_response(str("nab lab created me for their systems management"),person)
                replied=True
            if ("thanks" or "thankyou" or"thank") in message:
                give_response(str("Most welcome"),person)
                replied=True
            else:
                try:
                    speak(wikipedia.summary(str(message),sentences=1))
                except Exception as e:
                    print("Exception",str(e))
                    speak(person,"I dont have the answer in my database! teach me,Use the question and then the answer seperated by the word means ")
                replied=True
            if replied:
                break
