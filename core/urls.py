
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.hosaik.urls')),
    path('blog/', include('apps.blog.urls')),
    path('honey', include('apps.honey.urls')),
    path('users/', include('apps.users.urls')),

]
