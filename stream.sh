#!/bin/sh

PLUGINPATH=/usr/src/mjpg-streamer-code/mjpg-streamer
STREAMER=$PLUGINPATH/mjpg_streamer
DEVICE=/dev/video0
RESOLUTION=640x480
FRAMERATE=25
HTTP_PORT=8001

# check for existing webcam device
if [ ! -e "/dev/video0" ]; then
  echo "stream.sh: Error - NO /dev/video0 device" 2>&1 | logger
  exit 2
fi

#PLUGINPATH=/usr/local/lib

$STREAMER -i "$PLUGINPATH/input_uvc.so -y -n -d $DEVICE -r $RESOLUTION -f $FRAMERATE" -o "$PLUGINPATH/output_http.so -n -p $HTTP_PORT -w $PLUGINPATH/www" -b

#cd /usr/src/
#$STREAMER -i "$PLUGINPATH/input_uvc.so -y -n " -o "$PLUGINPATH/output_http.so -n -w ./www -p 8001"
