from numpy import inf

def main():
    
    with open('input.txt') as f:
        lines = f.readlines()
        matrix = [line.rstrip() for line in lines]
        
    print(matrix)
    rows = len(matrix)
    cols = len(matrix[0])
    print(rows)
    print(cols)
    
    count = 0
    
    lowest_centers = []
    largest_basins = []
    
    for row in range(0,rows):
        for col in range(0,cols):
            center = int(matrix[row][col])

            up = int(matrix[row-1][col]) if (row-1)>-1 else 99
            down = int(matrix[row+1][col]) if (row+1)<rows else 99
            left = int(matrix[row][col-1]) if ((col-1)>-1) else 99
            right = int(matrix[row][col+1]) if ((col+1)<cols) else 99

            if (center<up and center<down and center<left and center<right):
                lowest_centers.append(center+1)
    
    #print(sum(lowest_centers))     
            
if __name__ == "__main__":
    main()