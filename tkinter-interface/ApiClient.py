import requests
from requests.exceptions import RequestException, Timeout

class ApiClient:
    def __init__(self, timeout=5):
        self.url = "https://mecanicarubio.com/api"
        self.timeout = timeout

    def _get(self, endpoint):
        response = requests.get(self.url + endpoint, timeout=self.timeout)

        if not response:
            raise Exception("No se pudo obtener la respuesta")

        response.raise_for_status()
        return response.json()

    def getAllClients(self):
        return self._get("/clients/all")

    def getClientInfo(self, client_id):
        return self._get(f"/clients/info/{client_id}")

    def getClientServices(self, client_id):
        return self._get(f"/clients/services/{client_id}")

    def getServiceInfo(self, service_id):
        return self._get(f"/services/info/{service_id}")