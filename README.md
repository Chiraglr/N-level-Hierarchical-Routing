# N-level-Hierarchical-Routing
Problem Statement: Routers have limited memory and compute power. Networks may grow so large that routers may not have the memory to store so many router addresses in its routing table or it may not have enough compute power to compute the routing table for all the routers in the network within a stipulated time. Therefore, hierarchical routing comes into picture. Hierarchical routing divides the network into different levels. This helps reduce memory consumption drastically, but, there is a price to pay for the improved memory consumption. There is no guarantee that the path taken by packets will be the most efficient path. This project simulates how n-level hierarchical routing can be used in networks. 

Language Used: Python

Network Requirements:
    i)In a n-level hierarchical network, there will normal routers that are at the bottom of the hierarchy and there will border gateway routers of varying levels from 1-level border gateway routers till n-level border gateway routers. An i-level border gateway router can be connected(or adjacent) to i-1-level border gateway routers, i-level border gateway routers and i+1 border gateway routers only. So in a 4-level hierarchical network, a 3-level border gateway router can be connected to 2-level border gateway routers, 3-level border gateway routers and 4-level border gateway routers. It cannot be connected to any other routers. Our routing algorithm doesn’t support that type of networks.
    ii)A router can be a multi-level border gateway router, but the different levels have to be consecutive, there cannot be any gaps. So a router can be a 2-level, 3-level, 4-level border gateway router but it cannot be a 2-level and 4-level border gateway router as there is a gap between 2 and 4 that is 3.

Example Network:
    It is a 2-level hierarchical network. Nodes 2,7,9,15,18,22,28 and 35 are 1-level border gateway routers. They interconnect the hierarchically lowest circles. Nodes 10,13,26 and 35 are 2-level border gateway routers as they interconnect the hierarchically highest circles.
The example hierarchical network shown in “Computer Networks by Andrew Tannenbaum” also works. 
![image](https://user-images.githubusercontent.com/29271117/42745582-31dc2c02-88f1-11e8-8ef8-0c4b172c97db.png)
Output:
![image](https://user-images.githubusercontent.com/29271117/42745622-6c008d92-88f1-11e8-9be5-139733655567.png)
Algorithms used: Floyds algorithm(To compute the cost for traversals between nodes), dijkstra’s 
                             algorithm(To trace the path taken between two nodes.)

Numbering used to identify nodes: Nodes are numbered in ascending order in clockwise order in
                             1-level network and then proceed to the next 1-level network in clockwise
                             direction inside a 2-level network and so on. So 1.1.1 will be router 0 in above 
                             network and 3.2.1 will be 35. The  first number in the address indicates the
                             highest level network and the second the second highest level network and so on.
