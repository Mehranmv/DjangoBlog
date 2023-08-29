# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
# local imports
from .models import Category, Post, Comment
from .form import CommentForm, ReplyCommentForm


class CategoryView(View):
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(categories=category.id)
        paginated = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page = paginated.get_page(page_number)
        posts = posts.filter(categories=category.id)
        return render(request, 'posts/category.html', {'category': category, 'posts': posts, "page": page})


class PostDetailView(View):
    form_class = CommentForm
    form_class_reply = ReplyCommentForm

    def get(self, request, post_slug):
        categories = Category.objects.all()
        ancestors = categories.get_ancestors(include_self=True)
        form = self.form_class()
        post = Post.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post=post, is_accepted=True)
        latest_post = Post.objects.filter(categories=post.categories)
        latest_post = latest_post.exclude(slug=post_slug)[:2]
        return render(request, 'posts/detail.html',
                      {"post": post, 'form': form, 'categories': categories, 'latest_post': latest_post, 'ancestors': ancestors, 'comments': comments,
                       'reply_form': self.form_class_reply()})

    def post(self, request, post_slug):
        post = get_object_or_404(Post, slug=post_slug)
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, _("نظر شما ثبت و پس از تایید به کاربران نمایش داده میشود"), 'success')
            return redirect('posts:post_detail', post.slug)


class CommentReplyView(View):
    form_class = ReplyCommentForm

    def post(self, request, post_slug, comment_id):
        post = get_object_or_404(Post, slug=post_slug)
        comment = get_object_or_404(Comment, id=comment_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.parent_id = comment.id
            reply.save()
            messages.success(request, _("نظر شما ثبت و پس از تایید به کاربران نمایش داده میشود"), 'success')
            return redirect('posts:post_detail', post.slug)
