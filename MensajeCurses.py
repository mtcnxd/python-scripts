import curses
import time
import requests

def get_status_investment() -> dict | None:
    url = 'https://mecanicarubio.com/api/investments/total'
    response = None
    response = requests.get(url)

    if response is not None:
        return response.json()
    else:
        return None

def mostrar_clima(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    curses.start_color()
    
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    data = get_status_investment()

    while True:
        if data is not None:
            for item in data['items']:
                stdscr.clear()
                stdscr.addstr(1, 0, f"ID: {item['id']}", curses.color_pair(1))
                stdscr.addstr(1, 20, f"Name: {item['name']}", curses.color_pair(4))
                stdscr.addstr(1, 50, f"Last amount: {item['last_amount']}", curses.color_pair(2))
                stdscr.addstr(1, 80, f"Current amount: {item['current_amount']}", curses.color_pair(3))
                stdscr.refresh()
                time.sleep(2)

# Main code start here

curses.wrapper(mostrar_clima)
