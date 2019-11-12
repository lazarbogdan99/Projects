import pyaudio
import numpy as np

# set up portaudio system / initiate
p = pyaudio.PyAudio()

# read frequencies
def freq():
     # sine frequency, Hz / frequency of the note
    f = input("Enter frequencies: ")   
    fr = np.array(f.split()).astype(float)
    return fr

volume  = 0.5                       # range [0.0, 1.0]
fs = 44100                          # sampling rate, Hz
duration = 2.0                      # in seconds
frequencies = freq()

while True:
    for i in frequencies:
        # generate samples
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*
            i/fs)).astype(np.float32)

        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

        # play sound
        stream.write(volume*samples)

        stream.stop_stream()
        stream.close()

    play = input("play again: ")
    if play == 'new':
        frequencies = freq()
    elif play == "n":
        break

p.terminate()