from django.urls import path
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
path('home1/', PostListView.as_view(),name='home1'),
path('fashion/', views.fashion,name='fashion'),
path('food/', views.food,name='food'),
path('health/', views.health,name='health'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('about/', views.about,name='blog-about'),
path('home/', views.home,name='home'),
path('contact/', views.contact,name='contact'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
]


