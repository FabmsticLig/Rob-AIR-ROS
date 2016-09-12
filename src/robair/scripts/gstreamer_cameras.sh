#!/bin/sh

gst-launch \
   videomixer name=mix sink_0::zorder=2 sink_1::zorder=1 ! ffmpegcolorspace ! v4l2sink device=/dev/video3 \
   v4l2src device=/dev/video1 ! video/x-raw-yuv,width=160,height=120,framerate=30/1 ! ffmpegcolorspace ! videobox border-alpha=1.0 top=-2 bottom=-2 left=-2 right=-2 ! mix.sink_0 \
   v4l2src device=/dev/video2 ! video/x-raw-yuv,width=640,height=480,framerate=30/1 ! ffmpegcolorspace ! mix.sink_1

