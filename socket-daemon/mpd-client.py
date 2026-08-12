from classes.MPDClient import MPDClient
import time

mpd = MPDClient('uconsole.local', 6600)

def ticks_ms():
    return time.monotonic_ns()

# Main code

interval = 1000
last_millis = 0

try:
    mpd.connect()

    while True:
        current_millis = ticks_ms()
        result = (current_millis - last_millis) / 1_000_000
        
        if result > interval:
            last_millis = current_millis

            current_status = mpd.get_status()
            is_playing = current_status.get('state')

            print(f"Estado:  {current_status.get('state')}")
            print(f"Tiempo:  {current_status.get('elapsed')} / {current_status.get('duration')}")

            song = mpd.get_track_info()
            print(f"Artista: {song.get('Artist', 'Desconocido')}")
            print(f"Album:   {song.get('Album', 'Desconocido')}")
            print(f"Titulo:  {song.get('Title', 'Desconocido')}")
            print("="*30)

            if is_playing == 'play':
                mpd.toggle_play_pause('pause')
            
            if is_playing == 'pause':
                mpd.toggle_play_pause('play')

except Exception as error:
    print(f"MPD Client error: {error}")
