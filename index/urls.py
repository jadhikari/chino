from django.urls import path
from . import views

urlpatterns = {
    path('',views.chino),
    path('about',views.about),
    path('calendar',views.calendar),
    path('components',views.components),
    path('contact',views.contact),
    path('company',views.company),
}
