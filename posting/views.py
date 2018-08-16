from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
#NOT YET USED from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from posting.tokens import account_activation_token
from django.contrib.auth import login

from .forms import CustomUserCreationForm
from .models import CustomUser

def home(request):
    return render(request, 'home.html')

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active
            user.save()
            current_site = get_current_site(self.request.POST)
            subject = '[gpDA]Active your Account'
            message = render_to_string('registration/account_activation_email.html',{
                'user' : user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

        return redirect('account_activation_sent')

class ActivationSent(TemplateView):
    template_name = 'registration/account_activation_sent.html'

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