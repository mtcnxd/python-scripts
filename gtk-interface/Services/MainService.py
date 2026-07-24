from .ApiService import ApiService

class MainService:
    def __init__(self):
        self.api_service = ApiService()
        
    def get_check_domain(self, button):
        try:
            response = self.api_service.get("api/index.php", {
                "command": "getCheckDomain",
                "domain": "ecoflamme.de"
            })
        except Exeption as error:
            return None

    def on_button_clicked(self, button):
        try:        
            response = self.api_service.get("api/index.php",{
                "command": "domainInfo",
                "domain": "ecoflamme.de"
            })

            return response

        except Exception as e:
            print(e)
            return None

    def on_switch_changed(self, switch, gparam):
        if switch.get_active():
            print("Switch ON")
        else:
            print("Switch OFF")