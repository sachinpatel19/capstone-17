#!/bin/sh
mkfifo pipeline
echo "I get here"
omxplayer -o hdmi "$*" < ./pipeline &
