from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages  # Import for displaying feedback messages


def send_email_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate form inputs
        if not name or not email or not subject or not message:
            messages.error(request, "All fields are required.")
            return render(request, 'index.html')  # Re-render the index page with an error message

        # Construct email message
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send email
            send_mail(
                subject,
                email_message,
                'salihuabduljawwad.a@gmail.com',  # Your configured email
                ['salihuabduljawwad.a@gmail.com'],  # Recipient's email address
                fail_silently=False,
            )
            messages.success(request, "Email sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send email. Error: {e}")

        # Render the index page with messages
        return render(request, 'index.html')

    return render(request, 'index.html')
