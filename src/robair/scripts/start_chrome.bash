#!/bin/bash

source /home/robair/.bashrc

#gst-launch -e v4l2src device=/dev/v4l/by-id/usb-KYE_Systems_Corp._USB_Camera_200901010001-video-index0 ! video/x-raw-yuv, framerate=30/1, width=160, height=120 ! videomixer name=mix ! ffmpegcolorspace ! v4l2sink device=/dev/video0 v4l2src device=/dev/v4l/by-id/usb-Microsoft_Microsoft®_LifeCam_HD-5000-video-index0 ! video/x-raw-yuv,framerate=30/1,width=640,height=480 ! mix. & #> /home/robair/scripts/stdout 2>/home/robair/scripts/stderr&

#gst-launch -e v4l2src device=/dev/video2 ! video/x-raw-yuv, framerate=30/1, width=160, height=120 ! videomixer name=mix ! ffmpegcolorspace ! v4l2sink device=/dev/video0 v4l2src device=/dev/video3 ! video/x-raw-yuv,framerate=30/1,width=640,height=480 ! mix. & #> /home/robair/scripts/stdout 2>/home/robair/scripts/stderr&

#gst-launch -e v4l2src device=/dev/v4l/by-id/usb-KYE_Systems_Corp._USB_Camera_200901010001-video-index0 ! video/x-raw-yuv, framerate=30/1, width=160, height=120 ! videomixer name=mix ! ffmpegcolorspace ! v4l2sink device=/dev/video0 v4l2src device=/dev/v4l/by-id/usb-Microsoft_Microsoft®_LifeCam_HD-5000-video-index0 ! video/x-raw-yuv,framerate=30/1,width=640,height=480 ! mix.

sleep 5

google-chrome --kiosk http://192.168.1.2:8087
#google-chrome http://192.168.1.2:8087
