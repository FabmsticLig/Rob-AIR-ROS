#!/usr/bin/env python

import rospy
import subprocess
import re

from std_msgs.msg import Int8

def wifi_monitor():
	pub = rospy.Publisher('wifi_quality', Int8, queue_size=10)
	rospy.init_node('wifi_monitor', anonymous=True)
	iface = rospy.get_param('~interface', 'wlan0')
	
	rate = rospy.Rate(1) # 1hz
	while not rospy.is_shutdown():
		cmd = subprocess.Popen('iwconfig {}'.format(iface), shell=True, stdout=subprocess.PIPE)
		expr = re.compile(' *Link Quality=(\d*)/(\d*) *Signal level=(-?\d*) *dBm')
		for line in cmd.stdout:
			m = expr.match(line)
			if m:
				quality = (int(m.group(1))*100)/int(m.group(2))
				rospy.loginfo('quality : {}'.format(quality))
				pub.publish(quality)
			elif 'Not-Associated' in line:
				quality = 0
				rospy.loginfo('quality : {}'.format(quality))
				pub.publish(quality)
				
		rate.sleep()

if __name__ == '__main__':
	try:
		wifi_monitor()
	except rospy.ROSInterruptException:
		pass
