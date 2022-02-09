from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.views.generic import (
                                ListView ,
                                DetailView ,
                                UpdateView,
                                
)
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect

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

@login_required(login_url='/login/')
def postCreate(request):
    postForm=PostForm(request.POST or None,request.FILES or None)


    if postForm.is_valid():
        post = postForm.save(commit=False)
        post.author = request.user
        post.save()
        print("Post ID")
        print(post.id)
        print("LAST")
        #HttpResponseRedirect('blog:blog-home-post'%post.id)
        return HttpResponseRedirect(reverse('blog:blog-home-post', args=(post.id,)))
        #return redirect("'blog:blog-home-post' post.id")
        #return reverse('blog:blog-home-post', args=(post.id,))
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

#login_required(login_url = "user:login")
def postUpdate(request,id,pk):
    post = get_object_or_404(Post,id = id,author = request.user,pk=pk,)

    postForm = PostForm(request.POST or None,request.FILES or None,instance=post,)
    if postForm.is_valid() :
        post = postForm.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(reverse("blog:blog-home-post" , args=(post.id,)))
    context = {
        "post":postForm,   } 

    return render(request,"blog/post_form.html",{"postForm":postForm})





def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
