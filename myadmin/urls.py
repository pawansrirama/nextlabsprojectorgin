from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('',views.admin_login,name='admin_login'),
path('loginauth/',views.admin_page,name='admin_page'),
path('invalidcredentials/',views.invaild_log,name='invaild_log'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
