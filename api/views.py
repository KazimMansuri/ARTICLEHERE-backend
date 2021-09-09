from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import viewsets             # for modelviewset, generic viewset , viewset
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User



############### model view set #####################



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer 
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
