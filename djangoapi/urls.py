
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from players import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    
	openapi.Info(
        title='Soccer API By Ifiok Ambrose',
        default_version='v1',
        description='This is A RestFul API to get Create, Retrieve, Update, and Soccer Players',
        terms_of_service='https://www.github.com/Ambrose280/soccer-rest-api',
        contact=openapi.Contact(email='ifiokambrose@gmail.com'),
        license=openapi.License(name='Test License')
               ),
        
	public=True,
    # permission_classes=(permissions.IsAuthenticated),

)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('players/', include('players.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

