import argparse


def is_invalid_two(num: str) -> bool:
    """
    Same as is_invalid except for puzzle 2
    """
    length = len(num)
    fish = False
    for i in range(1, length):
        if length % i == 0:
            ref = num[:i]
            fish = True
            for n in range((length // i)):
                if ref != num[n*i:i*n+i]:
                    fish = False
            if fish:
                return True
    return fish


def is_invalid(num: str) -> bool:
    """
    Determines whether a number is valid or not, AKA has repeating digits
    Args:
        num str: The number we are checking
    returns:
        bool: Whether the string is valid or not
    """
    length = len(num)
    if num[:length//2] == num[length//2:]:
        return True
    else:
        return False


def num_range(numberange: str) -> list[str]:
    """
    Converts a string "num-num" to a list of numbers from num_1 to num_2
    Args:
    numberange str: "11-32"
    returns:
        list[str]: All numbers in string form in the range
    """
    limits = numberange.split("-")
    lower = limits[0]
    higher = limits[1]
    retlist = []
    for num in range(int(lower), int(higher)+1):
        retlist.append(str(num))
    return retlist


def sum_invalids(puzzle_input: str) -> int:
    """
    Answer to the Advent of Code day 2 puzzle
    args: 
        puzzle_input str: "11-32,33-43"
    returns:
        int: the sum of all the invalid numbers
    """
    ranges = puzzle_input.split(",")
    retval = 0
    for ran in ranges:
        for num in num_range(ran):
            if is_invalid(num):
                retval += int(num)

    return retval

def sum_invalids_two(puzzle_input: str) -> int:
    """
    Answer to the Advent of Code day 2 puzzle
    args: 
        puzzle_input str: "11-32,33-43"
    returns:
        int: the sum of all the invalid numbers
    """
    ranges = puzzle_input.split(",")
    retval = 0
    for ran in ranges:
        for num in num_range(ran):
            if is_invalid_two(num):
                retval += int(num)

    return retval
def main():

    puzzle_in = args.input
    if args.fun == "2":
        print(sum_invalids_two(puzzle_in))
    else:
        print("Starting with: ", puzzle_in)
        print("Your answer is ", sum_invalids(puzzle_in))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--fun")
    args = parser.parse_args()
    main()
