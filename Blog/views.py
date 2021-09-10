from datetime import datetime

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect

from Blog.models import Students, Blog, Comment
from django.views import generic
from rest_framework.generics import ListAPIView

class BlogView(generic.ListView):
    template_name = "blog.html"
    queryset =Blog.objects.all()
    context_object_name = "blog"

class BlogDetailView(generic.DetailView):
    template_name = "detail.html"
    queryset = Blog.objects.all()
    context_object_name = "blog"
    # extra_context = {"comments " : Comment.objects.all()}
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        blog_id=self.kwargs['pk']
        comments = Comment.objects.filter(blog_id=blog_id)
        context['comments']=comments
        return context
    def post(self,request,*args,**kwargs):
        form= request.POST
        text = form['text']
        blog_id = self.kwargs['pk']
        print("post")
        Comment.objects.create(text=text,blog_id = blog_id)
        return redirect(f"/blog/{blog_id}")

def saw_date(request):
    today = datetime.now()
    return HttpResponse(f"Today : {str(today)}")

def image_view(request):
    path = settings.BASE_DIR/ 'static'/ '123.jpg'
    file = open(path,'rb')
    return FileResponse(file)


def student_view(request):
    student = Students.objects.all()
    data = {
        'students': student
    }

    return render(request,'student.html',context=data)

from Blog.forms import BlogForm, BlogSerializer


def create_post(request):
    if request.method== "POST":
        form = request.POST
        title = form['title']
        description = form['description']
        hashtag = form['hashtag']
        image=request.FILES['image']

        Blog.objects.create(title = title,description=description, hashtag=hashtag,image=image)

        return redirect ('/blog/')
    if request.method =="GET":
        return render(request,'create_post.html')


class BlogListApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
