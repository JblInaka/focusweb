from django.shortcuts import render, get_object_or_404
from blog.models import Post, Author, Comment 
from blog.forms import CommentForm
from django.http import HttpResponseRedirect 

# Create your views here.


def index(request):
    all_posts = Post.objects.all().order_by('-date') 
    return render(request,'blog/index.html', {'posts' : all_posts})


def detail(request, post_id):
    postdetail = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=postdetail).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=postdetail, user=request.user, content=content)
            comment.save()
            return HttpResponseRedirect("/")
    else:
        comment_form = CommentForm()
            
    return render(request, 'blog/detail.html', {'post':postdetail, 'comments':comments, 'comment_form':comment_form})

#text

# git@github.com:JblInaka/focusweb.git

