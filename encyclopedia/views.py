from django.shortcuts import render
from django import forms
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


class EditContentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())

def entry(request,title):
    if request.method == "POST":
        form = EditContentForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["content"]
            util.save_entry(title,entry)
            return render(request, "encyclopedia/entry.html", {
                    "entries": util.get_entry(title),
                    "title": title,
                })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entries": util.get_entry(title),
            "title": title
        })

def edit(request,title):
    initial = {'content': util.get_entry(title)}
    return render(request, "encyclopedia/edit.html",{
        "form":EditContentForm(initial=initial),
        "title": title
    })

    
    
def is_subst_in_list(list,substring):
    new_list = []
    for string in list:
        if substring in string:
            new_list.append(string)
    return new_list

new_list_entries = [x.lower() for x in util.list_entries()]

def query(request):
    entries_list = []
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


class NewEntriesForm(forms.Form):
    title = forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    entry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Entry'}))

def create(request):
    error = ''
    title = ''
    if request.method == 'POST':
        form = NewEntriesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            entry = form.cleaned_data["entry"]

            if title not in new_list_entries:
                util.save_entry(title,entry)
                return render(request, "encyclopedia/entry.html", {
                    "entries": util.get_entry(title),
                    "title": title,
                })
            else:
                error = 'This entry already exist.'
                return render(request, "encyclopedia/entry.html", {
                    "entries": error,
                    "title": title,
                })
            
    return render(request, "encyclopedia/create.html", {
        "form":NewEntriesForm(),
        "title": title
    })

def rand(request):
    entries = util.list_entries()
    rand_entry = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {"title":rand_entry,
    "entries":util.get_entry(rand_entry)})