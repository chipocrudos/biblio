from rest_framework.routers import DefaultRouter

from .views.book import BookViewSet
from .views.bookitem import BookItemViewset
from .views.library import LibraryViewSet
from .views.rack import RackViewSet

router_library = DefaultRouter()
router_library.register(
    prefix='library',
    basename='library',
    viewset=LibraryViewSet
)

router_library.register(
    prefix='rack',
    basename='rack',
    viewset=RackViewSet
)

router_library.register(
    prefix='book',
    basename='book',
    viewset=BookViewSet
)

router_library.register(
    prefix='bookitem',
    basename='bookitem',
    viewset=BookItemViewset
)


urlpatterns = router_library.urls
