#!/bin/bash

./record.sh

ls temp/

nodejs ./examples/google-audio-api/speech/recognize.js sync temp/b-01.wav -r 48000

rm ./temp/*

ls temp/











