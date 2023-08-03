
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls',  namespace='registration')),
    path('world/', include('world.urls', namespace='world')),
]
