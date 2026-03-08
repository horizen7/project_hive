"""
------- A* INTUITION ------
f(n) = g(n) + h(n)  
where f(n) is the total cost (the cost of the actual distance g and the heuristic); A* tries to find the lowest version of this
where g(n) is the actual amount of steps it takes to get to a given node
where h(n) is a heurisitc that give the predicted distance from the starting node to some other node in the graph
"""

import heapq

def a_star(graph, start, goal, heuristics):
    # ----------INITIALIZE PERSISTENT STRUCTURES/VARIABLE-------------
    # A* picks the node and path to pursue from open set based off the queue which has information about the smallest f value

    open_set = [(heuristics[start],start)] #stores the priority queue of the nodes in the graph
    g_costs = {start: 0} #what is this notation? makes sense that the cost from the starting node to itself is zero, but dictionary notation never like that?
                         #is it default initialized to zero?
    came_from = {} #keep track of the path to reconstruct later - what does it mean reconstruct later?
    

    # ---------THREE STEPS FOR FASTEST PATH FINDING---------------

    while open_set: # does everything in the heapq get used up?
        #retrieve and unpack the value of f (which is probably stored) and the name of the node
        #from the lowest value of from open_set

        current_f, current_node = heapq.heappop(open_set) 
        print(f"\nExploring {current_node}")

        #--------------CONDITION TO CHECK IF GOAL REACHED---------------
        if current_node == goal:
            print("Goal Reached!")

            #reconstruct path in the right order since path chain exists in came_from
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start) #why must the start be appended, shouldn't it be written into came_from 
            return path[::-1] #reverse so path is from end-goal
        
        #---------LOOK AT ALL THE NEIGHBORS TO A GIVEN NODE----------
        for neighbor, move_cost in graph[current_node]: #graph data gives the neighbors and their move_costs
            tentative_g_cost = g_costs[current_node] + move_cost #what does tentative mean in this case 
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]: #prevents going backwards 
                came_from[neighbor] = current_node #parent is neighbor
                g_costs[neighbor] = tentative_g_cost #add the g cost (steps taken) and save this 

                # calculate f = g+h
                f_cost = tentative_g_cost + heuristics[neighbor] 

                heapq.heappush(open_set, (f_cost, neighbor))
                print(f"  Added/Updated neighbor {neighbor} with f-cost {f_cost}")

    #when would None return? If there is not viable path?         
    return None



#---------DATA TO TEST--------- 
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
heuristics = {'A': 7, 'B': 6, 'C': 1, 'D': 0}

# Run it
shortest_path = a_star(graph, 'A', 'D', heuristics)
print(f"\nFinal Shortest Path: {shortest_path}")
                
