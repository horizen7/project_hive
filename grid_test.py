import curses
import time

class Node:

    def __init__(self, path):
        self.path = path
        self.i = 0
        self.next = self.path[0]

    def move(self):
        self.i += 1
        if self.i < len(self.path):
            self.next = self.path[self.i]

def win_init(stdscr):

    curses.curs_set(0)        # Hide cursor
    curses.noecho()           # Don't show typed keys
    curses.cbreak()           # React instantly to keypressq
    stdscr.keypad(True)       # Enable arrow keys

    curses.start_color()      # Enable colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.nodelay(True)     # non-blocking input
    #win.keypad(True)         # Enables keys

    # GET SCREEN SIZE
    height, width = stdscr.getmaxyx()
    # Create smaller window within
    win_height = 20
    win_width = 40
    win = curses.newwin(win_height, win_width, 5, 50)
    win.box()
    stdscr.keypad(True)
    return win, win_height, win_width

def node_init():
    nodes = []
    node1 = Node([(1, 1), (2, 1), (3, 1), (4, 2)])
    nodes.append(node1)
    return nodes

def node_logic():
    '''For each node, call astar to get the tuple of coordinates.
       Have it where future collisions are taken account
       Need to keep track of all positions and whether they will be occupied
       at a certain time, if so astar sees a roadblock and goes around
       Want astar to keep in mind "speed limits" at certain areas for future positions
       new nodes made through udp client message

       Basically node will get the coordinates for where they need to go using astar,
       in the updater() their position is updated to next respective coordinate
       Window is refreshed
       '''

def main(stdscr):

    #----- Initialize ------#

    i = 0
    win, win_height, win_width = win_init(stdscr)
    nodes = node_init()
    #----- Main Loop -----#
    while True:
        
        win.erase()
        win.box()

        for y in range(1, win_height-1):
            for x in range(1, win_width-1):
                win.addstr(y, x, ".")

        for node in nodes:
            win.addstr(node.next[0], node.next[1], "o", curses.color_pair(1))
            node.move()

        stdscr.addstr(3, 3, f"Node count: {len(nodes)}")
        stdscr.addstr(4, 3, f"i = {i}")

        # Refresh both
        stdscr.refresh()
        win.refresh()
        time.sleep(1)

        # kill input
        key = stdscr.getch()
        if key == ord('q'):
            break
        if i == 100:
            i = 0
        else:
            i += 1

# ----- Start Prog -----#
curses.wrapper(main)
