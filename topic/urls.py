from django.urls import path
from .views import *

urlpatterns = [
    path('', TopicList.as_view(), name='topic_list'),
    path('new/', TopicNew.as_view(), name='topic_new'), 
    path('<int:pk>/', TopicView.as_view(), name='topic_view'),
    path('<int:tid>/reply/', TopicReply.as_view(), name='topic_reply'),
    path('<int:pk>/delete/', TopicDelete.as_view(), name='topic_delete'),
]
