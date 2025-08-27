from django.shortcuts import render,get_object_or_404, redirect
from .forms import BlogForm
from .models import Blog    

def Home(request):
    blogs = Blog.objects.all()  
    author = None                

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['author']
            blog = Blog.objects.filter(author=name).first()
            #author1 = Blog.objects.getall()
            #author2 = authot1.filter(author=name)
            #if(autho2 == name):
            # render------
            if blog:
                author = name
    else:
        form = BlogForm()

    return render(request, 'index.html', {
        'form': form,
        'blogs': blogs,
        'author': author
    })











def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = BlogForm(instance=blog)

    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})