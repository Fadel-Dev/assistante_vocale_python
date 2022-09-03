import datetime

import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit as pf
listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty("voices")
engine.setProperty('voice','french')


try:
    with sr.Microphone() as source:
        print("parlez maintenant")
        voix = listener.listen(source)
        command=listener.recognize_google(voix,language='fr-Fr')
        print(command)
        #engine.say(command)
        if 'chansons de' in command:
            chanteur=command.replace('chansons de','')
            print(chanteur)
            engine.say(chanteur)
            pf.playonyt(chanteur)
        elif 'assistante' in command:
            engine.say('bonjour')
            engine.say('a qui ai je lhonneur')
        elif'quelle heure est-il'in command:
            heure=datetime.datetime()
            engine.say(heure)
        elif 'qui est ton maître' in command:
            maitre = 'Ah tu a oubliai cest toi fadel!     ,cher roboticien'
            print(maitre)
            engine.say(maitre)
            engine.runAndWait()
except:
    pass
