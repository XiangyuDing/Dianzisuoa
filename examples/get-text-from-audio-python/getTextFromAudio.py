#! /usr/bin/python3
#--------------------------------#
# File name: getTextFromAudio.py
# Author: Betsalel "Saul" Williamson
# Created on: October 11, 2017
# saul.williamson@pitt.edu
#--------------------------------#

## use accelerometer
import sys, traceback
import subprocess
import time
import os
import signal
import pyaudio, wave

BUFFER_SIZE = 1024
REC_SECONDS = 5
RATE = 48000
WAV_FILENAME = "foo.wav"
FORMAT = pyaudio.paInt16

from random import randint

def main():
    try:
        pa = pyaudio.PyAudio()
        for i in range(pa.get_device_count()):
          dev = pa.get_device_info_by_index(i)
          print((i,dev['name'],dev['maxInputChannels']))
          
        stream = pa.open(
            format = FORMAT,
            input = True,
            channels = 1,
            rate = RATE,
            input_device_index = 2,
            frames_per_buffer = BUFFER_SIZE
        )

        #run recording
        print('Recording...')
        data_frames = []
        toRange = int(RATE/BUFFER_SIZE * REC_SECONDS)
        for f in range(0, toRange):
            data = stream.read(BUFFER_SIZE)
            data_frames.append(data)
        print('Finished recording...')
        stream.stop_stream()
        stream.close()
        pa.terminate()

        wf = wave.open(WAV_FILENAME, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(pa.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(data_frames))
        wf.close()
        
        text = 'hello'
        proc = subprocess.Popen(
            ['./transcibeAudio.sh', WAV_FILENAME],stdout=subprocess.PIPE)

        result = proc.stdout.read()
        print result
        proc.wait()

    except KeyboardInterrupt:
        print("\nShutdown requested...exiting")
        
    except Exception:
        traceback.print_exc(file=sys.stdout)
        
    sys.exit(0)
## end of animate pet
if __name__ == "__main__":
    main()
    
