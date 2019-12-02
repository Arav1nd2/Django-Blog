
from django.urls import path, re_path
from . import views

app_name = "article"

urlpatterns = [
    re_path(r'^$', views.articleList, name="list"),
    re_path(r'^create/$', views.createArticle, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articleView, name="detail")
]
