cmake_minimum_required(VERSION 2.8.3)
project(bag_teleop)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  joy
)

catkin_package(
)

include_directories(

  ${catkin_INCLUDE_DIRS}
)

