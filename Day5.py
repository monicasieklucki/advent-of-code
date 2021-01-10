import math 

def main():
    seat_ids = []

    rows = []
    columns = []

    with open(r"/Users/monicasieklucki/Desktop/advent-of-code/input/Day5.txt") as file:
        for line in file:
            
            row = line[0:7]
            column = line[7:10]
            
            row_num = binary_search(row,0,127) #row
            col_num = binary_search(column,0,7) #column
            
            rows.append(row_num)
            columns.append(col_num)
                        
            print((row_num * 8) + col_num)
            seat_ids.append((row_num * 8) + col_num)

    
    #PART 1
    print("Highest Seat ID: " + str(max(seat_ids)))
    max_seat_id = max(seat_ids)
    min_seat_id = min(seat_ids)

    #PART 2    Answer: 671 hoowww
    #TODO  
    seat_ids.sort()
    print(seat_ids) 
    
      
def binary_search(string, l, h):

    low = l
    high = h
    
    for ch in string:  
        mid = math.ceil(high + low) // 2 # integer division
        if ch == 'B' or ch == 'R': #higher range
            low = math.ceil(mid)
            mid = math.ceil(mid)
        elif ch == 'F' or ch == 'L': #lower range
            high = mid
    return int(mid)
           
main()






