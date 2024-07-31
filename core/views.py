from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from django.contrib.messages import constants
from decimal import Decimal
from datetime import datetime
from .models import Account

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
                        'account_types': Account.ACCOUNT_TYPES,
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
            messages.add_message(request, constants.SUCCESS, f'Conta {account_id} - {account_name} atualizada com sucesso!')
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)
        return redirect('portifolio')
        
    else:
        updt_portifolio = get_object_or_404(Account, id=id)
        return render(request,
                      'portifolio/update_portifolio.html',
                      {
                          'updt_portifolio' : updt_portifolio,
                          'account_types': Account.ACCOUNT_TYPES
                      })

@login_required
def dashboard(request):
    return render(request, 'home.html')

@login_required
def buttons(request):
    return render(request, 'ui-features/buttons.html')

@login_required
def dropdowns(request):
    return render(request, 'ui-features/dropdowns.html')

@login_required
def typography(request):
    return render(request, 'ui-features/typography.html')

@login_required
def tables(request):
    return render(request, 'tables/basic-table.html')

@login_required
def charts(request):
    return render(request, 'charts/chartjs.html')

@login_required
def icons(request):
    return render(request, 'icons/font-awesome.html')

@login_required
def login(request):
    return render(request, 'login.html')

@login_required
def register(request):
    return render(request, 'register.html')

@login_required
def not_found(request):
    return render(request, 'error-404.html')

@login_required
def internal_server_error(request):
    return render(request, 'error-500.html')

@login_required
def blankpage(request):
    return render(request, 'blank-page.html')

@login_required
def documentation(request):
    return render(request, 'docs/documentation.html')
