from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    page = 0
    if request.method == "POST":
        page = int(request.POST['nr_page'])
    else:
        if request.GET.get('nr_page'):
            page = int(request.GET.get('nr_page'))

    blogs_count = Blog.objects.count()
    blogs_pages = int(blogs_count / 5) + 1
    blogs = Blog.objects.order_by('-date')[page*5:5+page*5]

    context = {
        'blogs': blogs,
        'blogs_count': blogs_count,
        'blogs_pages': range(blogs_pages),
        'page': [page-1, page, page+1],
    }
    return render(request, 'blog/blog.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})