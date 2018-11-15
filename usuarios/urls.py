from django.urls import path, re_path
from usuarios.views import RegistroUsuario
# from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
	path('registrar/', RegistroUsuario.as_view(), name="registrar"),

	# path('login/', LoginView.as_view(template_name='login.html'), name="login"),
	# este path de login toco ponerlo en el url global para q funcionara

	# path('logout/', logout_then_login, name="logout"),

	path('password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_email.html'), name="password_reset"),

	path('password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),

	re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_confirm"),

	path('reset_complete', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
]
