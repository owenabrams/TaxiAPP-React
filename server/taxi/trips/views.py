#from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets # changed under HTTP
from rest_framework_simplejwt.views import TokenObtainPairView # new under authentication

from .models import Trip # new under HTTP
from .serializers import LogInSerializer, TripSerializer, UserSerializer # changed under Authentication and HTTP


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class LogInView(TokenObtainPairView): # new under authentication
    serializer_class = LogInSerializer


class TripView(viewsets.ReadOnlyModelViewSet):  #new change under HTTP
    lookup_field = 'id' # new update under HTTP
    lookup_url_kwarg = 'trip_id' # new update under HTTP
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer