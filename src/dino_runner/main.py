import curses


def init_window() -> curses.window:
    _ = curses.initscr()
    curses.noecho()
    curses.cbreak()
    _ = curses.curs_set(0)
    return curses.newwin(24, 80, 0, 0)


def handle_input(window: curses.window) -> None:
    window.addstr(4, 4, "hello world, press [SPACE] to exit")
    curses.halfdelay(1)
    inp = 0
    while inp != 32:
        inp = window.getch()


def cleanup():
    curses.nocbreak()
    curses.echo()
    _ = curses.curs_set(1)
    curses.endwin()


def run() -> None:
    game_window = init_window()

    try:
        handle_input(game_window)
    finally:
        cleanup()
