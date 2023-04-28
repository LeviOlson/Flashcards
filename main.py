from deckSelector import deck_selector
import tkinter
from os import startfile, getcwd
import time
ds = deck_selector()

closings = []
def show_back(label, flip_btn, next_btn, got_it_btn, g):
    label.configure(text = g.get_back())
    flip_btn.grid_forget()
    next_btn.grid()
    got_it_btn.grid()

def got_it(window, g):
    if g.is_complete():
        return
    g.remove_card()
    if g.is_complete():
        l = tkinter.Label(window, text = "You got them all!")
        l.grid(row = 4, column = 0)
        close(window)

def close(window):
    closings.append((window, time.time() + 3))
    main_window.after(1000, lambda : window.destroy())

def next_card(back_label, front_label, next_btn, flip_btn, got_it_btn, g):
    if g.is_complete():
        return
    else:
        g.go_to_next()
        back_label.configure(text = "")
        front_label.configure(text = g.get_front())
        next_btn.grid_forget()
        got_it_btn.grid_forget()
        flip_btn.grid()


def open_deck_window(g):
    game_window = tkinter.Tk()

    front_label = tkinter.Label(game_window, text = g.get_front())
    back_label = tkinter.Label(game_window, text = "")
    front_label.grid(row = 0, column = 0)
    back_label.grid(row = 1, column = 0)

    flip_btn = tkinter.Button(game_window, text = "continue")
    got_it_btn = tkinter.Button(game_window, text = "Got it", command = lambda: got_it(game_window, g))
    next_btn = tkinter.Button(game_window, text = "next", command= lambda : next_card(back_label, front_label, next_btn, flip_btn, got_it_btn, g))
    flip_btn.configure(command = lambda: show_back(back_label, flip_btn, next_btn, got_it_btn, g))

    flip_btn.grid(row = 3, column = 1)


def open_file(path):
    print(path)
    startfile(path)

def trim_name(s):
    return s.replace(".csv", '')

if __name__ == '__main__':
    decks = ds.get_decks()
    paths = ds.get_paths()
    print(decks)
    print(paths)
    main_window = tkinter.Tk()

    help_btn = tkinter.Button(main_window, text = "help", command= lambda: open_file(getcwd() + "\\readme.txt"))
    help_btn.grid(row = 0, column = 0)

    for x in range(len(decks)):
        label = tkinter.Label(main_window, text = trim_name(decks[x]))
        label.grid(row = x + 1, column = 0)
        open_btn = tkinter.Button(main_window, text = "open deck",
                                  command = lambda y = x: open_deck_window(ds.get_game(y)))
        print("made button " + str(x) + " " + decks[x])
        open_btn.grid(row = x + 1, column = 1)

        edit_btn = tkinter.Button(main_window, text = "edit deck", command = lambda y = x: open_file(paths[y]))
        print("made button " + str(x) + " " + paths[x])
        edit_btn.grid(row = x + 1, column = 2)

    main_window.mainloop()