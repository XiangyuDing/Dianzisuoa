#!/bin/bash

arecord -D plughw:0,0 -d 5 -r 16 -f S16_LE | flac - -f --best --sample-rate 16000 -o file.flac