from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Contact
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def contact(request):
    if request.method=="POST":
        cont=Contact()
        name=request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        cont.name=name
        cont.email = email
        cont.message = message
        cont.save()
        return render(request, 'blog/contact.html')

    else:
        return render(request, 'blog/contact.html')


def fashion(request):
    context = {
        'fashion': Post.objects.filter(niche='fashion')
    }
    return render(request, 'blog/fashion.html',context)

def health(request):
    context = {
        'health': Post.objects.filter(niche='health')
    }
    return render(request, 'blog/health.html',context)


def food(request):
    context = {
        'food': Post.objects.filter(niche='food')
    }
    return render(request, 'blog/food.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home1.html'
    context_object_name = 'posts'
    ordering = ['-date']
    


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['niche','title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['niche','title', 'content']

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
    success_url = '/blog/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')

def index(request):
    return render(request, 'blog/index.html')

# Create your views here.
