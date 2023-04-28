import os
from game import game


class deck_selector:
    path = os.getcwd() + "\\decks\\"

    def trim_name(self, s):
        s = s.replace('[', '')
        s = s.replace(']', '')
        return s

    def __init__(self):
        self.decks = []
        for file in os.listdir(self.path):
            # check only text files
            if file.endswith('.csv'):
                self.decks.append(self.trim_name(file))

    def get_decks(self):
        return self.decks

    def get_paths(self):
        paths = []
        for x in range(len(self.decks)):
            paths.append(self.path + self.decks[x])
        return paths

    def get_game(self, index):
        g = game(self.path + self.decks[index])
        return g
