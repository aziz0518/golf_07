from django.contrib import messages
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from golf.forms import LoginForm
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import render, redirect


from django.core.mail import  EmailMessage
from django.template.loader import render_to_string
from golf.forms import  LoginForm, RegisterForm
from golf.models import User
from golf.views.token import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site




def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
            else:
                messages.add_message(
                    request,
                    level=messages.WARNING,
                    message='User not found'
                )

    return render(request, 'golf/auth/login.html', {'form': form})





# class LoginPageView(View):
#     template_name = 'golf/auth/login.html'
#     form_class = LoginForm


#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, 'golf/auth/login.html', {'form': form, 'message': message })
    
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('index')
#             else:
#                 messages.add_message(
#                     request,
#                     level=messages.WARNING,
#                     message='User not found'
#                     )

#         return render(request, 'golf/auth/login.html', {'form': form})
    




class RegisterPageView(View):
    template_name = 'golf/auth/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {'form': form, 'message': message })
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(first_name=first_name, email=email, password=password)
            user.is_active = False
            user.is_staff = True
            user.is_superuser = True
            user.save()
            # corrent_site = get_current_site(request)
            # subject = 'Verify your email'
            # message = render_to_string('golf/auth/email/activation.html',
            #                            {
            #                                'request':request,
            #                                'user': user,
            #                                'domain':corrent_site.domain,
            #                                'uid': urlsafe_base64_encode(force_bytes(user.id)),
            #                                'token': account_activation_token.make_token(user)

            #                            }
            #                            )
            # email = EmailMessage(subject=subject, body=message, to=[email])
            # email.content_subtype = 'html'
            # email.send()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        
        return render(request, 'golf/auth/register.html', {'form': form})