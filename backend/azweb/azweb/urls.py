"""azweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from azweb import settings
from django.conf.urls import url

urlpatterns = [
    path('',include('registration_ca.urls')),
    path('chem_e_cross',include('chem_e_cross.urls')),
    path('optimiser',include('optimiser.urls')),
    path('q-viz-it',include('qviz_it.urls')),
    path('IDP',include('IDP.urls')),
    path('chemathon',include('chemathon.urls')),
    path('cipher',include('cipher.urls')),
    path('cop',include('cop.urls')),
    path('lca',include('lca.urls')),
    path('chemvision',include('chemvision.urls')),
    path('panel_discussion',include('panel_discussion.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),


    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

# urlpatterns += staticfiles_urlpatterns()

