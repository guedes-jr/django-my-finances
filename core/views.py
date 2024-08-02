from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from django.contrib.messages import constants
from decimal import Decimal
from datetime import datetime
from .models import Account, Goal, CreditCard, Transaction
from . import constants as c

@login_required
def dashboard(request):
    return render(request, 'home.html')

@login_required
def portifolio(request):
    if request.method == 'POST':
        try:
            new_portifolio = Account(
                user = request.user,
                account_name=request.POST.get('account_name'),
                account_type=request.POST.get('account_type'),
                balance=Decimal(request.POST.get('balance')),
                created_at=datetime.now(),
            )
            new_portifolio.save()
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)

    portifolios = Account.objects.filter(user=request.user)
    amount = portifolios.aggregate(total=Sum('balance'))['total']
    return render(request, 
                    'portifolio/portifolios.html', 
                    { 
                        'portifolios': portifolios,
                        'account_types': c.ACCOUNT_TYPES,
                        'amount': amount
                    })

@login_required
def delete_portifolio(request, id):
    dlt_portifolio = Account.objects.filter(id=id)
    if dlt_portifolio.count() > 0:
        try:
            dlt_portifolio.delete()
            messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro ao remover a conta, erro: {e}')
    else:
        messages.add_message(request, constants.ERROR, f'Não existe nenhuma conta com o ID {id}')
    return redirect('portifolio')

def update_portifolio(request, id):
    if request.method == 'POST':
        account_name = request.POST.get('account_name')
        account_id = request.POST.get('id')
        try:
            Account.objects.filter(pk=account_id) \
                .update(
                    account_name=account_name,
                    account_type=request.POST.get('account_type'),
                    balance=Decimal(request.POST.get('balance')))
            messages.add_message(request, constants.SUCCESS, f'Conta {account_name} atualizada com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)
        return redirect('portifolio')
        
    else:
        updt_portifolio = get_object_or_404(Account, id=id)
        return render(request,
                      'portifolio/update_portifolio.html',
                      {
                          'updt_portifolio' : updt_portifolio,
                          'account_types': c.ACCOUNT_TYPES
                      })

@login_required
def goal(request):
    if request.method == 'POST':
        try:
            new_goal = Goal(
                user = request.user,
                category=request.POST.get('category'),
                description=request.POST.get('description'),
                current_value=Decimal(request.POST.get('current_value')),
                targeted_value=Decimal(request.POST.get('targeted_value')),
                start_date=request.POST.get('start_date'),
                end_date=request.POST.get('end_date'),
                created_at=datetime.now(),
            )
            new_goal.save()
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)

    goals = Goal.objects.filter(user=request.user)
    return render(request, 
                    'goal/goals.html', 
                    { 
                        'goals': goals,
                        'categorys': c.CATEGORY_CHOICES
                    })

@login_required
def delete_goal(request, id):
    dlt_portifolio = Goal.objects.filter(id=id)
    if dlt_portifolio.count() > 0:
        try:
            dlt_portifolio.delete()
            messages.add_message(request, constants.SUCCESS, 'Meta removida com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro ao remover a Meta, erro: {e}')
    else:
        messages.add_message(request, constants.ERROR, f'Não existe nenhuma Meta com o ID {id}')
    return redirect('goal')

