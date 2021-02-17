from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import(
     ListView, DetailView,
     CreateView,
     UpdateView,
     DeleteView

)    

# Create your views here.
       
     

#def myblog_home(request):
#   context={
 #       'posts':Post.objects.all() }
        
    #defining my blog homepage
  #  return render(request, 'myblog/home.html', context)

#creating a class base views

class PostListVeiw(ListView):
    model = Post
    template_name = 'myblog/home.html'
    context_object_name = 'posts'
    ordering =['-date_posted']
    paginate_by = 8


class UserPostListVeiw(ListView):
    model = Post
    template_name = 'myblog/user_posts.html'
    context_object_name = 'posts'
    #ordering =['-date_posted']
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDtailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

                
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    



def about(request):
    # blog about page
    return render(request, 'myblog/about.html')

#post like function
@login_required
def like_post(request):  
    user= request.user
    if request.method == 'POST':
        posts_id = request.POST.get('post_id')
        topic_obj = Post.objects.get(pk=posts_id)

        if user in topic_obj.liked.all():
            topic_obj.liked.remove(user)
        else:
            topic_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id= posts_id)

        if not created:
            if Like.values =='Like':
                Like.values == 'Unlike'
            else:
                Like.values == 'Like'
        like.save()
    
    return redirect('myblog:post-detail', pk=posts_id)

 
     
