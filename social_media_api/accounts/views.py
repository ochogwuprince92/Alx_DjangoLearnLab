from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework import status
from rest_framework import generics

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
        })

class RegisterUserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        user = request.user

        if user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        user.following.add(user_to_follow)
        return Response({"detail": f"Now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

# Follow User View: Allows users to follow another user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # Fetching the user to follow using get_object_or_404 to ensure the user exists
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        user = request.user  # Get the current logged-in user

        # Ensure the user does not follow themselves
        if user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user_to_follow to the current user's following list
        user.following.add(user_to_follow)
        return Response({"detail": f"Now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

# Unfollow User View: Allows users to unfollow another user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # Fetching the user to unfollow
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        user = request.user  # Get the current logged-in user

        # Ensure the user does not unfollow themselves
        if user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the user_to_unfollow from the current user's following list
        user.following.remove(user_to_unfollow)
        return Response({"detail": f"Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

# List of all users view: Returns a list of all users in the system (can be used to view users to follow)
class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get all users (excluding the current user to avoid following oneself)
        users = CustomUser.objects.all().exclude(id=request.user.id)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)