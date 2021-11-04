from django.urls import path
from . import views

urlpatterns = {
    path('',views.chino),
    path('about',views.about),
}