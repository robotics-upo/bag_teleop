# Bag Teleop Package

This is a simply package that contains only one node. The goal is to simplify the bag recording system when doing for example outdoors experiments. Instead of launching a ```rosbag_record``` in a terminal the node launch a selected .launch file when pressing a button. 

## To do

Make the node easily configurable with .yaml file to choose which button launch which .launch

## Dependencies

The only dependency is the ros joy package. The node subscribes by default to the topic ```/joy```. 