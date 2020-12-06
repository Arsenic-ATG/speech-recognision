import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()





# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google
try:
    speak('you said " ' + r.recognize_google(audio) + ' "')
    print('you said " ' + r.recognize_google(audio) + ' "')
except sr.UnknownValueError:
    speak("Google could not understand audio")
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Google error; {0}".format(e))