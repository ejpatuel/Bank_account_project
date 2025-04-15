import curses

# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(True)

class UserInteraction:
  def __init__(self):
    self.screen = curses.initscr()
    self.screen.clear()
    begin_x = 0; begin_y = 0
    self.win = curses.newwin(curses.LINES - 1, curses.COLS - 1, begin_y, begin_x)

  def get_user_banking_info(self, reentry):
    y_answers = {'yes', 'y', 'yse'}
    n_answers = {'no', 'n'}

    self.win.addstr(1, 1, 'Welcome, I see you are new to our bank, would you like to create a bank account?\n [Y/N]: ')
    self.win.refresh()
    self.win.box()
    self.win.getkey()

ui = UserInteraction()

curses.wrapper(ui.get_user_banking_info(False))


# def main(stdscr):
#   stdscr.clear()
#   begin_x = 0; begin_y = 0
#   win = curses.newwin(curses.LINES - 1, curses.COLS - 1, begin_y, begin_x)


#   win.clear()
#   win.addstr(1, 1, 'Welcome, I see you are new to our bank, would you like to create a bank account?\n [Y/N]: ')
#   win.refresh()
#   win.box()
#   win.getkey()

# curses.wrapper(main)



