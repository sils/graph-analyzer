#! /bin/python3
from argparser import get_args
import sys
from graph import RawGraph

__author__ = 'lasse'

if __name__ == "__main__":
    args = get_args()
    val = args.get('input')
    if val is None:
        file = input("Please enter the graph file to process: ")
    else:
        file = val[0]

    val = args.get('recursion')
    if val is not None:
        print("Setting recursion level to", val[0])
        sys.setrecursionlimit(val[0])
    else:
        sys.setrecursionlimit(10000)

    val = args.get('distance')
    if val is None:
        # yes, I'm too lazy to invoke it here automatically
        print("Use --help argument for usage information.")
        exit(1)
    graph = RawGraph()
    graph.from_file(file)
    print("The maximum degree is {}.".format(graph.maximum_degree()))
    connected_components = graph.get_connected_components()
    print("There are {} connected components.".format(len(connected_components)))
    max_size = 0
    for elem in connected_components:
        max_size = max(max_size, len(elem))
    print("The maximum size of a component is {}.".format(max_size))

    print("The minimal distance of knot {} and {} is {}.".format(val[0], val[1],
                                                                 graph.get_distance(val[0], val[1], connected_components)))
    if graph.is_two_colorizable(connected_components):
        print("You can colorize this graph with only two colors! Happy birthday!")
    else:
        print("Sorry. You cannot colorize this graph with only two colors!")
