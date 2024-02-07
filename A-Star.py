from pyamaze import maze, agent, COLOR
from queue import PriorityQueue

#Heuristic function h mahnattan distance
def heuristic(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    dist = abs(x1 - x2) + abs(y1 - y2)
    return dist

def aStar(m):
    start = (m.rows, m.cols)
    #Define 2 directionaries for g score and h score using dic comprehension
    g_score = {cell:float('inf') for cell in m.grid}
    #start value is 0
    g_score[start] = 0
    #key will be the cell and value will be infinity
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = heuristic(start, (1,1))

    #create a priority queue
    open = PriorityQueue()
    #Put the first entry in the priority queue
    open.put((heuristic(start, (1,1)), heuristic(start,(1,1)),start))

    #Declare empty dictionary to store the inverse path
    aPAth = {}

    #IF the open queue is not empty, get the cell value that has the lowest g score and f score
    while not open.empty():
        currCell = open.get()[2] # this element in the tuple
        if currCell == (1,1):
            break 

        #Explore all directions
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + heuristic(childCell, (1,1))
                
                #Once thr child is found findttemporarr g scoredf and f score
                
                #temp_g_score = g_score[currCell] + 1
                #temp_f_score = temp_g_score + heuristic(childCell, (1,1))

                #If the temp score is greater

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score

                    #Add a new entry in the priority queue
                    open.put((temp_f_score, heuristic(childCell,(1,1)), childCell))

                    #Add the current cell as a value in the path dictionary and child cell is the key value
                    aPAth[childCell] = currCell
    forwardPath = {}
    cell = (1,1)
    while cell != start:
        forwardPath[aPAth[cell]] = cell
        cell = aPAth[cell]

    return forwardPath
                    

             

                


m = maze(15,15)

m.CreateMaze()

path = aStar(m)

a = agent(m, footprints= True)

m.tracePath({a:path}) #Dictionary with key as agent and value is path



m.run()