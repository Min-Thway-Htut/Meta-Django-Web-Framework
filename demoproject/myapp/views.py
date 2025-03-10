from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import ContactForm



def contact_view(request):
    form = ContactForm()
    submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            submitted = True

    return render(request, "contact.html", {"form": form, "submitted": submitted})


