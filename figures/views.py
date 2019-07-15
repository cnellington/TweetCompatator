from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

from . import forms, services


# Handles original form page
def index(request):
    if request.method == 'POST':
        form = forms.CompareForm(request.POST)
        if form.is_valid():
            your_username = form.cleaned_data['your_user']
            other_username = form.cleaned_data['other_user']
            if (
                services.check_user_exists(your_username)
                and services.check_user_exists(other_username)
            ):
                request.session["your_user"] = your_username
                request.session["other_user"] = other_username
                services.process_users(your_username, other_username)
                return redirect(reverse("figures:figures"))
    else:
        form = forms.CompareForm()
    context = {
        "form": form
    }
    return render(request, "figures/index.html", context)


# Handles figure display
def figures(request):
    if not (request.session.get("your_user") and request.session.get("other_user")):
        return HttpResponseRedirect('/')

    user1 = request.session.get("your_user")
    user2 = request.session.get("other_user")

    context = {
        "your_user": user1,
        "other_user": user2,
        "tweets": str(services.get_tweet_stats(user1))
    }
    return render(request, "figures/figures.html", context)
