'''
Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
from pydub import AudioSegment
from pydub.playback import play

caminho = r"C:/Users/gusta/Music/Mc Papo - Piriguete (Reggaeton Brasil).mp3"

audio = AudioSegment.from_file(caminho, format="mp3")
play(audio)

