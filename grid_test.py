import curses
import time

class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def 
    

def win_init(stdscr):

    curses.curs_set(0)        # Hide cursor
    curses.noecho()           # Don't show typed keys
    curses.cbreak()           # React instantly to keypressq
    stdscr.keypad(True)       # Enable arrow keys

    curses.start_color()      # Enable colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.nodelay(False)     # Blocking input
    #win.keypad(True)         # Enables keys

    # GET SCREEN SIZE
    height, width = stdscr.getmaxyx()
    # Create smaller window within
    win_height = 20
    win_width = 40
    win = curses.newwin(win_height, win_width, 5, 50)
    win.keypad(True)
    win.box()               # Draw border
    return win, win_height, win_width

def node_init():
    nodes = []
    node1 = Node(3, 4)
    nodes.append(node1)
    return nodes

def main(stdscr):

    #----- Initialize ------#
    win, win_height, win_width = win_init(stdscr)
    nodes = node_init()
    #----- Main Loop -----#
    while True:
        for y in range(1, win_height-1):
            for x in range(1, win_width-1):
                win.addstr(y, x, ".")

        for node in nodes:
            win.addstr(node.y, node.x, "o", curses.color_pair(1))

        stdscr.addstr(3, 3, f"Node count: {len(nodes)}")
        # Refresh both
        stdscr.refresh()
        win.refresh()

        # Get input
        key = win.getch()
        if key == ord('q'):
            break

        win.refresh()

# ----- Start Prog -----#
curses.wrapper(main)
