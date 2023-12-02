from argparse import ArgumentParser
from collections import defaultdict
import re;

inputSet = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def handleLine(line: str):

    game, rest = line.split(":")
    gameId = int(game.split(" ")[-1])

    groups = rest.split(";")

    maxPerColour = defaultdict(lambda: 0)

    for group in groups:
        groupColours = re.findall('(\d+) ((?:red)|(?:green)|(?:blue))', group)
        for count, colour in groupColours:
            count = int(count)
            if maxPerColour[colour] < count:
                maxPerColour[colour] = count
    print(maxPerColour)
    total = 1
    for colour in maxPerColour:
        print(total)
        total *= maxPerColour[colour]

    return total

def main(file: str):
    lines = open(file).readlines()

    count = 0
    for line in lines:
        count += handleLine(line)
    return count

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--source", default="givensample.txt")
    parser.add_argument("--target", type=int)


    args = parser.parse_args()

    res = main(args.source)

    if args.target:
        if args.target != res:
            print(f"failed, got {res} expected {args.target}")
        else:
            print("correct")
    else:
        print("Result:", res)
