## Traveling-Ethiopia-Problem-II 
Questions 
1. Consider Figure 1 (A generic state space graph for traveling Ethiopia search problem) to solve  the following problems. 

1.1 Convert Figure 1, a State space graph for traveling Ethiopia search problem, into some  sort of manageable data structure.  

1.2 Write a class that takes the converted state space graph, initial state, goal state and a  search strategy and return the corresponding solution/path according to the given strategy.  Please consider only breadth-first search and depth-first search strategies for this question. 

![fig1](images/Figure%201%20Traveling%20Ethiopia.png "Traveling Ethiopia")



2. Given Figure 2, a state space graph with backward cost for the traveling Ethiopia search  problem. 

2.1 Convert Figure 2 into some sort of manageable data structure .

2.2 Assuming “Addis Ababa” as an initial state, write a program that use uniform cost search to generate a path to “Lalibela”. 

2.3 Given “Addis Ababa” as an initial state and “Axum”, “Gondar”, “Lalibela”, Babile,  “Jimma”, “Bale”, “Sof Oumer”, and “Arba Minch” as goal states;in no specific order, write  a customized uniform cost search algorithm to generate a path that let a visitor visit all those  goal states preserving the local optimum. 


![fig2](images/Figure%202%20Traveling%20Ethiopia.jpg "Traveling Ethiopia")


3. Given Figure 3, a state space graph with heuristic and backward cost. Write a class that use A*  search to generate a path from the initial state “Addis Ababa” to goal state “Moyale”. 

 ![fig3](images/Figure%203%20Traveling%20Ethiopia.jpg "Traveling Ethiopia")
4. Assume an adversary joins the Traveling Ethiopia Search Problem as shown in Figure 4. The goal of the agent would be to reach to a state where it gains good quality of Coffee. Write a class that  shows how MiniMax search algorithm directs an agent to the best achievable destination.  

![fig4](images/Figure%204%20Adversary%20Traveling%20Ethiopia.jpg "Traveling Ethiopia")




Note: A working solution for the following question may override your final exam result. 



5. Interactive Intelligent systems: Figure 5 is a relaxed state space graph for traveling Ethiopia  search problem.  

5.1 Design a three-wheel functional robot using Gazebo. Let it have a working physics  engine and sensors such as Proximity sensor, gyroscope, RGB camera, ... 

5.2 Create a .world file with all the states in Figure 5 using a Cartesian coordinate system. 

5.3 Write a ROS based class that use any uninformed search strategy and generate a path for  the robot to travel from any given initial state in Figure 5 to the given goal state. 

![fig5](images/Figure%205%20Traveling%20Ethiopia.png "Traveling Ethiopia")


Summary 
The questions are very related and are based on the algorithms we have covered in our class. Dealing with the first few questions correctly help you undertake the consecutive questions quickly and correctly. Therefore, I recommend you to spend more time in understanding the questions. Submissions are using a google form where I will put a place to write your project GitHub link. Your repository should be clean and easily reproducible. There will be in-person presentation session a week after your final Exam. 
