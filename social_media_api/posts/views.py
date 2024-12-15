from rest_framework.generics import get_object_or_404
from rest_framework import generics, status
from rest_framework import permissions, IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser
from rest_framework.views import APIView


# Like a Post View: Handle liking a post and generating notifications
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the post object
        post = get_object_or_404(Post, pk=pk)

        # Create or retrieve the like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # New like created
            return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)
        else:
            # Like already exists
            return Response({'message': 'Post is already liked.'}, status=status.HTTP_200_OK)

# Unlike a Post View: Handle unliking a post and generating notifications
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the user has liked the post before attempting to unlike
        like = get_object_or_404(Like, user=user, post=post)

        # Remove the like
        like.delete()

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="unliked your post",
            target=post,
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Enforcing authentication

    def get(self, request):
        # Get the authenticated user's following list
        following_users = request.user.following.all()

        # Filter posts by authors in the following list
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts (assuming a PostSerializer exists)
        from posts.serializers import PostSerializer
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)