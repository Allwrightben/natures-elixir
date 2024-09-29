from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                subject=(
                    f"New message from {contact.name}"
                    f" REG: {contact.category}"
                ),
                message=(
                    f"Name: {contact.name}\n"
                    f"Email: {contact.email}\n\n"
                    f"Message:\n{contact.message}"
                ),
                # From email
                from_email='benallwright11@gmail.com',
                # Owner email
                recipient_list=['ben.allwright@learningpeople.co.uk'],
                fail_silently=False,
            )

            messages.success(
                request, "Your message has been sent successfully!"
            )
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'contact_form': form})
