import _curses

window = _curses.initscr()
window.getch()
_curses.endwin()