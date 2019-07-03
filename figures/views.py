from django.shortcuts import render
from django.http    import HttpResponse
from . import forms

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.CompareForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['your_user'])
            print(form.cleaned_data['other_user'])
    else:
        form = forms.CompareForm()
    context = {
        "form": form
    }
    return render(request, "figures/index.html", context)
