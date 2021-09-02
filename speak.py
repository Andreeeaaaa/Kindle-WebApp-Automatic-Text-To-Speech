from gtts import gTTS
import os
import pydub
import simpleaudio as sa

import settings

def text_to_mp3(text:str):
    languange = settings.get_language()[0: -1]
    speech = gTTS(text=text, lang=languange, slow=False)
    speech.save(settings.WORKSPACE_DIR + '/speech_temp/speech.mp3')

def mp3_to_wav():
    src = settings.WORKSPACE_DIR + '/speech_temp/speech.mp3'
    dst = settings.WORKSPACE_DIR + '/speech_temp/speech.wav'
    sound = pydub.AudioSegment.from_mp3(src)
    sound.export(dst, format='wav')

def speak():
    filename = settings.WORKSPACE_DIR + '/speech_temp/speech.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    return play_obj