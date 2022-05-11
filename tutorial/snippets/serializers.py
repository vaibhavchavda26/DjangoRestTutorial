from dataclasses import fields
from resource import setrlimit
from rest_framework import serializers
from . models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

#modelserializer
"""
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


#Adding end points for our user model
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many = True, queryset = Snippets.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
"""

#Hyperlinking our API
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format = 'html')

    class Meta:
        model = Snippets
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only = True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']