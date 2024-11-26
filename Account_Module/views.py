from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from utils.email_service import send_email
from .forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from .models import User
from django.core.mail import EmailMessage


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'Account_Module/register.html', {
            'register_form': register_form
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if not user:
                user_username = register_form.cleaned_data.get('username')
                user: bool = User.objects.filter(username__iexact=user_username).exists()
                if not user:
                    user_password = register_form.cleaned_data.get('password')
                    new_user = User(
                        email=user_email,
                        username=user_username,
                        is_active=True,
                        email_active_code=get_random_string(72)
                    )
                    new_user.set_password(user_password)
                    new_user.save()
                    try:
                        send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user},
                                   'Emails/active_account.html')

                    except:
                        register_form.add_error('email', 'خطا در ارسال ایمیل فعالسازی')

                    else:
                        return redirect(reverse('login_page'))
                else:
                    register_form.add_error('username', 'این نام کاربری قبلا مورد استفاده واقع شده است')
            else:
                register_form.add_error('email', 'حساب کاربری با این ایمیل از قبل وجود دارد')
        return render(request, 'Account_Module/register.html', {
            'register_form': register_form
        })


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'Account_Module/login.html', {
            'login_form': login_form
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if user.is_active:
                    user_password = login_form.cleaned_data.get('password')
                    is_password_correct: bool = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'ایمیل یا رمز عبور اشتباه می باشد')
                else:
                    login_form.add_error('email', 'حساب کاربری شما فعال نمی باشد')
            else:
                login_form.add_error('email', 'ایمیل یا رمز عبور اشتباه می باشد')

        return render(request, 'Account_Module/login.html', {
            'login_form': login_form
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_page'))


class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = ForgetPasswordForm()
        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'Account_Module/forget_password.html', context)

    def post(self, request):
        forget_pass_form = ForgetPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if user.is_active:
                    return redirect('reset_password_page', user.id)
                else:
                    forget_pass_form.add_error('email', 'حساب کاربری وجود ندارد یا فعال نمی باشد')
            else:
                forget_pass_form.add_error('email', 'ایمیل وارد شده نادرست می باشد')
        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'Account_Module/forget_password.html', context)


class ResetPasswordView(View):
    def get(self, request, id):
        user: User = User.objects.filter(id=id, is_active=True).first()
        if user is not None:
            reset_pass_form = ResetPasswordForm()
            return render(request, 'Account_Module/reset_password.html', {
                'reset_pass_form': reset_pass_form,
                'user': user
            })
        else:
            return render(request, '404.html')

    def post(self, request, id):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(id=id, is_active=True).first()
        if reset_pass_form.is_valid():
            if user is not None:
                user_pass = reset_pass_form.cleaned_data.get('password')
                user.set_password(user_pass)
                user.save()
                return redirect(reverse('login_page'))
            else:
                return render(request, '404.html')
        return render(request, 'Account_Module/reset_password.html', {
            'reset_pass_form': reset_pass_form,
            'user': user
        })


# class ForgetPasswordView(View):
#     def get(self, request):
#         forget_pass_form = ForgetPasswordForm()
#         context = {
#             'forget_pass_form': forget_pass_form
#         }
#         return render(request, 'Account_Module/forget_password.html', context)
#
#     def post(self, request):
#         forget_pass_form = ForgetPasswordForm(request.POST)
#         if forget_pass_form.is_valid():
#             user_email = forget_pass_form.cleaned_data.get('email')
#             user: User = User.objects.filter(email__iexact=user_email).first()
#             if user is not None:
#                 # todo : send forget password email
#                 return redirect(reverse('login_page'))
#             else:
#                 forget_pass_form.add_error('email', 'حساب کاربری با این ایمیل یافت نشد')
#
#         return render(request, 'Account_Module/forget_password.html', {
#             'forget_pass_form': forget_pass_form
#         })
#
#
# class ResetPasswordView(View):
#     def get(self, request, email_active_code):
#         user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
#         if user is not None:
#             reset_pass_form = ResetPasswordForm()
#             return render(request, 'Account_Module/reset_password.html', {
#                 'reset_pass_form': reset_pass_form,
#                 'user': user
#             })
#         else:
#             return render(request, '404.html')
#
#     def post(self, request, email_active_code):
#         reset_pass_form = ResetPasswordForm(request.POST)
#         user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
#         if reset_pass_form.is_valid():
#             if user is not None:
#                 user_new_pass = reset_pass_form.cleaned_data.get('password')
#                 user.set_password(user_new_pass)
#                 user.email_active_code = get_random_string(72)
#                 user.is_active = True
#                 user.save()
#                 return redirect(reverse('login_page'))
#             else:
#                 return render(request, '404.html')
#         return render(request, 'Account_Module/reset_password.html', {
#             'reset_pass_form': reset_pass_form,
#             'user': user
#         })


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
        else:
            return render(request, '404.html')
