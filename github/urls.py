from django.urls import path
from . import views  # O la ruta correcta a tu archivo views.py

urlpatterns = [
    # Tus otras URLs...
    path('/webhook/github/', views.github_webhook, name='github_webhook'),

    
]