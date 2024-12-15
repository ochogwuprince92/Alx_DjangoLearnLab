from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # Actor is the user who performed the action
    recipient = serializers.StringRelatedField()  # Recipient is the user receiving the notification
    verb = serializers.CharField()  # Action description (e.g., "liked your post")
    timestamp = serializers.DateTimeField()  # Time when the notification was created
    target = serializers.CharField()  # The target of the action (e.g., Post title)
    
    class Meta:
        model = Notification
        fields = ['actor', 'recipient', 'verb', 'timestamp', 'target']
        read_only_fields = ['timestamp']
