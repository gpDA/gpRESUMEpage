from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from posting.tokens import account_activation_token
from django.contrib.auth import login

from .forms import CustomUserCreationForm
from .models import CustomUser

def home(request):
    return render(request, 'home.html')

def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, ):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        # return redirect('home')
        return render(request, 'registration/signup_success.html')
    else:
        return render(request, 'error.html')

def password_reset(request):
    if request.method == 'POST':
        return HttpResponseRedirect("/password_reset/done")
    return render(request, 'registration/password_reset_form.html')


def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')
def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html')    
def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')    
