from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

def send_email_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Construct email message
        email_message = f"Name: {name}\nEmail: {email}\n\n{message}"

        # Send email
        send_mail(
            subject,
            email_message,
            email,  # sender's email address
            ['salihuabduljawwad.a@gmail.com'],  # recipient's email address
            fail_silently=False,
        )

        # Redirect after sending email
        return HttpResponseRedirect(reverse('success_page'))  # Redirect to success page

    return render(request, 'email_form.html')
