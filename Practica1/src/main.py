from Problem import Problem
from State import State
from Search_Algorithm import Search_Algorithm

import argparse


def main():
    """
    Main method, where the magic is done. This method creates and initializes the original state.
    Then, applying the selected search algorithm, it calculates and it writes the correct solution.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', required=True, type=str, default='DFS',
                        help='Set the search algorithm desired.')
    parser.add_argument('-d', '--depth', default=9, type=int,
                        help='Set the maximum depth.')
    parser.add_argument('-i', '--increase', default=1, type=int,
                        help='Set the increase in each iteration.')
    parser.add_argument('-r', '--random', default=False, type=bool,
                        help='Initial state configuration is randomly generated.')
    parser.add_argument('-f', '--file', default='../terrain.txt', type=str,
                        help='Route to load your initial state configuration.')
    parser.add_argument('-o', '--output', default='successors.txt', type=str,
                        help='File to write the solution.')
    args = parser.parse_args()

    terrain = State(0, 0, 0, 0, 0, 0, 0) # Initial state. Initialized at 0.
    operations = Problem(0, 0, args.file, terrain)

    if args.random:     # Generate the terrain randomly
        operations.generate_terrain(terrain)
    else:
        if operations.file_format_correct():
            operations.read_file(terrain)
        else:
            print("File {} has not a valid format.".format(args.file))
            exit(1)

    # Search algorithm to calculate the solution
    sol = Search_Algorithm().search(operations, args.algorithm, args.depth, args.increase)
    if sol is None:
        print('No se ha encontrado una solución')
    else:
        operations.write_file(sol, args.output)


if __name__ == "__main__":
    main()
