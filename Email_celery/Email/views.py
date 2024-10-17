# email_app/views.py
from django.shortcuts import render
from Email.tasks import send_email_task

def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = [request.POST.get('recipient')]
        
        # Call the Celery task to send the email
        send_email_task.delay(subject, message, recipient_list)
        
        return render(request, 'email_sent.html')
    
    return render(request, 'send_email.html')
