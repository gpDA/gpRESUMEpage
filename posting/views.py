from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
#NOT YET USED from django.contrib.auth.decorators import login_required
import uuid
import sys
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from .models import CustomUser
import uuid
import sys
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

'''
def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            uid = str(uuid.uuid4())
            user = form.save(commit=False)
            user.is_active = False
            url = request.build_absolute_uri(f'login?uid={uid}')
            send_mail(
                'Your login link',
                f'Use this link to log in:\n\n{url}',
                'noreply',
                [email],
            )
        return render(request, 'account_activation_sent.html')
    
def login(request):
    uid = request.GET.get('uid')
    user = authenticate(uid=uid)
    if user is not None:
        auth_login(request, user)
    return redirect('/')
'''    


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
            email = request.POST['email']
            username = request.POST['username']
            user = form.save(commit=False)
            user.is_active = False
            #current_site = get_current_site(request)
            url = request.build_absolute_uri(f'/login?username={username}')
            send_mail(
                'Your login link',
                f'Use this link to log in:\n\n{url}',
                'noreply',
                [email],
            )     
            '''       
            subject = '[gpDA]Active your Account'
            message = render_to_string('registration/account_activation_email.html',{
                'user' : user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            '''
            #user.email_user(subject, message)
            return redirect('activationSent')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})
        

def ActivationSent(request):
    return render(request, 'registration/account_activation_sent.html') 

def Activation(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/account_activation_invalid.html')
