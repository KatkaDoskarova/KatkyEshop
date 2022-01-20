from django.shortcuts import render, redirect
from Account.forms import RegistrationForm


def register(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = RegistrationForm()

    return render(response, "register.html", {"form":form})



