from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from .forms import Postform

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog_turma/postlist.html',{'posts':posts})

def post_detail(request, pk):
    post =  get_object_or_404(Post, pk=pk)
    return render(request, 'blog_turma/post_detail.html', {'post':post})

def post_new(request):
    if request.method == 'POST':
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform()
    return render(request, 'blog_turma/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Postform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            # post = form.save(commit=False)
            # post.author = request.user
            
            # post.published_date = timezone.now()
            # post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform(instance=post)
    return render(request, 'blog_turma/post_edit.html', {'form': form})