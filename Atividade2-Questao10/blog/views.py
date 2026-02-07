
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})


def post(request, ano, mes, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        data_publicacao__year=ano,
        data_publicacao__month=mes
    )

    return render(request, 'blog/post.html', {'post': post})