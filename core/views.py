from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from django.contrib.messages import constants
from decimal import Decimal
from datetime import datetime
from .models import Account

@login_required
def portifolio(request):
    if request.method == 'POST':
        balance = request.POST.get('balance')
        try:
            new_portifolio = Account(
                user = request.user,
                account_name=request.POST.get('account_name'),
                account_type=request.POST.get('account_type'),
                balance=Decimal(balance),
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
