import pyaudio
import wave
from pylab import *
import scipy.io.wavfile as wav

"""
notas_Hz = {'A': 440.00, # la
            'B': 493.88, # si
            'C4': 523.251,
            'D4': 587.33,
            'E4': 659.255,
            'F4': 698.456,
            'G4': 783.991,
            'A4': 880.00, #la 4
            'C': 261.63, # do
            'D': 293.66, # re
            'E': 329.63, # mi
            'F': 349.23, # fa
            'G': 392.00,# sol            
            'DO': 523.25, # do octava
            'P': 0.0} 
"""
notasGuitarra = {1: 329.63,
                 2: 246.94,
                 3: 196.0,
                 4: 146.83,
                 5: 110.0,
                 6: 82.41}

"""
'E4' : 329.63,
'B3' : 246.94,
'G3' : 196.0,
'D3' : 146.83,
'A2' : 110.0,
'E2' : 82.41
"""


def record(seconds):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = seconds
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def convert(cuerda):
    srate2, data2 = wav.read('output.wav')
    X = fft(data2)
    N = len(data2)
    X_mag = abs(X) * 2.0 / N
    freq = fftfreq(len(data2), 1.0 / srate2)
    if (cuerda==1):
        X1 = where(abs(freq)>190 , X, 0)
        X2 = where(abs(freq)<500 , X1, 0)
    elif (cuerda == 2):
        X1 = where(abs(freq)>140 , X, 0)
        X2 = where(abs(freq)<400 , X1, 0)
    elif (cuerda == 3):
        X1 = where(abs(freq)>110 , X, 0)
        X2 = where(abs(freq)<310 , X1, 0)
    elif (cuerda == 4):
        X1 = where(abs(freq)>90 , X, 0)
        X2 = where(abs(freq)<200 , X1, 0)
    elif (cuerda == 5):
        X1 = where(abs(freq)>50 , X, 0)
        X2 = where(abs(freq)<190 , X1, 0)
    elif (cuerda == 6):
        X1 = where(abs(freq)>10 , X, 0)
        X2 = where(abs(freq)<150 , X1, 0)
    X_mag = abs(X2)*2.0/N
   # plot (freq, X_mag)
    #show()
    return freq, X_mag


def getFreq(frecuencia, magnitud):
    maximo = max(magnitud)
    for i in range(0, len(magnitud)):
        if magnitud[i] == maximo:
            return abs(frecuencia[i])


def afinador(cuerda):
    frecuenciaTeorica = notasGuitarra[cuerda]
    print "Toque la cuerda en este momento"
    record(3)
    f, mag = convert(cuerda)
    frecuenciaReal = getFreq(f, mag)
    if (frecuenciaReal - frecuenciaTeorica) < -3:
        return frecuenciaReal, frecuenciaReal, frecuenciaTeorica,"La cuerda esta muy baja"
    elif (frecuenciaReal - frecuenciaTeorica) > 3:
        return frecuenciaReal, frecuenciaReal, frecuenciaTeorica,"La  esta  muy alta"
    else:
        return frecuenciaReal, frecuenciaReal, frecuenciaTeorica,"La cuerda esta perfecta"