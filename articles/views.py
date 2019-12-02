from django.shortcuts import render, redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def articleList(req):
    data = Articles.objects.all().order_by('created_at')
    return render(req, 'articles/listView.html', {'articles': data})


def articleView(req, slug):
    # return HttpResponse(slug)
    data = Articles.objects.get(slug=slug)
    return render(req, 'articles/detailView.html', {'article': data})


@login_required(login_url="/accounts/login")
def createArticle(req):
    if req.method == 'POST':
        form = forms.CreateArticle(req.POST, req.FILES)
        # save the data
        if form.is_valid():
            data = form.save(commit=False)
            data.author = req.user
            data.save()
            return redirect("article:list")
    else:
        form = forms.CreateArticle()
    return render(req, 'articles/createView.html', {'form': form})
