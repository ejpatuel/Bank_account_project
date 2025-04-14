import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

def main(stdscr):
  stdscr.clear()
  begin_x = 0; begin_y = 0
  height = 5; width = 40
  win = curses.newwin(curses.LINES - 1, curses.COLS - 1, begin_y, begin_x)


  win.clear()
  win.addstr(1, 1, 'Welcome, I see you are new to our bank, would you like to create a bank account?\n [Y/N]: ')
  win.refresh()
  win.box()
  win.getkey()

curses.wrapper(main)

# def main(stdscr):
#     curses.curs_set(0)  # Hide cursor
#     stdscr.clear()
#     stdscr.addstr(0, 0, "Hello")
#     stdscr.refresh()
#     stdscr.getch()  # Wait for key press

# curses.wrapper(main)



