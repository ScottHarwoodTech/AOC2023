from argparse import ArgumentParser
import re

def main(source: str):
    lines = open(source).readlines()

    total = 0
    for line in lines:
        line = line.strip()
        first = re.match(r'^.*?(\d)', line)
        last = re.match(r'^.*?(\d)', line[::-1])

        total += int(first.group(1)+last.group(1))

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
        print("Result:", res)