#Credit https://www.youtube.com/watch?v=3Mga7_8bYpw&t=505s
#using vox for basic speech recognition

from vosk import Model, KaldiRecognizer

import pyaudio

model = Model(r"/Users/haydenfriedman/Downloads/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text[14:-3])
