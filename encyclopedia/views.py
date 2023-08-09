from django.shortcuts import render
from django import forms
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
                return render(request, "encyclopedia/title.html", {
                    "entries": util.get_entry(title),
                    "title": title,
                })
            else:
                error = 'This entry already exist.'
                return render(request, "encyclopedia/title.html", {
                    "entries": error,
                    "title": title,
                })
            
    return render(request, "encyclopedia/create.html", {
        "form":NewEntriesForm(),
        "title": title
    })