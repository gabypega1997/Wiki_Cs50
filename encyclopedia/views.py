import re
from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    return render(request,"encyclopedia/wiki.html",{
        'title':title,
        'get_entry': util.get_entry
    })

