maze_solvable = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

maze_unsolvable = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def find_neigh(y, x, maze): #x cols y rows
    neighbours = []

    if( x > 0 ):
        neighbours.append((y, x - 1))
    
    if( x < len(maze[0]) - 1 ):
        neighbours.append((y, x + 1))

    if ( y > 0):
        neighbours.append((y - 1, x))
    
    if (y < len(maze) - 1):
        neighbours.append((y + 1, x))

    return neighbours


def solve_maze(maze):
    queue = []
    visited = []
    start = (1,1) #starting point
    finish = (1,5) #goal

    #initialize backtrace list
    backtrace = {}

    #mark walls as visited cells
    for y in range(0, len(maze)): #row
        for x in range(0, len(maze[y])): #col
            if(maze[y][x] == 1):
                visited.append((y, x)) #tuple with position

    queue.append(start)
    maze[start[0]][start[1]] = 2
    while(len(queue) > 0):
        current = queue.pop(0) #remove first element from list
        x = current[1]
        y = current[0]

        if (start == finish): #did we reach the goal?
            return True
        
        if(current != start):
            maze[y][x] = 2 #visuals for me
        
        neighbours = find_neigh(y, x, maze)

        for i in range(0, len(neighbours)):
            check = neighbours[i]

            if(not (check in visited)):
                visited.append(check)
                #How we got there??!
                backtrace[str(check[0]) + "_" + str(check[1])] = current

                queue.append(check)

    print(backtrace)

    if(current == finish):
        #PATH RECREATION
        path = [finish]
        current = finish

        while(current != start):
            current = backtrace[str(current[0]) + "_" + str(current[1])]
            path.insert(0, current)

        if(len(path) > 2):
            for i in range(0, len(path)):
                y = path[i][0]
                x = path[i][1]
                maze[y][x] = 3 #visuals for me

        for line in maze:
            print(line)
        return True
        
    else:

        for line in maze:
            print (line)
        print("Cannot solve!")
        return False


solve_maze(maze_solvable)
print("\n\n\n")
solve_maze(maze_unsolvable)
