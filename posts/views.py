# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
# local imports
from .models import Category, Post, Comment
from .form import CommentForm, ReplyCommentForm
import utils


class CategoryView(View):
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(category=category.id)
        page_number = request.GET.get('page')
        page = utils.pagination(posts, page_number)
        context = {
            'category': category,
            'posts': posts,
            'page': page
        }
        return render(request, 'posts/category.html', context)


class PostDetailView(View):
    form_class = CommentForm
    form_class_reply = ReplyCommentForm

    def get(self, request, post_slug):
        post = get_object_or_404(Post, slug=post_slug)
        ancestors = post.category.get_ancestors(include_self=True)
        form = self.form_class()
        comments = Comment.objects.accepted(post)
        latest_post = Post.objects.filter(category=post.category)
        latest_post = latest_post.exclude(id=post.id)[:2]
        context = {
            "post": post,
            'form': form,
            'latest_post': latest_post,
            'ancestors': ancestors,
            'comments': comments,
            'reply_form': self.form_class_reply()
        }
        return render(request, 'posts/detail.html', context)

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
