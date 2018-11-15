from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from usuarios.forms import RegistroForm


class RegistroUsuario(CreateView):
	model = User
	template_name = "registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy("inicio")
