
def main():
    
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        
        
    # PART 1
    
    x, y, aim = 0, 0, 0

    for line in lines:
        direction_distance = line.split(" ")
        
        if direction_distance[0] == "forward":
            x += int(direction_distance[1])
            y += (aim * int(direction_distance[1]))
        elif direction_distance[0] == "down":
            aim += int(direction_distance[1])
        elif direction_distance[0] == "up":
            aim -= int(direction_distance[1])
    print(x)
    print(y)
    print(x * y)
if __name__ == "__main__":
    main()