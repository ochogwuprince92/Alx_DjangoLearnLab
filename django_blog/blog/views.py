from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q
from .models import Post, Tag
from django.http import HttpResponseForbidden

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, "profile.html")

def home(request):
    return render(request, 'home.html')

def post(request):
    return render(request, 'post.html')
    
# List View: Display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Detail View: Show individual post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create View: Create a new post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('posts')

# Update View: Edit an existing post
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_queryset(self):
        # Ensure only the author can edit their posts
        return Post.objects.filter(author=self.request.user)

    success_url = reverse_lazy('posts')

# Delete View: Delete a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'

    def get_queryset(self):
        # Ensure only the author can delete their posts
        return Post.objects.filter(author=self.request.user)

    success_url = reverse_lazy('posts')
    # View to display the post and its comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

# View to create a new comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['post_id']})

# View to edit a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

# View to delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()

    return render(request, 'search_results.html', {'posts': posts, 'query': query})

def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = tag.posts.all()
    return render(request, 'tag_posts.html', {'posts': posts, 'tag': tag})

def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)  # Fetch the comment by primary key (pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)  # Redirect to the post's detail page
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form})

def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Ensure the user is authenticated
            comment.save()
            return redirect('post_detail', pk=post.pk)  # Redirect to the post's detail view
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # Ensure the user is the author of the comment or is an admin
    if comment.author == request.user or request.user.is_staff:
        comment.delete()
        return redirect('post_detail', pk=comment.post.pk)  # Redirect to the post's detail view
    else:
        return HttpResponseForbidden("You are not allowed to delete this comment.")