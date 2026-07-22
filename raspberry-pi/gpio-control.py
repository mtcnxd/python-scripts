from services import BoardService

board_service = BoardService()

try:
	while timer < 10:
		print(f"Counter: {timer}")
		timer = timer + 1
		board_service.blink()

except Exception as error:
	print(f"An error ocurred: {error}")
