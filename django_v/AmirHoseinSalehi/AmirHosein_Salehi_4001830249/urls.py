from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="all-articles"),
    path("<str:slug>", view=views.detail, name="article-detail"),
    ]