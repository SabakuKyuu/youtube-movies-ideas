from django.urls import path
from .views import (
    IdeaListAPIView,
    IdeaCreateAPIView,
    IdeaDetailAPIView,
    IdeaUpdateAPIView,
    IdeaDeleteAPIView,
    VoteListAPIView,
    VoteCreateAPIView,
    VoteDetailAPIView,
    VoteUpdateAPIView,
    VoteDeleteAPIView,
)

urlpatterns = [
    path('ideas/list/', IdeaListAPIView.as_view()),
    path('ideas/create/', IdeaCreateAPIView.as_view()),
    path('ideas/detail/<int:pk>/', IdeaDetailAPIView.as_view()),
    path('ideas/update/<int:pk>/', IdeaUpdateAPIView.as_view()),
    path('ideas/delete/<int:pk>/', IdeaDeleteAPIView.as_view()),
    path('votes/list/', VoteListAPIView.as_view()),
    path('votes/create/', VoteCreateAPIView.as_view()),
    path('votes/detail/<int:pk>/', VoteDetailAPIView.as_view()),
    path('votes/update/<int:pk>/', VoteUpdateAPIView.as_view()),
    path('votes/delete/<int:pk>/', VoteDeleteAPIView.as_view()),
]

