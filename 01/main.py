from argparse import ArgumentParser
import re

words = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

captureGroup = '(\d|(?:' + ")|(?:".join(words.keys()) + '))'


def unpackCap(capture: re.Match, line: str):
    if (not capture):
        raise Exception(f"Capture not found: {line}")

    return capture.group(1)

def main(source: str):
    lines = open(source).readlines()

    total = 0
    for line in lines:
        line = line.strip()
        first = unpackCap(re.match(f'^.*?{captureGroup}', line), line)
        last = unpackCap(re.match(f'^.*{captureGroup}.*?$', line), line)

        if len(first) > 1:
            first = words[first]

        if len(last) > 1:
            last = words[last]

        total += int(first+last)

    return total

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("source", default="givensample.txt")
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