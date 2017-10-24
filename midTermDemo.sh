#!/bin/bash
# this assumes that the audio device is connected and there is internet connection

echo "************************"
echo "**** Mid Term Demo ******"
echo "************************"

printf "\n\nRunning audio demo:\n"

./record.sh temp/demo.wav

ls temp/

./transcibeAudio.sh temp/$(ls temp | sort -n | head -1)

rm temp/*

ls temp/

printf "\n\nRunning keypad demo:\n"

./examples/keypad/keypad.py