#pip install SpeechRecognition
#pip install pyaudio(안되면 pip install pipwin, pipwin install pyaudio)

import speech_recognition as sr
import signal, sys
import time
from datetime import datetime

#SIGINT가 아닐 때 종료하는 법은 어떻게 할까 ...

path = ""

#signal (process kill)
def handler(signum, frame):
    stopper(wait_for_stop=False)
    print("프로그램이 종료됩니다.", signum)
    time.sleep(0.1)
    sys.exit()

#background thread
def callback(recognizer, audio):
    print("HEY! :")
    try:
        s = datetime.now().strftime("%Y%m%d%H%M")
        f = open(path+s+".txt", 'a')
        say = recognizer.recognize_google(audio, language='ko-KR')
        f.write(say+"\n")
        print("you said: " + say)
    except sr.UnknownValueError:
        print("음성을 감지하지 못했습니다.")
    except sr.RequestError as e :
        print("Could not request result from Google Speech Recognition service; {0}".format(e))

def main():
    #making recognizer and mic
    r = sr.Recognizer()
    m = sr.Microphone()

    #signal setting
    signal.signal(signal.SIGTERM, handler)

    with m as source : #주변 소음 판단
        r.adjust_for_ambient_noise(source)
        print("ambient noise check OK")

    stopper = r.listen_in_background(m, callback)

    print("백그라운드 마이크 실행: ")
    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    main()
