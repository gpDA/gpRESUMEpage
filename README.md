# gpRESUMEpage

* It is now development MODE

#### Objective of this exercise 
  : is to make a personal website which becomes a repository for my study and project. Using ckeditor, I enable code explanation line by line using snippets and code capturing pictures.  
  
#### WHAT is special about gpRESUMEpage
1. Since I use both English and Korean I enable Postings and Projects in both English and Korean to meet with more audiences. For example, Posten & Postko are sharing the same number field in the database and have a ONE to ONE relationship. So that a user can look at the corresponding Postings and Projects in different languages with a click away

2. Also people can leave their comments on Projects and Postings as they sign in. To make an EASY sign in, people can either register their account with email verification OR use social account login such as GITHUB and FACEBOOK

sample MODELS.PY [https://github.com/gpDA/gpRESUMEpage/blob/c170f1241e9d2047303e892493d5e56c773d02cc/project/models.py#L9-L18]

```
class Projecten(models.Model):
    # 1 - M CustomUser
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200, blank=True)
    number = models.IntegerField()
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField(config_name='default', null=True)
    order = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)    
```

sample VIEWS.PY [https://github.com/gpDA/gpRESUMEpage/blob/c170f1241e9d2047303e892493d5e56c773d02cc/posting/views.py#L30-L53]

```
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
```

sample HTML [https://github.com/gpDA/gpRESUMEpage/blob/c170f1241e9d2047303e892493d5e56c773d02cc/templates/signup.html#L1-L23]

```
{% extends 'base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
      {% for field in form %}
      <p>
        {{ field.label_tag }}<br>
        {{ field }}
        {% if field.help_text %}
          <small style="display: none">{{ field.help_text }}</small>
        {% endif %}
        {% for error in field.errors %}
          <p style="color: red">{{ error }}</p>
        {% endfor %}
      </p>
      {% endfor %}
    <button type="submit">Sign up</button>
  </form>
{% endblock %}
```



TO RUN THE CODE

    source ./bin/active
    PIP INSTALL EVERYTHING IN requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    
