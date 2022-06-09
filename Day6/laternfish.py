def main():  
    # opening file and reading lines
    with open('input.txt') as f:
        lines = f.readlines()
        
    initial_state = lines[0].split(',')
    print(initial_state)
    
    dict = {}   
    
    # initialize dictionary with 0 for all possible values
    for i in range(0, 9):
        dict[str(i)] = 0

    # load initial states into dictionary
    for i in initial_state:
        if i in dict.keys():
            dict[i] = dict[i] + 1            
        else:
            dict[i] = 1

    #print(dict)
    
    # this is only from the initial to after day 1
    
    # iterate over a few days
    # PART 1 - after 80 days
    # PART II - after 256 days
    for i in range(1, 257):
        print(f"After {i} day: ")
        valueAt0 = dict['0']
        prev = dict['8']
        for k,v in reversed(dict.items()):
            # current key, value pair
            #print("key", "current value")
            #print(k, v)
            
            # update dictionary here
            if k == '8':
                #print("is 8")
                dict[k] = valueAt0
            else:
                dict[k] = prev
                
            # previous value
            #print(f"Prev before changing it to the current value = {prev}")
            prev = v
            #print(f"Prev after changing it to the current value = {prev}")
    
            #print()        
            
        # after 1 day passed
        dict['6'] = dict['6'] + valueAt0
        print(dict)
        #print(f"Value with Key 0 = {valueAt0}")
        # store the value at key = 0
    
    total_fish = 0
    for v in dict.values():
        total_fish += v
    print(total_fish)

if __name__ == "__main__":
    main()