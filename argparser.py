# Copyright 2014 by Lasse Schuirmann, License: GPL v3

import argparse

def get_args():
    """
    :return: a dict with the cmd args
    """
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__)

    arg_parser.add_argument(nargs=1, metavar='FILE', dest='input',
                            help='File path to parse the graph file from')
    arg_parser.add_argument('-r', '--recursion-level', nargs=1, type=int, metavar='INT', dest='recursion',
                            help='Maximum level of recursion')
    arg_parser.add_argument('-d', '--distance', nargs=2, type=int, metavar='INT', dest='distance',
                            help='Indices from the knots where you want to know the distance')

    return vars(arg_parser.parse_args())
