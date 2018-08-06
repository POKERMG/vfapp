from functools import wraps

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from vehicle.forms import RegistrationForm

# decorator to handle submission of login and registration forms from modals
def login_or_register(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        context = {}

        if request.method == 'POST':
            if request.POST['form_type'] == 'login_form':
                print('Login form')
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                else:
                    # TODO: Return a 'Login Failed' error message.
                    print("login failed")
                    pass
            elif request.POST['form_type'] == 'registration_form':
                # TODO: handle registration form
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                else:
                    context['registration_form'] = form
                    print(form)
                    # TODO: Return a 'Registration Failed' error message.
                    print("registration failed")
                    pass

        if not request.user.is_authenticated:
            context['login_form'] = AuthenticationForm(auto_id=False)
            if 'registration_form' not in context:
                context['registration_form'] = RegistrationForm(auto_id=False)

        return func(request, context, *args, **kwargs)
    return decorator
