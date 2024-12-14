from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='actor_notifications')
    verb = models.CharField(max_length=255)  # Action description (e.g., "liked your post")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # For generic notifications (can be a post, comment, etc.)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')

    def __str__(self):
        return f"Notification for {self.recipient.username} by {self.actor.username}"


# Create your models here.
