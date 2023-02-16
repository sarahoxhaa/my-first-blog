from django.shortcuts import render
from django.utils import timezone
from .models import Post
    #This is exactly what views are supposed to do: connect models and templates. In our post_list view we will need to take the models we want to display and pass them to the template. In a view we decide what (model) will be displayed in a template.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})