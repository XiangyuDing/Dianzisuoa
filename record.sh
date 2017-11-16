#!/bin/bash

# useage ./record.sh <filename.wav>

# arecord -f cd -t wav | flac - -o out.flac
arecord -f DAT --channels=1 --duration=5 -D sysdefault:CARD=1 $1
