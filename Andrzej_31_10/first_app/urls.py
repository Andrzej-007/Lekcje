from django.urls import path
from .views import *


urlpatterns = [
    path('', ShowData.as_view()),
    path('calendar/', ShowLink.as_view()),


]