def update_goal(request, id):
    if request.method == 'POST':
        goal_id = request.POST.get('id')
        description = request.POST.get('description')
        try:
            Goal.objects.filter(pk=goal_id) \
                .update(
                        category=request.POST.get('category'),
                        description=description,
                        current_value=Decimal(request.POST.get('current_value')),
                        targeted_value=Decimal(request.POST.get('targeted_value')),
                        start_date=request.POST.get('start_date'),
                        end_date=request.POST.get('end_date'))
                
            messages.add_message(request, constants.SUCCESS, f'Meta {description} atualizada com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)
        return redirect('goal')
        
    else:
        updt_goal = get_object_or_404(Goal, id=id)
        return render(request,
                      'goal/update_goal.html',
                      {
                          'updt_goal' : updt_goal,
                          'categorys': c.CATEGORY_CHOICES
                      })
@login_required
def credcard(request):
    if request.method == 'POST':
        try:
            new_card = CreditCard(
                user = request.user,
                card_type = CreditCard.identify_card_type(request.POST.get('card_number')),
                card_number = request.POST.get('card_number'),
                surname=request.POST.get('surname'),
                cardholder_name=request.POST.get('cardholder_name'),
                expiration_date=request.POST.get('expiration_date'),
                security_code=request.POST.get('security_code'),
                limit=Decimal(request.POST.get('limit')),
                current_limit=Decimal(request.POST.get('current_limit')),
                created_at=datetime.now(),
            )
            new_card.save()
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'{e}\n{new_card.__dict__}')

    credcards = CreditCard.objects.filter(user=request.user)
    return render(request, 
                    'credcard/credcards.html', 
                    { 
                        'credcards': credcards
                    })
    
@login_required
def delete_credcard(request, id):
    dlt_portifolio = CreditCard.objects.filter(id=id)
    if dlt_portifolio.count() > 0:
        try:
            dlt_portifolio.delete()
            messages.add_message(request, constants.SUCCESS, 'Cartão de crétido removido com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro ao remover a Cartão de crédito, erro: {e}')
    else:
        messages.add_message(request, constants.ERROR, f'Não existe nenhum Cartão de crédito com o ID {id}')
    return redirect('credcard')


def update_credcard(request, id):
    if request.method == 'POST':
        card_id = request.POST.get('id')
        surname = request.POST.get('surname')
        try:
            CreditCard.objects.filter(pk=card_id) \
                .update(
                        surname = surname,
                        cardholder_name=request.POST.get('cardholder_name'),
                        expiration_date=request.POST.get('expiration_date'),
                        limit=Decimal(request.POST.get('limit')),
                        current_limit=Decimal(request.POST.get('current_limit'))
                    )
                
            messages.add_message(request, constants.SUCCESS, f'Cartão de crédito {surname} atualizada com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)
        return redirect('credcard')
        
    else:
        updt_credcard = get_object_or_404(CreditCard, id=id)
        return render(request,
                      'credcard/update_credcard.html',
                      {
                          'updt_credcard' : updt_credcard,
                      })

@login_required
def transaction(request):
    if request.method == 'POST':
        try:
            new_transaction = Transaction(
                user = request.user,
                
                created_at=datetime.now(),
            )
            new_transaction.save()
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'{e}\n{new_transaction.__dict__}')

    credcards = CreditCard.objects.filter(user=request.user)
    return render(request, 
                    'credcard/credcards.html', 
                    { 
                        'credcards': credcards
                    })
    
@login_required
def delete_transaction(request, id):
    dlt_portifolio = CreditCard.objects.filter(id=id)
    if dlt_portifolio.count() > 0:
        try:
            dlt_portifolio.delete()
            messages.add_message(request, constants.SUCCESS, 'Cartão de crétido removido com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro ao remover a Cartão de crédito, erro: {e}')
    else:
        messages.add_message(request, constants.ERROR, f'Não existe nenhum Cartão de crédito com o ID {id}')
    return redirect('transaction')


def update_transaction(request, id):
    if request.method == 'POST':
        card_id = request.POST.get('id')
        surname = request.POST.get('surname')
        try:
            CreditCard.objects.filter(pk=card_id) \
                .update(
                        surname = surname,
                        cardholder_name=request.POST.get('cardholder_name'),
                        expiration_date=request.POST.get('expiration_date'),
                        limit=Decimal(request.POST.get('limit')),
                        current_limit=Decimal(request.POST.get('current_limit'))
                    )
                
            messages.add_message(request, constants.SUCCESS, f'Cartão de crédito {surname} atualizada com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)
        return redirect('transaction')
        
    else:
        updt_transaction = get_object_or_404(CreditCard, id=id)
        return render(request,
                      'transaction/update_transaction.html',
                      {
                          'updt_transaction' : updt_transaction,
                      })