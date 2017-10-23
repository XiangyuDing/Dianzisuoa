#!/bin/bash

# arecord -f cd -t wav | flac - -o out.flac
arecord -f DAT --channels=1 --duration=5 -D sysdefault:CARD=1 temp/b.wav
