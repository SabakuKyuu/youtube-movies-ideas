from rest_framework import generics
from .models import Vote, Idea
from .serializers import VoteSerializer, IdeaSerializer


class IdeaListAPIView(generics.ListAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class IdeaCreateAPIView(generics.CreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class IdeaDetailAPIView(generics.RetrieveAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class IdeaUpdateAPIView(generics.UpdateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class IdeaDeleteAPIView(generics.DestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class VoteListAPIView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteCreateAPIView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteUpdateAPIView(generics.UpdateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDeleteAPIView(generics.DestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

