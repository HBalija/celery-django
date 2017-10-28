from django.shortcuts import render, redirect

from .forms import ContactForm
from .tasks import send_contact_email


def contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_contact_email.delay(data)
            return redirect('contact')

    return render(request, 'index.html', {
        'form': form,
    })
