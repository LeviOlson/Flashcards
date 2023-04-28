import card
import csv

class game:

    def __init__(self, deck_file_path, card_index=0):
        # the deck of cards
        self.deck = []
        # what card the user is at
        self.card_index = 0
        # how many cards have been removed
        self.cards_removed = 0
        # how many cards remain
        self.cards_left = 0
        self.load_deck(deck_file_path)
        self.card_index = card_index

    def get_front(self):
        return self.deck[self.card_index].get_front()

    def get_back(self):
        return self.deck[self.card_index].get_back()

    def is_complete(self):
        return len(self.deck) == 0

    def go_to_next(self):
        self.card_index += 1
        if self.card_index >= len(self.deck):
            self.card_index = 0
        return self.is_complete()

    def remove_card(self, index=None):
        if index is None:
            index = self.card_index

        del self.deck[index]
        self.cards_removed += 1
        self.cards_left = len(self.deck)
        return self.go_to_next()

    def load_deck(self, file_path):
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    c = card.card(row[0], row[1])
                    self.deck.append(c)

                    line_count += 1
