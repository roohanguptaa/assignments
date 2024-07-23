from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render

def send_email(request):
    # Use a raw string for the file path to avoid escape sequence issues
    file_path = r'C:\assignments\confirmation_page.png'

    email = EmailMessage(
        'Python (Selenium) Assignment - Your Name',
        'Please find the attached screenshot of the confirmation page.',
        settings.EMAIL_HOST_USER,
        ['tech@themedius.ai'],
        ['hr@themedius.ai']
    )
    email.attach_file(file_path)
    email.send()
    return render(request, 'email_sent.html')
