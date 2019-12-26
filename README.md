# Bag Teleop Package

This is a simply package that contains only one node. The goal is to simplify the bag recording system when doing for example outdoors experiments. Instead of launching a ```rosbag_record``` in a terminal the node launch a selected .launch file when pressing a button. 

## Configuring the node

At this moment there are 3 buttons configured(make sure to use the joystick in X mode): 

-   A
-   X
-   BACK

Each one launch a bag in the launch/ folder of the package named as the button, a.launch, x.launch, back.launch. 

## To do

Make the node easily configurable with .yaml file to choose which button launch which .launch

## Dependencies

The only dependency is the ros joy package. The node subscribes by default to the topic ```/joy```. 