  
def main():
    
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
      
    #print(lines[0])
    
    hexadecimal = lines[0]
    print(hexadecimal)
    #decode message from hexadecimal into binary
    
    #single packet at outermost layer -> cotains more packets
    
    #first 3 its encode packet version (Num)
    #next 3 bits encode the packet typeID (Num)
    
    #focus on parsing the hierarchy of sub-packets
    
    
    
      

if __name__ == "__main__":
    main()