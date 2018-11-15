from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# form para registrarse o darse de alta

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
