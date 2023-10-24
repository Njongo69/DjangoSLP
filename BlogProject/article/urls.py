from django.urls import path
from .views import showarticle

app_name = 'article'

urlpatterns = [path('', showarticle), ]
