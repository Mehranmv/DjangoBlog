# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
# local imports
from .models import Category, Post, Comment, Bookmark, Like
from accounts.models import Membership
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
        is_bookmarked = False
        if request.user.is_authenticated:
            if Membership.objects.filter(user=request.user).exists():
                membership = Membership.objects.get(user=request.user)
            else:
                membership = None
            if post.is_membership_item and membership:
                pass
            elif not post.is_membership_item:
                pass
            else:
                messages.error(request, _("برای نمایش این پست باید اکانت ویژه تهیه کنید !"), 'danger')
                return redirect('accounts:user_profile')
            try:
                Bookmark.objects.get(user=request.user, post=post)
                is_bookmarked = True

            except Bookmark.DoesNotExist:
                is_bookmarked = False
        elif not request.user.is_authenticated:
            messages.error(request, 'برای دیدن پست های ویژه باید وارد شوید', 'danger')
            return redirect('home:home_page')

        context = {
            "post": post,
            'form': form,
            'latest_post': latest_post,
            'ancestors': ancestors,
            'comments': comments,
            'is_bookmarked': is_bookmarked,
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


class BookmarkPost(LoginRequiredMixin, View):
    def post(self, request):
        if request.user.is_authenticated:
            post_id = request.POST.get("post_id")
            is_bookmarked = request.POST.get("is_bookmarked") == "True"
            post = get_object_or_404(Post, id=post_id)
            if is_bookmarked:
                Bookmark.objects.filter(user=request.user, post=post).delete()
                is_bookmarked = False
                return JsonResponse({"is_bookmarked": is_bookmarked}, status=200)
            else:
                Bookmark.objects.create(user=request.user, post=post)
                is_bookmarked = True
                return JsonResponse({"is_bookmarked": is_bookmarked}, status=200)
        return JsonResponse({"error": ""}, status=400)


class CommentLikeView(LoginRequiredMixin, View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        like = Like.objects.filter(comment=comment, user=request.user)
        if like.exists():
            like.delete()
        else:
            Like.objects.create(comment=comment, user=request.user)
        return redirect('posts:post_detail', comment.post.slug)
