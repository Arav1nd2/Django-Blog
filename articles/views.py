from django.shortcuts import render

# Create your views here.


def articleList(req):
    return render(req, 'articles/listView.html')
