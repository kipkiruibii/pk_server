from django.contrib import admin
from django.urls import path,include
from pk_server.pk_server_app import urls as appUrls
urlpatterns = [
    path('pk_admin/', admin.site.urls),
    path('/', include(appUrls.urlpatterns)),
]
