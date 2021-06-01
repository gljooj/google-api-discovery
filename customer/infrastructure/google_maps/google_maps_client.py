from customer.infrastructure.google_maps.context.google_context_api import GoogleContextAPI
from customer.infrastructure.google_maps.presentations import GeoLocationGetRequest, GeoLocationGetResponse


class GoogleMapsClient:
    def __init__(self):
        self.context = GoogleContextAPI()

    def get_geo_location(self, payload: [GeoLocationGetRequest]) -> [GeoLocationGetResponse]:
        request = list(map(lambda p: GeoLocationGetRequest(p['id'], p['city']), payload))
        data = []
        for r in request:
            data.append({"id": r.id, "result": self.context.get(r)})
        return list(map(lambda d: GeoLocationGetResponse(d), data))
