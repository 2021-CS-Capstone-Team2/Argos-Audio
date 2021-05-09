#pip install SpeechRecognition
#pip install pyaudio(안되면 pip install pipwin, pipwin install pyaudio)

import speech_recognition as sr
import time

def main():
    r = sr.Recognizer()
    typelist = ("file","mic")
    c = "mic"
    filename = "korean"
    
    if( (c in typelist) and c == "file") :
        with sr.AudioFile(filename+".wav") as source:
            audio = r.record(source)
    elif ( (c in typelist) and c == "mic") :
        with sr.Microphone() as source:
            print("WAIT ...")
            r.adjust_for_ambient_noise(source)
            print("ambient noise check OK, PLEASE TELL ME SOMETHING")
            audio = r.listen(source)

    try: #원하면 say return 하면 됨
        say = r.recognize_google(audio, language="ko-KR")
        print("You said: "+say)
    except sr.UnknownValueError:
        print("음성 정보를 인식하지 못했습니다.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}". format(e))

if __name__ == "__main__":
    main()
