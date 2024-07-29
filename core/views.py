from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
def forms(request):
    return render(request, 'forms/basic_elements.html')

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
