#!/bin/bash

# this file should be a wav file with sample rate of 48000 Hz
# usage: ./transcribeAudio.sh <audio-file>

nodejs ./examples/google-audio-api/speech/recognize.js sync $1 -r 48000