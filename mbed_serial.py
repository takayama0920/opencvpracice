import rospy
from std_msgs.msg import Float64
import serial

rospy.init_node('topic_publisher')

pub = rospy.Publisher('country',Float64, queue_size=10)

ser = serial.Serial('/dev/ttyACM0', timeout=0.1)

while True:
    c = ser.read()
    str = ser.read(100)
    line = ser.readline()
    pub.publish(ser.read(100))
    print(str) 

