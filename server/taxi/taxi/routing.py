from django.urls import path # new under wbsockets 1
from channels.routing import ProtocolTypeRouter, URLRouter # changed under Websockets 1

from taxi.middleware import TokenAuthMiddlewareStack # new under websockets 1
from trips.consumers import TaxiConsumer


application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddlewareStack( # changed under websockets 1
        URLRouter([
            path('taxi/', TaxiConsumer),
        ])
    ),
})