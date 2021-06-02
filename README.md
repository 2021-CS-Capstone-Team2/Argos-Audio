# Argos-Audio


해당 코드는 Argos Project의 Audio Detecting 관련 코드입니다.

<h2>speech_recog_tmp.py</h2>
Python의 SpeechRecognition API를 사용하였으며,

음성 파일(.wav) 또는 마이크 원하는 방식으로 인자를 전달받아 음성을 인식합니다.

테스트 용으로 사용하시면 좋습니다.


<h2>speech_recog.py</h2>
**use in Argos Program**

Python의 SpeechRecognition API를 사용하였으며,

음성을 인식하기 위한 마이크가 별도의 thread를 만들어 background에서 동작합니다.

해당 thread에서 음성이 감지되었을 경우 callback에 있는 내용이 동작합니다.


*handler()의 경우 signal을 처리하고 싶을 때 사용하시면 됩니다. Argos 프로젝트에서는 사용하지 않았습니다.*





<h3>참고 링크</h3>
1. https://pypi.org/project/SpeechRecognition/
