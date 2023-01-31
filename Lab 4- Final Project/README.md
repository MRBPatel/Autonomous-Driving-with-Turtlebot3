# Team 4 - Vinus

## Lab 4:

### Final project- TurtleBot Path-finding and Automatic Parking
####Methodology
##### Wall follower
We built a wall following algorithm where our bot would forward until it finds a point and turn right as soon as it reaches a 


##### Mapping
A SLAM method is used by the robot to map out its surroundings. Data from the LIDAR is used to built a map and saved in a range.txt file. The LIDAR gives the intensity values in the map.


##### Localization
The robot uses information from its sensors to pinpoint where the desired point is in the map which would we later used for parking.


##### Returning to Original Position
After completing the wall follow and mapping, subtask is to reach the starting position. These were achieved by navigating towards the starting position using PI controller and A* algorithm. 


##### Path Planning
The robot plans a path to the assigned parking space using the navigation stack. To accomplish this, one can use the environment's various characteristics or park according to the marked lines.


##### Locating the nearest parking spot:  
Using the information gathered during mapping and all possible parking spots, locate the parking lot with a given intensity (the intensity of the black tape) which is closest to the initial position 


##### Navigating to the Parking location: 
We employed A* algorithm, a popular method for pathfinding and graph traversal and the robot moves 


##### Parking
The robot can utilize its sensor data to pinpoint the precise location and orientation of the goal.

    



