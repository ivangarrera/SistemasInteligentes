import random


class Gui:
    def __init__(self):
        self.__initiated = True

    def choose_one_action(self, possible_actions):
        index = random.randint(0, len(possible_actions) - 1)
        return possible_actions[index]

    def algorithm_is_applicable(self, terrain, ground_desired):
        applicable = False
        for row in terrain:
            for square in row:
                if square != ground_desired:
                    applicable = True
        return applicable



    def algorithm(self, terrain, terrain_obj):
        print("Nothing yet")

def main():
    """try:
        with open("./solution.txt", 'w') as f:
            for step in solving_steps:
                f.write(step+"\n")
    except Exception as ex:
        print(ex.__str__())"""

main()