from django.contrib import admin
from django.urls import path
from citation_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/citations/', views.api_citations, name='api_citations'),
]