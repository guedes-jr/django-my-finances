from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Account, Goal, CreditCard
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from .models import CustomUser

User = get_user_model()

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
            return redirect('login')
        except Exception as e:
            # Mensagem de erro
            messages.add_message(request, constants.ERROR, f'Erro interno do sistema: {str(e)}')
            return render(request, 'registration/signup.html')

    return render(request, 'registration/signup.html')


def access(request):
    if request.user.is_authenticated:
        return redirect('/')   

    if request.method == 'GET':
        return render(request, 'registration/access.html')

    elif request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=name,
                            password=password)
    if user is not None:
        login(request, user)
        return redirect('/')    
    else:
        messages.add_message(request, constants.ERROR, 'Usuário e/ou senha incorretos!')
        return render(request, 'registration/access.html')
    
def signout(request):
    logout(request)
    return redirect('/accounts/login')

@login_required
def perfil(request):
    if request.method == 'POST':
        if request.POST.get('password'):
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                messages.add_message(request, constants.ERROR, 'Senha e confirmar senha são diferentes!')
                return redirect('perfil')
            
            try:
                request.user.set_password(new_password)
                request.user.save()
                messages.add_message(request, constants.SUCCESS, 'Senha alterada com sucesso!')
            except Exception as e:
                messages.add_message(request, constants.ERROR, f'Erro ao alterar senha\nErro: {e}')
                
        else:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            cpf_cnpj = request.POST.get('cpf_cnpj')
            username = request.POST.get('username')
            email = request.POST.get('email')
            birth_date = request.POST.get('birth_date')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            bio = request.POST.get('bio')
            description = request.POST.get('description')
            avatar = request.FILES.get('avatar')
            
            # Verificar se todos os campos obrigatórios estão preenchidos
            if any(len(field.strip()) == 0 for field in [first_name, last_name, cpf_cnpj, username, email]):
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
                return redirect('perfil')

            # Verificar se a imagem é menor que 10MB
            if avatar and avatar.size > 10_000_000:
                messages.add_message(request, constants.ERROR, 'A imagem deve ter menos de 10MB')
                return redirect('perfil')
            
            try:
                CustomUser.objects.filter(id=request.POST.get('id')) \
                        .update(
                            first_name=first_name,
                            last_name=last_name,
                            cpf_cnpj=cpf_cnpj,
                            username=username,
                            email=email,
                            birth_date=birth_date,
                            phone_number=phone_number,
                            address=address,
                            bio=bio,
                            description=description
                        )
                if avatar:
                    CustomUser.objects.filter(id=request.POST.get('id')) \
                        .update(
                            avatar=avatar
                        )
                messages.add_message(request, constants.SUCCESS, 'Perfil Atualizado com sucesso')
            except Exception as e:
                messages.add_message(request, constants.ERROR, f'Erro ao atualizar os dados\nErro: {e}')
            
    accounts = Account.objects.filter(user=request.user)    
    goals = Goal.objects.filter(user=request.user)    
    credcards = CreditCard.objects.filter(user=request.user)    
    return render(request, 
                  'perfil/perfil.html',
                  {
                      'accounts': accounts,
                      'goals': goals,
                      'credcards': credcards
                  })

@login_required
def delete_perfil(request):
    return render()
