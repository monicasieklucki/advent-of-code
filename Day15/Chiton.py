from collections import deque

def main():
      
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        
    
    global matrix, rows, cols
    matrix = lines

    rows = len(matrix)
    cols = len(matrix[0])

    #Dijkstra's Algorithm
    start = (0,0)
    end = (2,2)
    visited = []
    #visited.append(start)
    
    stack = deque()
    stack.append(start)
    
    #distance from each node to the starting node
    distances = {}
    distances[start[0], start[1]] = matrix[start[0]][start[1]]  
    
    while stack:
        print(stack)
        currPos = stack.popleft()
        visited.append(currPos)

        currRow=currPos[0]
        currCol=currPos[1]
        #print(currPos)
        
        if currPos == end:
            break
    
        #up,down,left,right
        children = get_children(currPos)
        for child in children:           
            #up,down,left,right = get_children(currPos)
            if child not in visited and child!=float("inf"): 
                print("current: " + str(currPos))              
                row=child[0]
                col=child[1]
                weight = matrix[row][col]
                
                if distances.has_key(child):
                    if distances[child] > distances[child] + int(matrix[row][col]):
                        distances[child] = distances[child] + int(matrix[row][col])
                else:
                    distances[child] = distances[child] + int(matrix[row][col]) 
                

                stack.append(child)
    
    #print(distances)
    #print(distances[(3,6)])
    
    
    

    
def get_children(currPos):
        
    children = []
    
    row=currPos[0]
    col=currPos[1]

    #distances!!! in matrix
    #int(matrix[row-1][col])
    #int(matrix[row+1][col]
    #int(matrix[row][col-1])
    #int(matrix[row][col+1])
    #cols = len(matrix[0])
    up = (row-1, col) if (row-1)>-1 else float('inf')
    down = (row+1, col) if (row+1)<rows else float('inf')
    left = (row, col-1) if (col-1)>-1 else float('inf')
    right = (row, col+1) if (col+1)<cols else float('inf')
    
    children.append(up)
    children.append(down)
    children.append(left)
    children.append(right)    
    
    return children 
      
if __name__ == "__main__":
    main()