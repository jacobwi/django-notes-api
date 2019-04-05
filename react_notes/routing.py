from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notes.routings

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
    URLRouter(
      notes.routings.websocket_urlpatterns
    )
  )
})