from django.shortcuts import render
from django import forms
from django.db.models import Q 

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

def is_subst_in_list(list,substring):
    new_list = []
    for string in list:
        if substring in string:
            new_list.append(string)
    return new_list


def query(request):
    entries_list = []
    new_list_entries = [x.lower() for x in util.list_entries()]
    query = request.GET.get("q").lower()

    entries_list = is_subst_in_list(new_list_entries,query)

    if len(entries_list) > 0:
        error_message = ""
    else:
        error_message = "That query didn't match any entries."

    return render(request, "encyclopedia/query.html", {
        "entries": entries_list,
        "error_message": error_message
    })