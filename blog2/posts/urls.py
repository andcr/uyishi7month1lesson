from django.conf.urls import url
from . import views

urlpatterns = [
    url('page1/', views.page1, name='page1')
]