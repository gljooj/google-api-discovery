import abc
from typing import Dict


class ContextAPI:
    url: str

    @abc.abstractmethod
    def authentication(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def do_post(self, request):
        raise NotImplemented

    @abc.abstractmethod
    def do_get(self, request):
        raise NotImplemented

    @staticmethod
    def parser(response):
        return response.json()

    def post(self, request) -> Dict:
        response = self.do_post(request)

        if response.status_code not in [200, 201]:
            raise Exception(f'{response.text} -- {response.status_code}')

        data = self.parser(response)
        return data

    def get(self, request) -> Dict:
        response = self.do_get(request)
        if response.status_code != 200:
            raise Exception(f'{response.text} -- {response.status_code}')

        data = self.parser(response)
        return data
