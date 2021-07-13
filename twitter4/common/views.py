from django.shortcuts import render
from .forms import EmailForm
from helpers.send_email_message import email
from django.shortcuts import redirect

# Create your views here.


def send_user_email(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_message = form.save()
            email(subject=email_message.sender, message=email_message.message, recipient_list=['greateapp@yopmail.com'])
            return redirect('home')

    return render(request, 'common/contact_us.html', {'form': form})