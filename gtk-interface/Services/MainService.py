from .ApiService import ApiService
from .DataBaseLite import DataBaseLite
from gi.repository import GLib
import threading

class MainService:
    def __init__(self):
        self.api_service = ApiService()
        self.database = DataBaseLite()
        
    def get_check_domain(self, button):
        try:
            response = self.api_service.get("api/index.php", {
                "command": "getCheckDomain",
                "domain": "ecoflamme.de"
            })
        except Exception as error:
            print(error)
            return None

    def get_domain_info(self, domain_name, callback):
        def thread_target():
            try:
                response = self.api_service.get("api/index.php",{
                    "command": "domainInfo",
                    "domain": domain_name
                })

                GLib.idle_add(callback, response)

            except Exception as e:
                print(f"ERROR: {e}")
                GLib.idle_add(callback, None)

        threading.Thread(target=thread_target, daemon=True).start()

    def on_switch_changed(self, switch, gparam):
        if switch.get_active():
            print("Switch ON")
        else:
            print("Switch OFF")