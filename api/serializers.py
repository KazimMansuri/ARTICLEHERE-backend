from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token





class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']


# for password hashing:-

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}


    def create(self, vaidated_date):
        user = User.objects.create_user(**vaidated_date)
        Token.objects.create(user=user)
        return user







