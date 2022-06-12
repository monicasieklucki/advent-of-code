def main():  
    # opening file and reading lines
    with open('input.txt') as f:
        lines = f.readlines()
        
    initial_state = [int(i) for i in lines[0].split(',')]
    print(initial_state)

    print(min(initial_state))    
    print(max(initial_state))
    
    print("PART I")
    dict = {}
    for pos in range(min(initial_state), max(initial_state)+1):
        fuel = 0
        for i in initial_state:
            fuel += abs(i - pos)
        #print(f"Fuel used: {fuel}")
        dict[pos] = fuel
            
    print(dict)
    print("Minimum fuel used: ")
    print(min(dict.values()))
        
    print("PART II")
    # very slow brute force solution
    dict2 = {}
    for pos in range(min(initial_state), max(initial_state)+1):
        #print(f"Position is {pos}")
        total_fuel = 0
        
        for curr_state in initial_state:
            # getting total fuel for each potential horzontal position
            fuel = 0
            step = 0
            
            #print(f"Current state is {curr_state}")
            # this is getting linear distance - quick
            #print("Linear distance: " + str(abs(curr_state - pos)))
            
            # I need to get the exponential increase
            # I can't figure out how to do it any faster - slow and naive solution
            #for i in range(min([curr_state, pos]), max([curr_state, pos])+1):
            #    print(i)
            #    fuel+=step
            #    step = step + 1
            
            # I looked up the solutions
            # Use triangular number
            # https://en.wikipedia.org/wiki/Triangular_number#Formula
            n = max([curr_state, pos]) - min([curr_state, pos])
            fuel = n * (n + 1) // 2
            #print(max([curr_state, pos])+1*(max([curr_state, pos])+1) // 2)
            #fuel = (max([curr_state, pos])*(max([curr_state, pos])+1)) // 2
                  
            total_fuel += fuel
        dict2[pos] = total_fuel           

    print("Minimum fuel used: ")
    print(dict2)
    print(min(dict2.values())) 
    
if __name__ == "__main__":
    main()