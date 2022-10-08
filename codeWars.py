"""
DESCRIPTION:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def splitNumberAppend(number: int) -> tuple[int, ...]:
    result = []
    for digit in str(number):
        result.append(int(digit))
    return tuple(result)


@profile
def splitNumberTuple(number: int) -> tuple[int, ...]:
    result = tuple()
    for digit in str(number):
        result += (int(digit),)
    return result


def splitNumberComprehension(number: int) -> tuple[int, ...]:
    return tuple(int(i) for i in str(number))


def digitalRoot(number: int) -> int:
    # split number into individual digit
    digits = splitNumberTuple(number)
    # add all digits together
    sum_digits = sum(digits)
    # split summation of all digits
    split_sum_digits = splitNumberTuple(sum_digits)
    # if number is make up of 1 digits
    if len(split_sum_digits) == 1:
        return split_sum_digits[0]
    # else sum all the split digits and pass to digital Root
    else:
        new_number = sum(split_sum_digits)
        return digitalRoot(new_number)


if __name__ == '__main__':
    import random
    for i in range(1000000):
        result = digitalRoot(random.randint(100, 10_000_000))