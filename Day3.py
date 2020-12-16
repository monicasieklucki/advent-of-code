def main():
    print(
        count_trees_from_slope(1, 1) *
        count_trees_from_slope(3, 1) *
        count_trees_from_slope(5, 1) *
        count_trees_from_slope(7, 1) *
        count_trees_from_slope(1, 2)
    )
    
def count_trees_from_slope(right, down):
    f = open(r"C:\Users\User\Desktop\AOC\input\Day3.txt")
    
    right_direction=0
    down_direction=0    
    tree_count = 0
    
    arr = [] 
    for line in f:
        ch_arr = []
        for ch in line:
            ch_arr.append(ch)
        arr.append(ch_arr)
    
    #boundaries
    len_rows = len(arr) #323
    len_cols = len(arr[0]) #32

    while (down_direction < len_rows):        
        
        if right_direction > 30:
            right_direction = right_direction % 31
            
        if arr[down_direction][right_direction] == "#":
            tree_count += 1

        right_direction += right
        down_direction += down
    
    print(tree_count)
    return tree_count
    
main()
