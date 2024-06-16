from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os



def change_pitch(sound, octaves):
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(44100)

def text_to_speech(text, lang='ru', voice='man'):
    tts = gTTS(text=text, lang=lang)
    
    temp_file = "temp.mp3"
    tts.save(temp_file)
    
    audio = AudioSegment.from_mp3(temp_file)
    
    if voice == 'man':
        audio = audio.speedup(playback_speed=1.8)
        audio = change_pitch(audio, -0.4)
    
    elif voice == 'woman':
        audio = audio.speedup(playback_speed=1.4)
        audio = change_pitch(audio, 0.3)
    
    play(audio)
    
    os.remove(temp_file)