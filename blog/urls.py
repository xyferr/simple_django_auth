from django.urls import path
from . import views

urlpatterns = [
    path('create-blog-post/', views.create_blog_post, name='create_blog_post'),
    path('doctor-blog-posts/', views.doctor_blog_posts, name='doctor_blog_posts'),
    path('patient-blog-posts/', views.patient_blog_posts, name='patient_blog_posts'),
    path('blog-post/<int:id>/', views.blog_post_detail, name='blog_post_detail'),
]