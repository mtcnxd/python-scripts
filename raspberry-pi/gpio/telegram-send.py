from Services.ProjectService import ProjectService
import telegram_send
import asyncio

counter = 0

main_service = ProjectService()

params = {
    "name":"marcos",
    "apellido":"tzuc",
    "edad":40,
    "curp":"TUCM851227",
    "phone":"9991210161"
}

while counter <= 10:
    current_time = main_service.get_current_time()
    value = main_service.start(counter)
    print(f"{current_time} Hola mundo | counter value: {counter} | value: {value}")
    result = main_service.convert_to_json(params)
    counter = counter +1

    if counter == 2:
        asyncio.run(
            telegram_send.send(
                messages=[f"API Response: ``` {result}```"],
                parse_mode="markdown"
            )
        )
