import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist
import math
import numpy as np
from testspot import wallfollower
from Astar import AStarPlanner
from Astar import main
from pathplanning import Task1
from rotate import rotate
import time

# variable which need later on

roll = pitch = yaw = 0.0

kp=0.5

#rospy.init_node('parking_node')

def get_rotation (msg):
    global roll, pitch, yaw, target_rad, cur_position
    cur_position = msg.pose.pose.position
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    #print(yaw)
	

sub = rospy.Subscriber ('/odom', Odometry, get_rotation)


if __name__ == "__main__":
    task3 = wallfollower()
    task3.check()

    s, target_rad, p = task3.get_cor()
    p1 = task3.get_spot()
    print(target_rad)

    print(p1)
    #print(y)

    items = []
    items.append(s)
    items.append(p)
    print(s)
    print(p)
    
    file_to_delete = open("items.txt",'w')
    file_to_delete.close()
    file = open('items.txt','w')
    for item in items:
    	for i in range(3):
            s1 = str(item[i])
            file.write(s1 +"\n")
    file.close()
    
    sx = cur_position.x
    
    sy = cur_position.y
    gx = s[0]
    gy = s[1]
    task1 = Task1()
    task1.spin(sx, sy, gx, gy)
    
    #target_rad = target*math.pi/180
    a = target_rad + yaw
    time.sleep(3)

    if yaw >= 0 and a > 6.24:
        target_rad = a + 2*np.pi
        
    elif yaw >= 0 and a > 3.14:
        target_rad = (a-2*np.pi)
        
    elif yaw < 0 and a > 0:
        target_rad = a
        
    elif yaw < 0 and a < 0:
        target_rad = a
    else:
        print('conversion is not possible')
    #rotate()
    Dis = []
    X = []
    Y = []
    file = open('ranges.txt','r')
    lines = file.readlines()
    collision = []
    for i in range(len(lines)):
        s12 = []
        s1 = lines[i]
        #s1 = lines[1]
        p = s1.split("\n")
        p = p[0].replace("[", "")
        p = p.replace("]", "")
        p = p.split(",")
        p = np.array(p)
        res = p.astype(np.float)
        c1 = res.tolist()
        collision.append(c1)

    ox, oy = [], []
    for i in range(len(collision)):
        p, q = collision[i][0], collision[i][1]
        ox.append(p)
        oy.append(q)
        
    # start and goal position
    '''
    sx = 3.8  # [m]
    sy = 0.06 # [m]
    gx = 0.3  # [m]
    gy = 0.0  # [m]
    '''
    grid_size = 0.05  # [m]
    robot_radius = 0.105  # [m]
    sx = s[0]
    sy = s[1]
    p23 = []

    print(p1)
    #p23 = p1
    
    for i in range(len(p1)):
    	p12 = p1[i]
    	if math.isnan(p12[0]):
    		print('.')
    	else:
    		p23.append(p12)

    print(len(p1))
    for i in range(len(p23)):
        p13 = p23[i]
        gx1 = p13[0]
        gy1 = p13[1]

        a_star = AStarPlanner(ox, oy, grid_size, robot_radius)
        rx, ry, D = a_star.planning(sx, sy, gx1, gy1)
        Dis.append(D)
        
    time.sleep(3)
    Dis1 = Dis
    if len(Dis1) == 1:
        i = 0
    else:
        i = Dis1.index(min(Dis1))


    print(Dis)
    print('1111')
    print(p1)
    print('1111')
    print(i)
    print('1111')
    print('1211')
    print(len(Dis))
    print('3333')
    time.sleep(3)

    f = p1[i]
    fgx = f[0]
    fgy = f[1]
    task1 = Task1()
    task1.spin(sx, sy, fgx, fgy)    
    	
