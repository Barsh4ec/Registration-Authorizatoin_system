from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='index'),
    path('user/', include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
