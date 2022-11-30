# Smarter-Traffic

You can try out this project!

## Introduction
Upon tasked with the challenge of creating a STEM solution for climate change, I decided to focus on one of the greatest contributors to CO2 emissions (and by extension climate change) the transportation industry. Specifically commercial trucks and vehicles that emit a large quantity of CO2 when idling. I tackle this problem by creating 2 programs that work together to prevent large trucks from idling as long at an intersection.


## Plan
There are 3 main components to this solution. 
1. Grabbing data from a camera that can see all cars in a specific lane 
2. Interpreting this data and making a decision about which lane gets priority 
3. communicating the decision made by the program to actual traffic lights by using a simple text file.

These 3 components work together to allow large carbon emmittors such as trucks and buses to spend less time idling and less time overall on the road. Due to the ever increasing number of commercial trucks and lorries on the road, the amount of time all trucks spend not idling adds up quickly. 

## Shortcomings
The program has individual parts that do their jobs properly but cannot communicate with each other. Specifically The image detection software is supposed to recognize the different types of vehicles and **then** take the different types of vehicles and store how many appear on the screen in real time however the program I created completes these tasks seperately and can only log how many cars are on the screen without differentiating between different types.

## Creators

This project was created by James Zhang

Biography:
* Burnaby North Secondary School grade 11 student
* Took AP Computer Science course offered by school (Basic Java)
* Interested in the real world applications of tech
* Beginner Python and image classification experience


## Future Plans

I hope in the future to be able to merge the two OpenCV python applications into a single application which can do what both applications do at once(detect different vehicles and log the amount of each that are present as two different variables) which would improve automation. I also hope to work with actual Traffic Engineers in the future to better understand the flow of traffic if my model was implemented in the real world. 


## Technologies

Technologies Used: JFrame, OpenCV, 

Languages Used: Python, Java
