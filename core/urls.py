from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # bu tilda o‘zgartirish uchun
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('About.urls')),
    path('', include('Category.urls')),
    path('', include('Contact.urls')),
    path('', include('Home.urls')),
    path('', include('Register.urls'))
#    path('', views.home, name='home'),
#   path('about/', views.about, name='about'),
)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)