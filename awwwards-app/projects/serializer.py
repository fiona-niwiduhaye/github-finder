from rest_framework import serializers
from .models import Profile
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','image', 'description', 'user', 'date_posted', 'link']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'bio', 'contact']
