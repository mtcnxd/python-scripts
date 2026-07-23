from services import BoardService

board_service = BoardService()

try:
    timer = 1
    while timer <= 25:
        print(f"Blinking: {timer}")
        timer = timer + 1
        board_service.blink()

except Exception as error:
    print(f"An error ocurred: {error}")

finally:
    board_service.cleanup()
