from django.shortcuts import render,redirect,reverse
from django.views.generic import (
                                ListView ,
                                DetailView 
)
from .models import Post
from .forms import PostForm

def home(request):
    context={
        'posts':Post.objects.all()
    }
    
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name ='posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


def postCreate(request):
    postForm=PostForm(request.POST or None,request.FILES or None)


    if postForm.is_valid():
        post = postForm.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("blog:blog-home")
    
    return render(request,"blog/post_form.html",{"postForm":postForm})


#class PostCreateView(CreateView):
   #model = Post
   #fields = ['title','content']

   #def form_valid(self,form):
    #   form.instance.author= self.request.user
     #  super().form_valid(form)
      # posts = Post.objects.all()
       #reverse("blog:blog-home-post",kwargs={"pk":self.pk})

   #def get_absolute_url(self):
       #return redirect('blog:blog-home')
       
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
