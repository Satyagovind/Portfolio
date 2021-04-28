from django.shortcuts import render,get_object_or_404
from . import urls
from .models import Blogs

# Create your views here.
def some(request):
     all_blogs = Blogs.objects.order_by('-date')
     return render (request,'portfo/blog.html', {'myBlogs':all_blogs})


def details(request,blog_id):
     blogs = get_object_or_404(Blogs, pk=blog_id)
     return render(request,'portfo/details.html', {'details':blogs})
