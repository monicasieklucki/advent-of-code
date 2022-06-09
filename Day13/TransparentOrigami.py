def main():
    
    fold1 = []
      
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    #print(lines[-2])    
    #print(lines[-1])
    
    #fold1_y = int(lines[-2][-1])
    #fold2_x = int(lines[-1][-1])
    for line in lines:
        if line == "":
            print(line)
            
    
    
    #print(fold1_y)
    #print(fold2_x)
    
    #for line in lines:
    #    print(line)
    #    if line == '':
    #        break
    #    xy = line.split(',')
    #    if int(xy[1]) > 7:
            #print(int(xy[1]) - fold1_y)
    #        mirror = int(xy[1]) - fold1_y
    #        print(int(xy[1]) - fold1_y)
    #        if not (int(xy[0]),int(fold1_y) - mirror) in fold1:
    #            fold1.append((int(xy[0]),int(fold1_y) - mirror))
    #    else:
    #        if not (int(xy[0]),int(xy[1])) in fold1:
    #            fold1.append((int(xy[0]),int(xy[1])))
    #        continue
        #print(xy[0])
        #print(xy[1])
        
    #print(fold1)
    #print(len(fold1))
    #835 dots is too high
    
if __name__ == "__main__":
    main()