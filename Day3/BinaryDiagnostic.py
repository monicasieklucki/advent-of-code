
def main():
    
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
      
    #print(lines)
    
    gamma = ""
    epsilon = ""
    
    #PART 1
    for i in range(0, len(lines[0])):
        zero_count = 0
        one_count = 0

        for binary in lines:
            if binary[i] == "0":
                zero_count += 1
            else:
                one_count += 1
        
        if zero_count > one_count:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print("PART I")
    #print(int(gamma, 2))
    #print(int(epsilon, 2))
    print(int(gamma, 2) * int(epsilon, 2))
    
    
    #PART 2
    print("PART II")
    oxy_rating = 0
    co2_rating = 0
    
    index = 0
    mutable_list = sorted(lines)

    for i in range(0, len(lines[0])):
        #print(f'i in range: {i}')
        
        zero_count = 0
        one_count = 0
        #count occurrences
        for binary in mutable_list:
            if binary[i] == "0":
                zero_count += 1
            else:
                one_count += 1
        #print(f'Zero count is {zero_count}')
        #print(f'One count is {one_count}')        
        
        #print(mutable_list)
        
        # oxygen generator rating
        for line in lines:
            if len(mutable_list) == 0:
                break
            
            if line in mutable_list:
                #print(line)
                if zero_count > one_count:
                    if line[index] == "1":
                        mutable_list.remove(line)
                if one_count >= zero_count:
                    if line[index] == "0":
                        mutable_list.remove(line)            
            #if one_count > zero_count:
        #print(mutable_list)
        oxy_rating = mutable_list[0]
        index += 1
       
    # redundant code. 
    #  create function for getting the oxygen and co2 rating
    index = 0
    mutable_list = sorted(lines)
    for i in range(0, len(lines[0])):
        #print(f'i in range: {i}')
        
        zero_count = 0
        one_count = 0
        #count occurrences
        for binary in mutable_list:
            if binary[i] == "0":
                zero_count += 1
            else:
                one_count += 1
        #print(f'Zero count is {zero_count}')
        #print(f'One count is {one_count}') 
        
        # co2 scrubber rating
        for line in lines:
            if len(mutable_list) == 1:
                break
            
            if line in mutable_list:
                #print(line)
                if zero_count > one_count:
                    if line[index] == "0":
                        mutable_list.remove(line)
                if one_count >= zero_count:
                    if line[index] == "1":
                        mutable_list.remove(line)            
            #if one_count > zero_count:
        #print(mutable_list)
        co2_rating = mutable_list[0]
        index += 1
         
    print(f"Oxygen generator rating is {oxy_rating}")
    print(f"CO2 scrubber rating is {co2_rating}")

    #print(int(oxy_rating, 2))
    #print(int(co2_rating, 2))
    print(int(oxy_rating, 2) * int(co2_rating, 2))
    
if __name__ == "__main__":
    main()