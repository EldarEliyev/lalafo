from django.shortcuts import render, redirect, get_object_or_404
from..models.comment import Comment
from ..serializers import CommentSerializer
from ..forms import CommentForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from..models.like import Like 

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def toggle_comment_like(self, request, pk=None):
        comment = self.get_object()
        like = Like.objects.filter(comment=comment).first()

        if like:
            like.delete()
            message = "Unliked Comment"
        else:
            Like.objects.create(comment=comment)
            message = "Liked Successfully Comment"
        return Response({"message": message,  "like_count": comment.comment_likes.count()})
    
#Comment CRUD:

def comment_list(request):
    comments = Comment.objects.all()
    return render(request,  "comment_list.html",  {"comments": comments})

def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comment_list")
    else:
        form = CommentForm()
    return render(request,  "create_comment.html",  {"form": form})

def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("comment_list")
    else:
        form = CommentForm(instance=comment)
    return render(request,  "update_comment.html",  {"form": form})

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        comment.delete()
        return redirect("comment_list")
    return render(request,  "delete_comment.html",  {"comment": comment})