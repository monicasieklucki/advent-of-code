def main():  
    # opening file and reading lines
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    line_segments = []  
    # xstart,ystart -> xend, yend 
    for line in lines:
        print(line)
        line = line.split(' ')
        # preprocess lines to get x and y coordinates
        start_coords = line[0]
        stop_coords = line[2]
        start = start_coords.split(',')
        stop = stop_coords.split(',')
        x1 = int(start[0])
        y1 = int(start[1])
        x2 = int(stop[0])
        y2 = int(stop[1])

        # PART 1
        # it's very slow - wys to speed this up?? 
        if x1 == x2:   
            get_vertical_lines(x1,x2,y1,y2,line_segments)
        elif y1 == y2:
            get_horizontal_lines(x1,x2,y1,y2,line_segments)
        else: #PART 2
            # diagonal lines here
            print("diagonal")
            get_diagonal_lines(x1,x2,y1,y2,line_segments)
    
    visited = []
    unvisited = []
    for coords in line_segments:
        if coords not in unvisited:
            unvisited.append(coords)
        elif coords in unvisited and coords not in visited:
            visited.append(coords)

    print(f"At least two lines overlap at {len(visited)} points.")

def get_vertical_lines(x1,x2,y1,y2,line_segments):
    verticals = []   
    for y in range(y1, y2+1):
        line_segments.append((x1,y))
    for y in range(y2, y1+1):
        line_segments.append((x1,y))
    return

def get_horizontal_lines(x1,x2,y1,y2,line_segments):
    horizontals = []
    for x in range(x1, x2+1):
        line_segments.append((x, y1))
    for x in range(x2, x1+1):
        line_segments.append((x, y1))
    return


def get_diagonal_lines(x1,x2,y1,y2,line_segments):
    # instead of using <,>
    # use min and max functions
    if x1>x2 and y1<y2:
        for x in range(x2,x1+1):
            #print(x, y2)
            line_segments.append((x,y2))
            y2 = y2-1
        return 
    elif x1>x2 and y1>y2:
        for x in range(x2,x1+1):
            #print(x, y2)
            line_segments.append((x,y2))
            y2 = y2+1
        return 
    elif x1<x2 and y1<y2:
        for x in range(x1,x2+1):
            #print(x,y1)
            line_segments.append((x,y1))
            y1 = y1+1
        return 
    elif x1<x2 and y1>y2:
        for x in range(x1,x2+1):
            #print(x,y1)
            line_segments.append((x,y1))
            y1=y1-1
        return
     
    return       
       
if __name__ == "__main__":
    main()