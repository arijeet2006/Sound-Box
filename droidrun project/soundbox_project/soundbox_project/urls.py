from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.dashboard, name='home'),
    
    path('api/log/', views.log_payment, name='log_payment'),

    path('api/live-data/', views.get_live_data, name='live_data'),
]