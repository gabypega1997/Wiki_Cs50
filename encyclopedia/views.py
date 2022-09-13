from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    return render(request,'encyclopedia/wiki.html',{
        "mdtext":util.get_entry(title),
        'title':title
    })

