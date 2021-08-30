from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddComment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #form_class = CreatePost
    fields = ['title', 'content', 'category', 'img', 'vid']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'img', 'vid']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.all().filter(author=user)



class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddComment
    ordering = ['-date']

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('blog-home')

@login_required
def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        messages.success(request, f'You Unliked {post}')
    else:
        post.likes.add(request.user)
        messages.success(request, f'You Liked {post}')
    return HttpResponseRedirect(reverse('post-dateil', args= [str(pk)]))
