#!/usr/bin/env python
# license removed for brevity
import rospy
import curses
import numpy
from std_msgs.msg import String
from std_msgs.msg import Int8
from rospy.numpy_msg import numpy_msg
from threading import Thread
from md49test.msg import Position
from md49test.msg import MotorCmd


class RosClient(Thread):

	def callback(self,data):
		self.screen.addstr(1, 0, "                                                                            ")
		self.screen.addstr(1, 0, "%f %f %f" % (data.x, data.y, data.theta))
		self.screen.refresh()

	def run(self):
	
		self.screen = curses.initscr()
		curses.cbreak()
		self.screen.keypad(1)

		key = ''
		
		pubs1 = rospy.Publisher('cmdmotors', MotorCmd, queue_size=10)
		pubondo = rospy.Publisher('cmdondo', Int8, queue_size=10)
		rospy.Subscriber("position", Position, self.callback, queue_size = 1)
		rate = rospy.Rate(100) # 10hz
		mcmd = MotorCmd()

		while (not rospy.is_shutdown()) and key != ord('q'):
			key = self.screen.getch()  # get the key
			#screen.clear()
			self.screen.addstr(0, 0, "                           ")  # display it on the screen
			self.screen.refresh()
			

			# the same, but for <Up> and <Down> keys:
			if key == curses.KEY_UP:
				
				self.screen.addstr(0, 0, "Up")
				mcmd.speed1=64
				mcmd.speed2=64
				pubs1.publish(mcmd)

			elif key == curses.KEY_DOWN:
				self.screen.addstr(0, 0, "Down")
				mcmd.speed1=-64
				mcmd.speed2=-64
				pubs1.publish(mcmd)
			elif key == curses.KEY_LEFT:
				self.screen.addstr(0, 0, "Left")
				mcmd.speed1=-64
				mcmd.speed2=64
				pubs1.publish(mcmd)
			elif key == curses.KEY_RIGHT:
				self.screen.addstr(0, 0, "Right")
				mcmd.speed1=64
				mcmd.speed2=-64
				pubs1.publish(mcmd)
			elif key == ord(' '):
				self.screen.addstr(0, 0, "Space")
				mcmd.speed1=0
				mcmd.speed2=0
				pubs1.publish(mcmd)
			elif key == ord('a'):
				self.screen.addstr(0, 0, "a")
				pubondo.publish(0)
			elif key == ord('z'):
				self.screen.addstr(0, 0, "z")
				pubondo.publish(1)
		
			rate.sleep()
		rospy.signal_shutdown("Quit")
			

if __name__ == '__main__':

	rc=RosClient()
	rospy.init_node('cmdspeed1', anonymous=True)
	try:
		rc.start()
		rospy.spin()
		rc.join()
		
	except rospy.ROSInterruptException:
		pass
	curses.nocbreak()
	rc.screen.keypad(0)
	curses.echo()
