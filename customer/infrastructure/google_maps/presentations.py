from typing import Dict


class GeoLocationGetRequest:
    def __init__(self, id_customer, city):
        self.id = id_customer
        self.city = city

    @property
    def payload(self):
        return {'address': self.city}


class GeoLocationGetResponse:
    def __init__(self, payload: Dict):
        self.id = payload.get("id")
        self.payload = payload.get('result', '').get('results', '')[0]['geometry']['location'] \
            if len(payload.get('result', '').get('results', '')) > 0 else {}

    @property
    def latitude(self):
        return self.payload.get("lat", "")

    @property
    def longitude(self):
        return self.payload.get("lng", "")
