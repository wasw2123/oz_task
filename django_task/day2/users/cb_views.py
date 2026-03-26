from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.core import signing
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import CreateView, FormView
from django.urls import reverse
from users.forms import SignupForm, LoginForm

User = get_user_model()

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()
        signer = TimestampSigner()
        signed_user_email = signer.sign(user.email)
        signer_dump = signing.dumps(signed_user_email)
        url = f'{self.request.scheme}://{self.request.META["HTTP_HOST"]}{reverse("verify_email")}?code={signer_dump}'
        if settings.DEBUG:
            print(url)
        else:
            subject = "Todo 이메일 인증입니다."
            message = f'<a href="{url}">인증링크</a>를 눌러 인증해주세요.'
            #send_email(subject, message, user.email)
            #a_tag사용 불가로 변경
            email = EmailMessage(subject, message, to=[user.email])
            email.content_subtype = 'html'
            email.send()

        context = {
            'user': user
        }

        return render(self.request, 'registration/signup_done.html', context)


MAX_AGE = 10 * 60


def verify_email(request):
    code = request.GET.get('code', '')
    signer = TimestampSigner()
    try:
        decode_user_email = signing.loads(code)
        email = signer.unsign(decode_user_email, max_age=MAX_AGE)
    except (TypeError, SignatureExpired, BadSignature):
        return render(request, 'registration/verify_failed.html')
    user = get_object_or_404(User, email=email, is_active=False)
    user.is_active = True
    user.save()

    context = {
        "user": user
    }
    return render(request, 'registration/verify_success.html', context)

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        next_page = self.request.GET.get('next')
        if next_page and url_has_allowed_host_and_scheme(next_page, allowed_hosts=self.request.get_host()):
            return HttpResponseRedirect(next_page)

        return super().form_valid(form)


