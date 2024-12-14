from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.request.data['post'])
        serializer.save(author=self.request.user, post=post)

class FeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        followed_users = user.following.all()  # Get all users the current user follows

        # Get posts from the followed users, ordered by the creation date (most recent first)
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the user already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the Like instance
        Like.objects.create(user=user, post=post)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post,
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the user has liked the post
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

# Create your views here.
