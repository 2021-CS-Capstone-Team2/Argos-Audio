#pip install SpeechRecognition
#pip install pyaudio(pip install pipwin, pipwin install pyaudio)

import speech_recognition as sr
import signal, sys
import time
from datetime import datetime

path = "C:/ArgosAjou/"
filename = "audio_"

#signal (process kill)
def handler(signum, frame):
    stopper(wait_for_stop=False)
    print("프로그램이 종료됩니다.", signum)
    time.sleep(0.1)
    sys.exit()

#background thread
def callback(recognizer, audio):
    print("sound detect :")
    try:
        say = recognizer.recognize_google(audio, language='ko-KR')
        if(say):
            s = datetime.now().strftime("%Y%m%d%H%M%S")
            f = open(path+s+".txt", 'w')
            f.write(say)
            print("you said: " + say)
    except sr.UnknownValueError:
        print("Can't recognize ... it may be noise ...")
    except sr.RequestError as e :
        print("Could not request result from Google Speech Recognition service; {0}".format(e))

def main():
    #making recognizer and mic
    r = sr.Recognizer()
    m = sr.Microphone()

    #signal setting - mic terminate
    signal.signal(signal.SIGTERM, handler)

    #noise check ... this time is very important ...
    with m as source : 
        r.adjust_for_ambient_noise(source)
        print("ambient noise check OK")

    stopper = r.listen_in_background(m, callback)

    print("Background mic ON ...")
    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    main()
