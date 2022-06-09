
def main():
    
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
      
    #PART 1     
    measurements = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            measurements += 1    
    
    print("PART 1")
    print(measurements)

    
    #PART 2   
    q1, q2 = [], []
     
    sum1, sum2, max_capacity, count = 0, 0, 3, 0
    
    for i in range(1, len(lines)):
        
        q1.append(int(lines[i]))
        if len(q1) == max_capacity:
            sum1 = sum(q1)
            q1.pop(0)
  
        q2.append(int(lines[i - 1]))
        if len(q2) == max_capacity:
            sum2 = sum(q2)            
            q2.pop(0)

        if sum2 < sum1:
            count += 1
    
    print("PART 2")
    print(count)


if __name__ == "__main__":
    main()