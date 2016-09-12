#!/bin/bash

gst-launch-1.0 tcpclientsrc host=192.168.0.151 port=5000 ! h264dec ! autovideosink sync=false
