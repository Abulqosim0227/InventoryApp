"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    # Admin panel with translation
    path(_('admin/'), admin.site.urls),
    
    # Shop URLs
    path('', include('shop.urls')),  # Default landing page (shop)
    
    # Multiple file upload URLs
    path('files/', include('multiplefile.urls')),  # Assign a unique prefix
    
    # Rosetta for translations (optional)
    path('rosetta/', include('rosetta.urls')),  
    
    # User management URLs
    path('user/', include('user.urls')),  
    
    # Configuration or other settings (ensure unique prefixes)
    path('config/', include('config.urls')),  
]

# Static and media file handling during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = i18n_patterns(
#     path(_('admin/'), admin.site.urls),
#     path('', include('shop.urls')),
#     path('', include("multiplefile.urls")),
#     path('rosetta/', include('rosetta.urls')),
#     path('user/', include('user.urls')),
#     path('', include('config.urls')),


# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
