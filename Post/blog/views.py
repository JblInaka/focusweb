from django.shortcuts import render, get_object_or_404
from blog.models import Post, Author, Comments 
from blog.forms import CommentForm

# Create your views here.


def index(request):
    all_posts = Post.objects.all().order_by('-date') 
    return render(request,'blog/index.html', {'posts' : all_posts})


def detail(request, post_id):
    postdetail = get_object_or_404(Post, pk=post_id)
    comments = Comments.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = comment_form.get('content')
            comment = Comments.objects.create(post=post, user=request.user, content=content)
            comment.save()
            HttpResponseRedirect('')
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
            
    return render(request, 'blog/detail.html', {'post':postdetail, 'comments':comments, 'comment_form':comment_form})

#text

# git@github.com:JblInaka/focusweb.git
# git@github.com:JblInaka/focusweb.git

