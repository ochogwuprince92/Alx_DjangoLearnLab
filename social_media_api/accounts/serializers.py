from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
    extra_kwargs = {
        'followers': {'read_only': True},
    }