from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.core.exceptions import ValidationError
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birth_date = request.POST.get('birth_date')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        description = request.POST.get('description')
        avatar = request.FILES.get('avatar')

        print('first_name', first_name)
        print('last_name', last_name)
        print('cpf_cnpj', cpf_cnpj)
        print('username', username)
        print('email', email)
        print('password', password)
        print('birth_date', birth_date)
        print('phone_number', phone_number)
        print('address', address)
        print('bio', bio)
        print('description', description)
        print('avatar', avatar)

        # Verificar se todos os campos obrigatórios estão preenchidos
        if any(len(field.strip()) == 0 for field in [first_name, last_name, cpf_cnpj, username, email, password, confirm_password]) or (not avatar):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('signup')

        # Verificar se a imagem é menor que 10MB
        if avatar.size > 10_000_000:
            messages.add_message(request, constants.ERROR, 'A imagem deve ter menos de 10MB')
            return redirect('signup')

        # Verificar se as senhas são iguais
        if password != confirm_password:
            messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais!')
            return render(request, 'registration/signup.html')
        
        try:
            # Criar o usuário
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                cpf_cnpj=cpf_cnpj,
                username=username,
                email=email,
                password=password,
                birth_date=birth_date,
                phone_number=phone_number,
                address=address,
                bio=bio,
                description=description,
                avatar=avatar
            )
            # Mensagem de sucesso
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return redirect('dashboard')
        except Exception as e:
            # Mensagem de erro
            messages.add_message(request, constants.ERROR, f'Erro interno do sistema: {str(e)}')
            return render(request, 'registration/signup.html')

    return render(request, 'registration/signup.html')


# def logar(request):
#   if request.user.is_authenticated:
#     return redirect('/divulgar/dashboard')   
  
#   if request.method == 'GET':
#     return render(request, 'login.html')
  
#   elif request.method == 'POST':
#     nome = request.POST.get('nome')
#     senha = request.POST.get('senha')

#     user = authenticate(username=nome,
#                         password=senha)
#     if user is not None:
#       login(request, user)
#       return redirect('/divulgar/dashboard')    
#     else:
#       messages.add_message(request, constants.ERROR, 'Usuário e/ou senha incorretos!')
#       return render(request, 'login.html')
    
# def sair(request):
#   logout(request)
#   return redirect('/auth/login')