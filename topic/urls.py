from django.urls import path
from .views import *

urlpatterns = [
    path('', TopicList.as_view(), name='topic_list'),
    path('new/', TopicNew.as_view(), name='topic_new'), 
    path('<int:pk>/', TopicView.as_view(), name='topic_view'),
]
