#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python

import datetime
import rospy
from std_msgs.msg import String


# BEGIN CALLBACK
def callback(msg):
#    print(msg)
    print msg.data

    date = datetime.datetime.now()

    with open("encoder.txt","a") as f:
        f.write(str(date)+','+msg.data)
# END CALLBACK


rospy.init_node('topic_subscriber')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('counter', String, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
