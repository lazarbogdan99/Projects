from tkinter import *
import pyaudio
import wave
import sys
import threading
import numpy as np

# --- classes ---

def play_audio():
    global is_playing
    global my_thread

    volume  = 0.5                       # range [0.0, 1.0]
    fs = 44100                          # sampling rate, Hz
    duration = 2.0                      # in seconds
    f = 440.0

    p = pyaudio.PyAudio()

    # generate samples
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*
                f/fs)).astype(np.float32)

    stream = p.open(
        format = pyaudio.paFloat32,
        channels = 1,
        rate = fs,
        output = True)

    while is_playing: # is_playing to stop playing
        stream.write(volume*samples)
        
    stream.stop_stream()
    stream.close()

    p.terminate()


# --- functions ---

def press_button_play():
    global is_playing
    global my_thread

    if not is_playing:
        is_playing = True
        my_thread = threading.Thread(target=play_audio)
        my_thread.start()

def press_button_stop():
    global is_playing
    global my_thread

    if is_playing:
        is_playing = False
        my_thread.join()

# --- main ---

is_playing = False
my_thread = None

root = Tk()
root.title("Magikarp")
root.geometry("400x300")

button_start = Button(root, text="PLAY", command=press_button_play)
button_start.grid()

button_stop = Button(root, text="STOP", command=press_button_stop)
button_stop.grid()

root.mainloop()