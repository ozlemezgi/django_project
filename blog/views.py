from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from users.models import Profile
from django.views.generic import (
                                ListView ,
                                DetailView ,
                                DeleteView,
                                

)
from .models import Post,Like,Comment
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
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name ='posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")





class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        p = Post.objects.get(id=self.kwargs['pk'])
        number_of_likes = p.like_set.all().count()
        print(number_of_likes)
        #total_likes=p.total_likes()
        #context["total_likes"]= total_likes
        context["number_of_likes"]= number_of_likes
        comments = p.comments.all()
        context["comments"]= comments
        return context

    
       #p = Post.objects.get(id=pk)
       #number_of_likes = p.like_set.all().count()


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

@login_required(login_url='/login/')
def addComment(request,pk):
    post = get_object_or_404(Post,id = pk)
    profil = Profile.objects.get(user=request.user)
    if request.method == "POST":
    
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = profil, comment_content = comment_content)
       # newComment.rate=rate
        newComment.post = post
        newComment.save()
    return redirect(reverse("blog:blog-home-post",kwargs={"pk":pk}))



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

@login_required(login_url = "/login/")
def postUpdate(request,pk):
    post = get_object_or_404(Post,pk=pk,author = request.user)

    postForm = PostForm(request.POST or None,request.FILES or None,instance=post)
    if postForm.is_valid() :
        post = postForm.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(reverse("blog:blog-home-post" , args=(post.pk,)))
    context = {
        "postForm":postForm,   }

    return render(request,"blog/post_update.html",context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url= '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})







def like(request, pk):
    p = Post.objects.get(id=pk)
    number_of_likes = p.like_set.all().count()
    new_like, created = Like.objects.get_or_create(user=request.user, post_id=pk)
    if not created:
        print("not created")
        return HttpResponseRedirect(reverse('blog:blog-home-post', args=(pk,)))
    else:
        
        print("All Created")
        return HttpResponseRedirect(reverse('blog:blog-home-post', args=(pk,)))
       

def showLikes(request):
    p = Post.objects.get(...)
    number_of_likes = p.like_set.all().count()
