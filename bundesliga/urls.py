from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bundesliga_app', include('bundesliga_app.urls')),
    url(r'', include('bundesliga_app.urls'))
]
