import sys
from string import Template


def pairs_finder(addends_list: list, target: int) -> list:
    """This function finds pairs of integers from a list that sum to a given value
    Args:
        addends_list: the values to pair
        target: the result for the sum pairs
    Returns:
        A list of tuples with pairs of integers
    """

    # create a sort list by using tims sort algorithm O(log n)
    addends_list_sorted = sorted(addends_list)
    addends = []
    add_pair = addends.append
    # loop thorough ordered list and find pairs
    for n in addends_list_sorted:
        # find out if a pair number exists for n in list and
        # since list is ordered, the last number must be greater than pair.
        # if it is not, then is possible to discard it, and move to the previous one
        pair = target - n
        while  len(addends_list_sorted) > 1 and addends_list_sorted[-1] > pair:
            addends_list_sorted.pop()
        else:
            if pair == addends_list_sorted[-1] and pair != n: # avoid adding the same number
                add_pair((n, pair))
                addends_list_sorted.pop()
    return addends


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(f"Usage: python3 find_pairs <list of unique numbers"
                         f" separated by commas> <target number>")
    # some validations provided even though redundant by assumptions
    row_list = sys.argv[1].strip(',').split(',')
    try:
        input_list = [int(n_string) for n_string in row_list]
    except ValueError:
        raise SystemExit(f"'{sys.argv[1]}' contains not valid elements. "
                         f"Argument should be composed of numbers separated by commas")
    try:
        target = int(sys.argv[2])
    except ValueError:
        raise SystemExit(f"'{sys.argv[2]}' is not a valid argument, it must be an integer")

    pairs = pairs_finder(input_list, target)
    template_output = Template('\t $index)  $pair1, $pair2')

    # print output
    pairs_qty = len(pairs)
    if not pairs_qty:
        print(f'There are no pairs of numbers that sum to "{target}"'
              f' in the list: {input_list}')
    else:
        print(f'the pair{"s" if pairs_qty > 1 else ""} of numbers that sum to'
              f' "{target}" from the list: {input_list} {"are" if pairs_qty > 1 else "is"}:')

    for index, pair in enumerate(pairs, start=1):
        print(template_output.substitute(index=index, pair1=pair[0], pair2=pair[1]))