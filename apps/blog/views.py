from .models import Post, PostView, Like, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('blog:detail', slug=post.slug)
        return redirect('blog:detail', slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'comment_form': CommentForm(),
            'view_type': 'View Post'
        })
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)

        return object


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/blog/'
    template_name = 'blog/create_post.html'

    def post(self, *args, **kwargs):
        form = PostForm(self.request.POST, self.request.FILES)
        try:
            if form.is_valid():
                post = form.save(commit=False)
                post.author = self.request.user
                post.save()
                return redirect('blog:home')
            else:
                print(form)
                return redirect('blog:create')
        except Exception as e:
            print(e)
            return redirect('blog:create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Create Post'
        })
        return context


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/posts/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Update Post'
        })
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/posts/list/'


def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_obj = Like.objects.filter(user=request.user, post=post)
    if like_obj.exists():
        like_obj[0].delete()
        return redirect('posts:posts_detail', slug=slug)
    else:
        Like.objects.create(user=request.user, post=post)
        return redirect('posts:posts_detail', slug=slug)
