from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from customer.forms import CustomUserCreationForm
from django.contrib import messages


def create_account(request):
    if request.method == 'POST':
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_customer.html', {
        'form': form
    })


def login_customer(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redireciona para a página de perfil do usuário após o login
            return redirect('index')
        else:
            # Exibir uma mensagem de erro se as credenciais forem inválidas
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'registration/login.html')


def logout_customer(request):
    logout(request)
    # Redireciona para a página de login após o logout
    return redirect('index')
