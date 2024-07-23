from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings

def send_email_with_attachment(request):
    subject = 'Python (Selenium) Assignment - Your Name'
    body = """
    Dear Team,

    Please find attached the source code, documentation, and the screenshot of the confirmation page.

    GitHub Repository: https://github.com/roohanguptaa/assignments

    Best regards,
    [Your Name]
    """
    to_email = ['tech@themedius.ai']
    cc_email = ['hr@themedius.ai']
    from_email = settings.EMAIL_HOST_USER

    email = EmailMessage(subject, body, from_email, to_email, cc=cc_email)
    
    # Attach the screenshot
    screenshot_path = r'C:\assignments\form_screenshots\confirmation.png'
    email.attach_file(screenshot_path)
    
    # Attach the source code and documentation
    source_code_path = r'C:\assignments\source_code.zip'
    documentation_path = r'C:\assignments\documentation.txt'

    email.attach_file(source_code_path)
    email.attach_file(documentation_path)
    
    email.send()
    
    return HttpResponse("Email sent successfully")
