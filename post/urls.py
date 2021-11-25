from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view()),
    path("<int:pk>/", views.PostDetailView.as_view()),
    path('xyi/', views.Blogcreat.as_view),
    path("/comment/<int:pk>/", views.create_comment),
    ]
