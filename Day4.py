import re

def main():
    f = open(r"/Users/monicasieklucki/Desktop/advent-of-code/input/Day4.txt")
    lines = f.readlines()
    
    part1_count = 0
    part2_count = 0

    passports = []
    passport = {}
    
    # get passport
    for line in lines:
        print(line)
        if line != '\n':
            line = line.rstrip().split()
            line = [field.split(':') for field in line]
            
            for field in line:
                passport[field[0]] = field[1]

            print(line)
        else:
            passports.append(passport)
            passport = {}

    f.close()

    print(passports)
    
    #Part 1
    for p in passports:
        if len(p) == 8 or len(p) == 7 and 'cid' not in p: 
            part1_count += 1
            
    #Part 2
    for p in passports:
        
        print(p)
        if len(p) == 8 or len(p) == 7 and 'cid' not in p:
            if ((len(p['byr']) == 4 and int(p['byr']) >= 1920 and int(p['byr']) <= 2002)) and ((len(p['iyr']) == 4 and int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020)) and ((len(p['eyr']) == 4 and int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030)) and ((p['hgt'][-2:] == "cm" and int(p['hgt'][:-2]) >= 150 and int(p['hgt'][:-2]) <= 193) or ((p['hgt'][-2:] == "in" and int(p['hgt'][:-2]) >= 59 and int(p['hgt'][:-2]) <= 76)) and (len(p['pid']) == 9 and p['pid'].isdigit())  and (re.match("^#[a-f0-9]{6}", p['hcl'])) and (p['ecl'] == 'amb' or p['ecl'] == 'blu' or p['ecl'] == 'brn' or p['ecl'] == 'gry' or p['ecl'] == 'grn' or p['ecl'] == 'hzl' or p['ecl'] == 'oth')):
                part2_count += 1
                
        

    print(part1_count)
    print(part2_count)
  
main()