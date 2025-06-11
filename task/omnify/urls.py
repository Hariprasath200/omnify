from django.urls import path
from .views import *

urlpatterns=[
    path('upcomingclass/',FitnessclassView.as_view(),name='fitnessclass'),
    path('booking/',BookingAccept.as_view(),name='BookingView'),
    path('allbookings/',AllBookingsView.as_view(),name='allbookings')
]