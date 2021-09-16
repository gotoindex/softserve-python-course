import argparse
import math


class Sequence:
    """Displays all natural numbers whose square is less than n.\n
    Any negative inputs will be converted into positive ones.
    ### Params:
    - n - a positive integer. The square of each number in 
    the result will be smaller than this number.
    """

    def __init__(self, n):
        self.max = math.ceil(math.sqrt(abs(n)))
    
    def show(self):
        print(', '.join(tuple(str(i) for i in range(1, self.max))))


parser = argparse.ArgumentParser(description='Display all natural numbers \
                                              whose square is less than n.')
parser.add_argument('n', type=int,
                    help='a positive integer. The square of each number in \
                          the result will be smaller than this number')
args = parser.parse_args()
Sequence(args.n)
