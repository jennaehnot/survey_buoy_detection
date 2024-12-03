#!/usr/bin/python3
import rospy
from std_msgs.msg import String
from vision_msgs.msg import Detection2DArray
from sound_play.msg import  SoundRequest
from sound_play.libsoundplay import SoundClient
from sensor_msgs.msg import CameraInfo

soundhandle = SoundClient()
lastbeep=0
BNDRY=[]
detects=[]
x_margin=rospy.get_param("/beeper_node/x_margin")
DELAY=rospy.get_param("/beeper_node/delay")

def callback(data):
    global lastbeep
    global detects

    object=data.detections

    if len(object) != 0: #if there's been a detection
       timestamp=data.header.stamp.secs

       if timestamp > (lastbeep + DELAY):

           #pull detect id and boundary box info from data
           id=data.detections[0].results[0].id
           bbox=data.detections[0].bbox
           bbox_x=bbox.center.x
           bbox_y=bbox.center.y
           size_x=bbox.size_x
           size_y=bbox.size_y
           area=size_x*size_y

           #pack detects array
           detects.append([timestamp, id, bbox_x, bbox_y, area])

           if id == 0:
                if (bbox_x > BNDRY[0]) and (bbox_x < BNDRY[1]):
                    soundhandle.playWave('/home/field/project11/catkin_ws/src/survey_buoy_detection/detect_buoys/config/beep-twice.wav', 1.0)
                    lastbeep=timestamp
                    print("beepin!")
                    print(detects[-1])
                    detects=[]
def listener():

    rospy.init_node('beep', anonymous=True)
    msg=rospy.wait_for_message('/camera_info',CameraInfo) #pull camera info, we only do this once
    WIDTH=msg.width #from camera info, find image width
    HEIGHT=msg.height
    CENTER=WIDTH/2 #calc center of image, we're using this as the area  directly in front of the boat

    #build boundary array; will need updating in future (today: 08.09.23)
    BNDRY.append(CENTER-x_margin) 
    BNDRY.append(CENTER+x_margin)
    print("center: ",CENTER, "Bndry: ", BNDRY[0], ", ", BNDRY[1])
    rospy.Subscriber("/yolo/detections", Detection2DArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
