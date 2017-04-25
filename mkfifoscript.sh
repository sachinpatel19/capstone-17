#!/bin/sh
mkfifo pipeline
omxplayer -o hdmi "$*" < ./pipeline &
