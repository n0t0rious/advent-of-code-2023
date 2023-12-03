test_input =[ '1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']

def main():
    with open('input.txt') as f:
        data = [i for i in f.read().strip().split("\n")]
    print(f'Part 1: {part_1(data)} Part 2: {part_2(data)}')

def part_1(inp):
    
    total = 0
    for line in inp:
        r = 0
        l = len(line) -1 

        while line[r].isalpha():
            r += 1
        while line[l].isalpha():
            l -= 1
        curr = int(line[r] + line[l])
        total += curr

    return total

def part_2(inp):
    numbers = ["one", "two", "three","four","five","six","seven","eight","nine"]
    total = 0
    for line in inp:
        first = 0
        last = 0
        found = False

        r = 0
        while r < len(line) and not found:
            if line[r].isdigit():
                first = int(line[r])
                break

            for x in range(len(numbers)):
                if line[r:].startswith(numbers[x]):
                    found = True
                    first = x + 1
                    break
            r += 1
        found = False

        l = len(line) - 1
        while l >= 0 and not found:
            if line[l].isdigit():
                last = int(line[l])
                break
            for x in range(len(numbers)):
                if line[:l+1].endswith(numbers[x]):
                    found = True
                    last = x + 1
                    break
            l -= 1
        total += (first * 10) + last

    return total
    

if __name__ == '__main__':
    main()


