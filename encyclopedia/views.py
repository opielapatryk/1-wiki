from django.shortcuts import render

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    return render(request, "encyclopedia/title.html", {
        "entries": util.get_entry(title),
        "title": title
    })