#!/usr/bin/env python
# license removed for brevity
import rospy
from md49test.msg import MotorCmd

def follow():
    pub = rospy.Publisher('/cmdmotors', MotorCmd, queue_size=1000)
    rospy.init_node('follow', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	msg = MotorCmd()
        msg.speed1 = 10
	msg.speed2 = 10
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        follow()
    except rospy.ROSInterruptException:
        pass

