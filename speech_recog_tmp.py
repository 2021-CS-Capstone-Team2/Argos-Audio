#pip install SpeechRecognition
#pip install pyaudio(안되면 pip install pipwin, pipwin install pyaudio)

import speech_recognition as sr
import time

r = sr.Recognizer()
with sr.Microphone() as source:
    print("MIC ON")
    audio = r.listen(source)

try:
    print("You said: "+r.recognize_google(audio, language="ko-KR"))
except sr.UnknownValueError:
    print("음성 정보를 인식하지 못했습니다.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}". format(e))
