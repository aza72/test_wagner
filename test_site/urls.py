from django.urls import path
from test_site.views import index

urlpatterns = [
    path('index/', index, name='index'),

]