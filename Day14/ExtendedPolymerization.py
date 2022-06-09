def main():
    
    map = {}
    
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    
    polymer = lines[0]

    for i in range(2, len(lines)):
        map[lines[i][0:2]] = lines[i][6]
    print(map)
    
    counts = {}
    for j in range(1, len(polymer)):
        #print(polymer[j-1]+polymer[j])
        counts[polymer[j-1]+polymer[j]] = 1
       
    print(counts) 
    for i in range(2):
        print(counts)    
        counts = count_map(counts, map)

    print(counts)
    #all_values = counts.values()
    
    #max_value = max(all_values)
    #min_value = min(all_values)
    
    
    #print(max_value - min_value)

def count_map(counts, map):
        
    keys = counts.keys() 
    for key in keys:
        print(key)
        #print(map[key])
        new_pair=map[key]+key[1]
        print(new_pair)
        if new_pair in counts:
            counts[new_pair]=counts[new_pair]+1
        else:
            counts[new_pair]=1
    return counts 


if __name__ == "__main__":
    main()
