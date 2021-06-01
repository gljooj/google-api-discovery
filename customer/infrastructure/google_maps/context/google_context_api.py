from customer.context.context_api import ContextAPI
import requests


class GoogleContextAPI(ContextAPI):
    def __init__(self):
        self.base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        self.token = ''
        self.params = {'key': self.authentication()}

    def authentication(self) -> str:
        return 'AIzaSyDc7QuWmkb6PcJFuYKySnj6KbW3B0Y4Tfc'

    def __bind_params(self, request):
        return self.params.update(request.payload)

    def do_post(self, request):
        pass

    def do_get(self, request):
        self.__bind_params(request)
        return requests.get(url=self.base_url, params=self.params,verify=False)
