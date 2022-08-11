#write a python program to display the current date and time
import datetime

x= datetime.datetime.now()
print(x)

#write a python program to get the python version you are using
import sys
print("python version")
print(sys.version)
print("python info")
print(sys.version_info)

#radius of a circle
import math
radius= float(input("Enter the radius of the circle : "))

area=math.pi*radius*radius

print("area of the circle is : {0}". format (area))

#write a python program to get the volume of a sphere
r=6
pi=3.1415
v=4/3*pi*r**3
print(" the volume of the sphere is:",v )

#write a python program to get the difference



#how to check os name
import platform
import os

print(os.name)
print(platform.system())
print (platform.release)


print(10 > 9)