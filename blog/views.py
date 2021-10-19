from django.shortcuts import render

posts=[
    {
        'author': 'ozlem ezgi sari',
        'title': 'First Blog Post',
        'content':'trial post',
        'date_posted':'October 19 , 2021 ',
    },
    {
        'author':'volkan aktaş',
        'title':'Hello Friends,Welcome to My Channel',
        'content':'How to get rich from Bitcoin',
        'date_posted':'October 20 , 2021 ',
    }
   
]



def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
