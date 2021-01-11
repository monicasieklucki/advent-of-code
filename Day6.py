
def main():

    count = 0
    total_count = 0
    
    part2_count = 0
    part2_total_count = 0
    
    answers = []
    
    each_answer = []
    person_count = 0
        
    with open(r"/Users/monicasieklucki/Desktop/advent-of-code/input/Day6.txt") as file:
        
        lines = file.readlines()
        lines.append('\n')
        
        for field in lines:
            each_answer.append(field)
            if field != '\n':
                field = field.rstrip()
                for ch in field:
                    if ch not in answers:
                        answers.append(ch)
                        count+=1
            else:                
                questions = []
                #print(answers)
                total_count += count
              
                answers = []
                each_answer = []
                count = 0
          
    print("Part 1: " + str(total_count))
    print("Part 2: " + str(part2_total_count))
    
with open("/Users/monicasieklucki/Desktop/advent-of-code/input/Day6.txt") as f:
    input = f.read().strip().split('\n\n')

def yes_answers(input, fcn):
    for group in input:
        yield len(fcn(*(set(s) for s in group)))

input = [line.split() for line in input]

print("Part 1:", sum(yes_answers(input, set.union)))

print("Part 2:", sum(yes_answers(input, set.intersection)))

main()

