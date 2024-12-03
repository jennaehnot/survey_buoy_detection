#!/usr/bin/python3
import time
import math
from datetime import datetime, date

file=open('/home/field/project11/catkin_ws/src/survey_buoy_detection/detect_buoys/feedback.txt','a') #open file

#Prompt for feedback
feedback=input("Enter your feedback/comments here: ")

#Get date and time, start new line at end of file, and write date and time
now=datetime.now()
now=now.strftime("%H:%M:%S")
#file.write("\n{0} {1}: ".format(date.today(),now))
file.write("\n{0} {1}: {2}".format(date.today(),now,feedback))

#calc how many lines we'll need to print
#this is to prevent the txt document from having extremely long run-on lines
#num_char=len(feedback)
#line_length=55
#num_lines=math.floor(num_char/line_length)
#strt=0
#for i in range(0,num_lines):
#     file.write("{0}\n".format(feedback[strt:strt+line_length]))
#     strt=strt+line_length
#file.write("{0}\n".format(feedback[strt:]))
#file.write(feedback)

#Wrap it up
print("\nGot it, thanks!")
file.close()
time.sleep(2)


