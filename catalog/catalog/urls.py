from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog_for_music.views import ArtistViewSet, AlbumViewSet, SongViewSet
from drf_yasg.views import get_schema_view as yasg_schema_view
from drf_yasg import openapi
from django.contrib import admin


router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)

schema_view = yasg_schema_view(
   openapi.Info(
      title="Music Catalog API",
      default_version='v1',
      description="API for managing music artists, albums, and songs",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
