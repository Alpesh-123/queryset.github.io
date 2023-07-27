from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]

urlpatterns += staticfiles_urlpatterns()
